#! /bin/sh

# docker base
docker build -f .utils/Dockerfile.base -t sktransf:base .

# docker build
docker build --no-cache -f .utils/Dockerfile -t sktransf:latest .

# docker run
# docker run -ti sktransf:latest /bin/bash
docker run -ti sktransf:latest python3 -m IPython
