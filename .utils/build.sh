#! /bin/bash

# build docker image
# --progress=plain for showing progress bar
docker build -f ./Dockerfile  -t awdible:latest . 

# run docker image
# -d for detached mode
sudo docker run  -p 8501:8501 --env-file .env/.env.dev awdible:latest

# if needed to run bash inside container
# docker exec -it <container-name> /bin/bash