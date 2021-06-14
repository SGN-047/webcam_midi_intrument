import cv2
import numpy as np
 
class Detection(object):
 
    THRESHOLD = 1500
 
    def __init__(self, image):
        
        #converting input color to black and white for easier processing
        self.previous_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    def active_div(self, image):
        
        #obtain a new input image array
        current_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        #find difference between previous and current image arrays
        delta = cv2.absdiff(self.previous_gray, current_gray)
        
        #any pixels with value greater than 25 is replaced by 255
        threshold_image = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
 
        cv2.imshow('OpenCV Detection', image)
        cv2.waitKey(10)
 
        #storing new image
        self.previous_gray = current_gray
 
        # set cell width
        h, w = threshold_image.shape[:2]
        cell_width = w//7
 
        #storing the range in which the delta value exists (according to image divisions and octaves)
        cells = np.array([0, 0, 0, 0, 0, 0, 0])
        #splitting the threshold image previously obtained into 7 divisions 
        #the countNonZero function returns the number of non-zero elements in division
        cells[0] = cv2.countNonZero(threshold_image[0:h, 0:cell_width])
        cells[1] = cv2.countNonZero(threshold_image[0:h, cell_width:cell_width*2])
        cells[2] = cv2.countNonZero(threshold_image[0:h, cell_width*2:cell_width*3])
        cells[3] = cv2.countNonZero(threshold_image[0:h, cell_width*3:cell_width*4])
        cells[4] = cv2.countNonZero(threshold_image[0:h, cell_width*4:cell_width*5])
        cells[5] = cv2.countNonZero(threshold_image[0:h, cell_width*5:cell_width*6])
        cells[6] = cv2.countNonZero(threshold_image[0:h, cell_width*6:w])
 
        # obtaining the most active range
        to_press =  np.argmax(cells)
 
        # return the most active cell, if threshold met
        if(cells[to_press] >= self.THRESHOLD):
            return to_press
        else:
            return None