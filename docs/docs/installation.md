# Installation


## 🎠 Using regular pip and venv tools

Creating a virtual environment :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

It is recommended to use a virtual environment to install the package.

Installing the package :

```bash
pip install awdible [--upgrade] [--user]

```

## 🌂 Using poetry or pipenv

It is recommended to use a virtual environment to install the package.

```bash
pip install poetry
poetry init
poetry add awdible
```



## 🍀 Check the installation

You can check the installation by running the following command :

```bash
pip show awdible
```

or 

```bash
awdible --version
```

or

```bash
pip list | grep awdible
```


## ⚠️ Third party dependencies

### 📼 FFmpeg

Please note that you should to have [ffmpeg](https://ffmpeg.org/) installed on your system to use certain features of Awdible.

On Ubuntu, Debian, Linux Mint (...) you can install it with the following command :
```bash
sudo apt update
sudo apt install ffmpeg -y 
```

On fedora, Red Hat, CentOS (...) you can install it with the following command :
```bash
sudo dnf install ffmpeg
```

On MacOs, you can install it with the following command :
```bash
brew install ffmpeg
```

Please check that the ffmpeg command is available in your terminal.

```bash
ffmpeg -version
```

If you have any issues with ffmpeg, please visit the [ffmpeg](https://ffmpeg.org/) website.

**It is possible not to have ffmpeg installed** but in such case, you will not be able to convert the downloaded files to mp3, wave, flac, etc.

### ⚛️ External api

Some features of Awdible require external api keys, specially the `-s` option.


you must have a set up your **[youtube rapid api](https://rapidapi.com/herosAPI/api/youtube-data8)** account. 

You need to add in your environment variables or export directly from a terminal the following :

```bash
export RAPID_API_KEY="*********"
export RAPID_API_HOST="youtube-data8.p.rapidapi.com"
```

### 🌎 Internet connection

Last but not least, Please not that a valid internet connection is required to use ```Awdible```.
