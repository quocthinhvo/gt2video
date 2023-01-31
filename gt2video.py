import os
import sys
import cv2
import time
from pathlib import Path


    
# Read agrv
path_video = sys.argv[2]
path_gt = sys.argv[1]
id_video = path_video
# Read gt.txt file and collect true id video
f = open(path_gt, "r")
lists_box = []
    

for line in f:
    if (f.readline().split(",")[0] == str(int(Path(path_video).stem))):
        lists_box.append(f.readline().split(","))

cap = cv2.VideoCapture(path_video)
  
output = cv2.VideoWriter(
    "output.avi", cv2.VideoWriter_fourcc(*'MPEG'), 
    30, (1080, 1920))

for line in lists_box:
    line[1] = int(line[1])
    line[3] = int(line[3])
    line[4] = int(line[4])
    line[5] = int(line[5])
    line[6] = int(line[6])

    frame_counter = 1
while(True):
    ret, frame = cap.read()
    if(ret):  
        print(frame_counter)   
        for line in lists_box:
            if (line[1] == frame_counter):
                print(line)
                tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(0, 255, 0), 1)  
                cv2.putText(tmp_frame, line[2] + " - class: " + line[7], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
        cv2.imshow(path_video, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    time.sleep(0.05)
    frame_counter += 1

cv2.destroyAllWindows()
output.release()
cap.release()