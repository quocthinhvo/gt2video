from fastapi import FastAPI
from typing import List
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 

import os

app = FastAPI()
app.mount("/videos", StaticFiles(directory="videos"), name="videos")
app.mount("/js", StaticFiles(directory="js"), name="js")


@app.get('/')
async def read_index():
    return FileResponse('index.html')
@app.get("/test")
def read_root():
    return {"status": "ok"}

@app.get("/list_videos")
def get_list_videos():
    list_videos = os.listdir('videos/') 
    return JSONResponse(list_videos)

