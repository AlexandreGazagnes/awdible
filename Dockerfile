FROM python:3.10-buster

WORKDIR /app

# RUN apt-get update -y && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/streamlit/streamlit-example.git .

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8501

# RUN ls -alh

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]