import cv2
from threading import Thread

class Webcam:
   
    def __init__(self):
        
        #starting cv2's video capture functionality
        #without the cv2.cap_dshow attribute, the program does not function
        self.video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        #capturing the video frame as an image for later processing
        self.current_frame = self.video_capture.read()[1]
           
    def capture_start(self):

        #creating multiprocessing thread to capture frames and send midi signals at same time
        p=Thread(target=self._update_frame, args=())
        p.start()
    
    
    def _update_frame(self):
        #updating the image that is being processed as time passes (for testing purposes)
        while(True):
            self.current_frame = self.video_capture.read()[1]
                   
    
    def refresh_image(self):
        #Obtaining the current frame
        return self.current_frame