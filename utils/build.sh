#! /bin/bash

# build docker image
# --progress=plain
docker build -f ./Dockerfile  -t audible:latest . 

# run docker image
# sudo docker run  -p 8501:8501 -d --env-file .env/.env.dev audible:latest
sudo docker run  -p 8501:8501 --env-file .env/.env.dev audible:latest