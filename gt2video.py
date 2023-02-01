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
    tmp_line = f.readline()
    if (tmp_line.split(",")[0] == str(int(Path(path_video).stem))):
        lists_box.append(tmp_line.split(","))

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
print(len(lists_box))

while(True):
    ret, frame = cap.read()
    if(ret):  
        print(frame_counter)   
        for line in lists_box:
            if (line[1] == frame_counter):
                # print(line)
                match line[7][0:1]:
                    case '1':
                        tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(0, 255, 0), 1)  
                        cv2.putText(tmp_frame, line[2] + " - class: " + line[7][0:1], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                    case '2':
                        tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(252, 186, 3), 1)  
                        cv2.putText(tmp_frame, line[2] + " - class: " + line[7][0:1], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (252, 186, 3), 2)
                    case '3':
                        tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(3, 49, 252), 1)  
                        cv2.putText(tmp_frame, line[2] + " - class: " + line[7][0:1], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (3, 49, 252), 2)
                    case '4':
                        tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(219, 3, 252), 1)  
                        cv2.putText(tmp_frame, line[2] + " - class: " + line[7][0:1], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (219, 3, 252), 2)
                    case '5':
                        tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(3, 252, 252), 1)  
                        cv2.putText(tmp_frame, line[2] + " - class: " + line[7][0:1], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (3, 252, 252), 2)
                    case '6':
                        tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(252, 3, 20), 1)  
                        cv2.putText(tmp_frame, line[2] + " - class: " + line[7][0:1], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (252, 3, 20), 2)
                    case '7':
                        tmp_frame = cv2.rectangle(frame, (line[3], line[4]), (line[3] + line[5], line[4] + line[6]),(252, 231, 3), 1)  
                        cv2.putText(tmp_frame, line[2] + " - class: " + line[7][0:1], (line[3], line[4]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (252, 231, 3), 2)
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