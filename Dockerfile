FROM python:3.10.9-bullseye

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
WORKDIR /app/Dastres
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY * .