![image](https://github.com/AlexandreGazagnes/awdible/blob/main/docs/assets/img/image.png?raw=true)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/python-3.10.x-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/AlexandreGazagnes/awdible)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
<!-- ![Coverage](https://github.com/AlexandreGazagnes/awdible/blob/main/docs/assets/img/cov.svg?raw=true) -->
![Tests](https://github.com/AlexandreGazagnes/awdible/actions/workflows/tests.yaml/badge.svg)
![Statics](https://github.com/AlexandreGazagnes/awdible/actions/workflows/statics.yaml/badge.svg)
![Doc](https://github.com/AlexandreGazagnes/awdible/actions/workflows/docs.yaml/badge.svg)
<!-- ![Pypi](https://github.com/AlexandreGazagnes/awdible/actions/workflows/publish.yaml/badge.svg) -->
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AlexandreGazagnes/awdible)

# Awdible - Just the best free version of audible

## About
Awdible is a free and open-source software, app and python package that allows you to download music from youtube and convert it to mp3.

The idea is to provide a free version of audible.

## Key Features

* Download music / audiobook from youtube
* Convert music / audiobook to mp3 / wave / flac (...) *need ffmpeg installed*
* Automaticly crop a long audio file to a specific duration ie 60 minutes
* Find music / audiobook from a list of songs / audiobook names : Waka Waka, Happy, Harry potter and the philosopher's stone, (...) *need specific api keys*
* Add specfic context about a file such as live, album, or title


## Installation

Using regular pip and venv tools :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install awdible
```


## Third party dependencies

### FFmpeg

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

### External api

Some features of Awdible require external api keys, specially the `-s` option.


you must have a set up your **[youtube rapid api](https://rapidapi.com/herosAPI/api/youtube-data8)** account. 

You need to add in your environment variables or export directly from a terminal the following :

```bash
export RAPID_API_KEY="*********"
export RAPID_API_HOST="youtube-data8.p.rapidapi.com"
```

### Internet connection

Last but not least, Please not that a valid internet connection is required to use ```Awdible```.


## Usage


### Local



#### As executable


Standard usage, download and convert to mp3 :

```shell
awdible [youtube-url] 
``` 

Specify a destination folder : 
```shell
awdible -d my/dest [youtube-url]
``` 
Specify a file list song  / audibooks **urls** and specify destination folder : 
```shell
awdible -f my_file.txt -d my/dest
``` 

The my_file.txt file must contain one youtube url per line.
my_file.txt example :
```
https://www.youtube.com/watch?v=3y5A4paFOb4
https://www.youtube.com/watch?v=3y5A4paFOb4
https://www.youtube.com/watch?v=3y5A4paFOb4
```
Specify a file list song  / audibooks **ids** and specify destination folder : 
```shell
awdible -f my_file.txt -d my/dest -p
``` 
The my_file.txt file must contain one youtube id per line.
my_file.txt example :
```shell
3y5A4paFOb4
3y5A4paFOb4
3y5A4paFOb4
```
Specify a file list song / audiooks **names** (not just yourube url) and specify destination folder :
```shell
awdible -f my_file.txt -s -d my/dest
``` 

The my_file.txt file must contain one youtube id per line.
my_file.txt example :
```shell
waka waka shakira
Stand by me
Somewhere over the rainbow
```

⚠️ **WARNING** ⚠️

Please note that for the `-s` option, you must have a set up your **[youtube rapid api](https://rapidapi.com/herosAPI/api/youtube-data8)** account. 

You need to add in your environment variables or export directly from a terminal the following :

```bash
export RAPID_API_KEY="*********"
export RAPID_API_HOST="youtube-data8.p.rapidapi.com"
```


#### As library


```python
from awdible import Awdible

url = "https://www.youtube.com/watch?v=3y5A4paFOb4"
awdible = Awdible(url)
awdible.run()

# or

urls = [
    "https://www.youtube.com/watch?v=3y5A4paFOb4",
    "https://www.youtube.com/watch?v=3y5A4paFOb4",
    "https://www.youtube.com/watch?v=3y5A4paFOb4"
    ]

awdible = Awdible(urls)
awdible.run()
```

#### As web app

Launch local streamlit : 

```shell
awdible gui 
``` 

### On line

The on line web app is temporarily unavailable. 

It will be available in the `0.3.0` release.


## Documentation

Please visit [Documentation](https://alexandregazagnes.github.io/awdible/) page.


## Updates


Please visit the : 
* [Changelog](https://alexandregazagnes.github.io/awdible/changelog) page 
* [Roadmap](https://github.com/AlexandreGazagnes/awdible/projects?query=is%3Aopen) page
* [Release](https://github.com/AlexandreGazagnes/awdible/releases) page
* [Issues](https://github.com/AlexandreGazagnes/awdible/issues) page



## Contributing

Awdible is an open-source project and we are always looking for more people to contribute to its development.

It could be by adding new features, fixing bugs, improving the documentation, or any other way you see fit.

Any help is welcome, and we will do our best to help you get started.

Any feedback is also welcome.

Please visit [Contributing](https://alexandregazagnes.github.io/awdible/contributing/) page.
