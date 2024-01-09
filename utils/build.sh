#! /bin/bash

# build docker image
docker build -f ./Dockerfile -t audible:latest . 

# run docker image
sudo docker run  -p 8501:8501 -d --env-file .env.dev audible:latest