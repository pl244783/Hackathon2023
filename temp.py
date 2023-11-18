
# import the opencv library 
import cv2 
import numpy as np
  
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True): 
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

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

        for line in parallel_lines:
            cv2.line(gray, (line[0][0], line[0][1]), (line[0][2], line[0][3]), (255, 255, 255), 2)
            cv2.line(gray, (line[1][0], line[1][1]), (line[1][2], line[1][3]), (255, 255, 255), 2)

    # Display the resulting frame 
    cv2.imshow('frame', gray) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 