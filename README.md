#  Road Lane Tracking using OpenCV

## Introduction
In this project, I am using OpenCV to process the video file step by step to obatin the following result.

*   **Steps:**
*    Defining the Region of interest by inspecting the situation. 
        *   In this case, as the person is driving on the right lane, it is in our better interest to define the process region to slightly rightward inclined to get better results. (In the real world scenario, the video won't be this much wide) 
*   Converting the image object to canny image.
* Creation of lines on a blank frame of the same resolution.


*   **Functions:**
    *   *region_of_interest* function will take the *canny_image* (converted from our *image* object) object and the region of interest parameters and then will specify an area for our processing.
    *   Further using the HoughLinesP function from OpenCV, defining the line parameters for our canny_image object.
    *   *draw_the_line* function will take the original image and the *line* object and then draw an overlay over our actual image frame.

*   In the next step, applying the process by reading and parsing the *capture* frame by frame and then process the capture.

## In action

![Processed video](https://raw.githubusercontent.com/sarbhanub/OpenCV-LaneDetection/master/data/screenshots/video-converted.gif)

  
### Acknowledgements

 - [Video Source (Pexels)](https://www.pexels.com/video/video-of-travel-854669/)
  