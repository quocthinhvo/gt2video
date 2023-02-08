FROM python:3.11.1-slim

WORKDIR /app

COPY requirements.txt .
RUN apt update && apt install  libgl1-mesa-glx libxrender1 libfontconfig1libglib2.0-0 
RUN pip install -r requirements.txt

COPY . .