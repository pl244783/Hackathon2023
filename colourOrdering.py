import cv2
import numpy as np
    
# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True): 
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # ## mask of green (36,0,0) ~ (70, 255,255)
    # mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
    # ## mask o yellow (15,0,0) ~ (36, 255, 255)
    # mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
    # ## final mask and masked
    # mask = cv2.bitwise_or(mask1, mask2)
    # target = cv2.bitwise_and(frame,frame, mask=mask)

    # convert to LAB space
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    # store the a-channel
    a_channel = lab[:,:,1]
    # Automate threshold using Otsu method
    th = cv2.threshold(a_channel,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    # Mask the result with the original image
    masked = cv2.bitwise_and(frame, frame, mask = th)

    cv2.imshow('frame', masked)
      
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lb=np.array([15, 0, 0])
    # ub=np.array([36, 255, 255])
    # mask = cv2.inRange(frame, lb, ub)   
    # if 255 in mask:
    #     print("yellow color present")
    # else:
    #     print('yellow colour is not present')

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
