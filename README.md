![image](./assets/img/image.png)

# Audible


## Description

Just a free version of audible.

## Access

Please visit [Audible on Streamlit]("https://audible.streamlit.app/") web app


# Usage 

## As executable


* ```audible [youtube-url]``` standard usage

* ```audible -o mp3 -d my/dest [youtube-url]``` standard usage

* ```aubible -f my_file.txt -o mp3 -d my/dest``` specify a file list of **youtube urls** and output format and destination folder
  
* ```aubible -f my_file.txt -o mp3 -r -d my/dest``` specify a file list ***song names** and output format and destination folder




## As library

```python

from audible import Audible

Audible.download("https://www.youtube.com/watch?v=3y5A4paFOb4")

```

## As web app

Please visit [Audible on Streamlit]("https://audible.streamlit.app/") web app
* ```audible gui``` : lunch local streamlit 

