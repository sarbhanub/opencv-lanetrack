# imports
import numpy as np
import matplotlib.pylab as plt
import cv2

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = image.shape[2]
    # match_mask_color = (255,) * channel_count # for rgb image only
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_line(img, lines):
    img = np.copy(img)
    blnk_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blnk_img, (x1, y1), (x2, y2), (0,0,255), thickness=5)
    img = cv2.addWeighted(img, 0.8, blnk_img, 1, 0.0)
    return img


# image = cv2.imread('data/test_image/road.jpg')   # converting to opcv obj
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def process(image):
    # values for the data
    # print(image.shape) # to get resolution
    height = image.shape[0]  # height
    width = image.shape[1]  # width
    '''
    defining region of interest for the data.
    adjusting height and width.
    as the lane is in right path, we can expect to follow the lines in the right side of the frame,
    thus using 3/4 & 1/4 ratio for our interest area tupple.
    '''
    region_of_interest_vertices = [(0, height), (3*width / 4, height / 4), (width, height)]

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 200, 200)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32), )
    lines = cv2.HoughLinesP(cropped_image,
                            rho=6,
                            theta=np.pi/60,
                            threshold=150,
                            lines=np.array([]),
                            minLineLength=25,
                            maxLineGap=40)
    image_with_lines = draw_the_line(image, lines)
    # plt.imshow(image_with_lines)
    # plt.show()
    return image_with_lines


cap = cv2.VideoCapture('data/video/video.mp4') # reading video file
while(cap.isOpened):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('vid_frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('b'):
        break

cap.release()
cv2.destroyWindow(winname='vid_frame')