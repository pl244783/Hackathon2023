import numpy as np 
import cv2 
  
  
# Capturing video through webcam 
webcam = cv2.VideoCapture(0) 
  
# Start a while loop 
while(1): 
    y3 = []
    height = {}
    # Reading the video from the 
    # webcam in image frames 
    _, base = webcam.read() 

    # lab = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2LAB)
    # # store the a-channel
    # a_channel = lab[:,:,1]
    # # Automate threshold using Otsu method
    # th = cv2.threshold(a_channel,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    # # Mask the result with the original image
    # imageFrame = cv2.bitwise_and(imageFrame, imageFrame, mask = th)

    hsv = cv2.cvtColor(base, cv2.COLOR_BGR2HSV)
    ## mask of green (36,0,0) ~ (70, 255,255)
    mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
    ## mask o yellow (15,0,0) ~ (36, 255, 255)
    mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
    ## final mask and masked
    mask = cv2.bitwise_or(mask1, mask2)
    imageFrame = cv2.bitwise_and(base,base, mask=mask)
  
    # Convert the imageFrame in  
    # BGR(RGB color space) to  
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
  
    # Set range for red color and  
    # define mask 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
  
    # Set range for green color and  
    # define mask 
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
  
    # Set range for blue color and 
    # define mask 
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
      
    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
 
  
    # Creating contour to track green color 
    contours, hierarchy = cv2.findContours(green_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 500): 
            x, y1, w, h = cv2.boundingRect(contour) 
            base = cv2.rectangle(base, (x, y1),  
                                       (x + w, y1 + h), 
                                       (0, 255, 0), 2) 
              
            cv2.putText(base, "Yellow Colour", (x, y1), 
                        cv2.FONT_HERSHEY_SIMPLEX,  
                        1.0, (0, 255, 0)) 
            
            y3.append(y1)
            height['yellow'] = y1
    
    _, baseFrame = webcam.read() 
  
    lab = cv2.cvtColor(baseFrame, cv2.COLOR_BGR2LAB)
    # store the a-channel
    a_channel = lab[:,:,1]
    # Automate threshold using Otsu method
    th = cv2.threshold(a_channel,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    # Mask the result with the original image
    baseFrame = cv2.bitwise_and(baseFrame, baseFrame, mask = th)

     # Convert the baseFrame in  
    # BGR(RGB color space) to  
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(baseFrame, cv2.COLOR_BGR2HSV) 
  
    # Set range for red color and  
    # define mask 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
  
    # Set range for green color and  
    # define mask 
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
  
    # Set range for blue color and 
    # define mask 
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
      
    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
 
  
    # Creating contour to track green color 
    contours, hierarchy = cv2.findContours(green_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    
    real = True
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 500):
            x, y2, w, h = cv2.boundingRect(contour) 
            for n in y3:
                if np.abs(n-y2) > 5:
                    pass
                else: 
                    real = False 
            if real:
                base = cv2.rectangle(base, (x, y2),  
                                        (x + w, y2 + h), 
                                        (0, 255, 0), 2) 
                
                cv2.putText(base, "Green Colour", (x, y2), 
                            cv2.FONT_HERSHEY_SIMPLEX,  
                            1.0, (0, 255, 0)) 
                
                height['green'] = y2
    # Python code for Multiple Color Detection 

	# Reading the video from the 
	# webcam in image frames 
    _, imageFrame = webcam.read() 


    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

    # Set range for red color and 
    # define mask 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 

    # Set range for green color and 
    # define mask 
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

    # Set range for blue color and 
    # define mask 
    blue_lower = np.array([60, 80, 2], np.uint8) 
    blue_upper = np.array([150, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 

    kernel = np.ones((5, 5), "uint8") 

    # For red color 
    red_mask = cv2.dilate(red_mask, kernel) 
    res_red = cv2.bitwise_and(imageFrame, imageFrame, 
                            mask = red_mask) 

    # For green color 
    green_mask = cv2.dilate(green_mask, kernel) 
    res_green = cv2.bitwise_and(imageFrame, imageFrame, 
                                mask = green_mask) 

    # For blue color 
    blue_mask = cv2.dilate(blue_mask, kernel) 
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
                            mask = blue_mask) 

    # Creating contour to track red color 
    contours, hierarchy = cv2.findContours(red_mask, 
                                        cv2.RETR_TREE, 
                                        cv2.CHAIN_APPROX_SIMPLE) 

    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            base = cv2.rectangle(base, (x, y), 
                                    (x + w, y + h), 
                                    (0, 0, 255), 2) 
            
            cv2.putText(base, "Pink Colour", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                        (0, 0, 255))	 
            
            height['pink'] = y
    
    # Creating contour to track blue color 
    contours, hierarchy = cv2.findContours(blue_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (255, 0, 0), 2) 
              
            cv2.putText(imageFrame, "Probably Tank", (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (255, 0, 0)) 

    if 'green' not in height:
        height['green'] = 280

    print(dict(sorted(height.items())))
        
    # Program Termination 
    cv2.imshow("Multiple Color Detection in Real-TIme", base) 
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        cap.release() 
        cv2.destroyAllWindows() 
        break