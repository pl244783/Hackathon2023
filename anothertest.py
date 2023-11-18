import cv2
import numpy as np
    
# define a video capture object 
vid = cv2.VideoCapture(0) 

while(True): 
    ret, frame = vid.read() 

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # ## mask of green (36,0,0) ~ (70, 255,255)
    # mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
    # ## mask o yellow (15,0,0) ~ (36, 255, 255)
    # mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
    # ## final mask and masked
    # mask = cv2.bitwise_or(mask1, mask2)
    # masked = cv2.bitwise_and(frame,frame, mask=mask)
    #frame = cv2.resize(frame, dsize=(500,500))
    # convert to LAB space
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    # store the a-channel
    a_channel = lab[:,:,1]
    # Automate threshold using Otsu method
    th = cv2.threshold(a_channel,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    # Mask the result with the original image
    masked = cv2.bitwise_and(frame, frame, mask = th)

    green = [0,255,0]
    yellow = [255, 255, 0]
    # if frame is not None:
    #     Y1, X1 = np.where(np.all(masked== green,axis=2))
    #     Y2, X2 = np.where(np.all(masked== yellow,axis=2))
    #     z1 = np.column_stack((X1,Y2))
    #     z2 = np.column_stack((X2, Y2))

    #     print(z1, '\n\n\n\n\nAHHHHHHHHHHHHHHHHHHHHHHHz\n\n\n\n\n', z2)

    edges = cv2.Canny(masked, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=70, minLineLength=100, maxLineGap=100)
  
    parallel_lines = []
    if lines is not None:
        for i in range(len(lines)):
            for j in range(i+1, len(lines)):
                line1 = lines[i][0]
                line2 = lines[j][0]
                angle1 = np.arctan2(line1[1]-line1[3], line1[0]-line1[2]) * 180 / np.pi
                angle2 = np.arctan2(line2[1]-line2[3], line2[0]-line2[2]) * 180 / np.pi
                if np.abs(angle1 - angle2) < 5 and np.abs(180 - angle1) < 5:
                    parallel_lines.append((line1, line2))

        frame1, frame2, frame3 = False, False, False
        colours = []
        colorLocation = []
        for line in parallel_lines:
            if int((line[0][0]+line[1][0])/2) < 450 and np.abs(line[0][1] - line[1][1]) < 20:
                cv2.line(masked, (line[0][0], line[0][1]), (line[0][2], line[0][3]), (255, 255, 255), 2)
                cv2.line(masked, (line[1][0], line[1][1]), (line[1][2], line[1][3]), (255, 255, 255), 2)
                #if int((line[0][0]+line[1][0])/2) < 450 and np.abs(line[0][1] - line[1][1]) < 20:
                #color = masked[int((line[0][0]+line[1][0])/2), int((line[0][1]+line[1][1])/2)]

            

    cv2.imshow('frame', masked)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 