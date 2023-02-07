from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, File, UploadFile
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import cv2
from pathlib import Path
import time
import sys
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws0")
async def get_stream(websocket: WebSocket, path_video: str, path_gt: str):
    await websocket.accept()
    try:
        # path_video = "D:\\Code\\gt2video\\data\\videos\\002.mp4"
        # path_gt = "D:\\Code\\gt2video\\data\\gt.txt"
        id_video = str(int(Path(path_video).stem))
        # Read gt.txt file and collect true id video
        f = open(path_gt, "r")
        lists_box = []
        for line in f:
            if (line.split(",")[0] == id_video):
                lists_box.append(line.split(","))

        cap = cv2.VideoCapture(path_video)
        fps_value = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count/fps_value
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
                ret, buffer = cv2.imencode('.jpg', frame)
                await websocket.send_bytes(buffer.tobytes())
            else:
                break
            time.sleep(1/(frame_count/duration))
            frame_counter += 1
        cap.release()
    except WebSocketDisconnect:
        print("Client disconnected")   

@app.websocket("/ws1")
async def get_stream1(websocket: WebSocket, path_video: str, path_gt: str):
    await websocket.accept()
    try:
        # path_video = "D:\\Code\\gt2video\\data\\videos\\002.mp4"
        # path_gt = "D:\\Code\\gt2video\\data\\gt.txt"
        print(path_gt)
        print(path_video)
        id_video = str(int(Path(path_video).stem))
        # Read gt.txt file and collect true id video
        f = open(path_gt, "r")
        lists_box = []
        for line in f:
            if (line.split(",")[0] == id_video):
                lists_box.append(line.split(","))

        cap = cv2.VideoCapture(path_video)
        fps_value = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count/fps_value
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
                ret, buffer = cv2.imencode('.jpg', frame)
                await websocket.send_bytes(buffer.tobytes())
            else:
                break
            time.sleep(1/(frame_count/duration))
            frame_counter += 1
        cap.release()
    except WebSocketDisconnect:
        print("Client disconnected")   
