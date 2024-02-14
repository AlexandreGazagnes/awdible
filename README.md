![image](./docs/assets/img/image.png)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/python-3.10.x-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/AlexandreGazagnes/awdible)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
![Coverage](https://github.com/AlexandreGazagnes/awdible/blob/main/docs/assets/img/cov.svg?raw=true)
![Tests](https://github.com/AlexandreGazagnes/awdible/actions/workflows/tests.yaml/badge.svg)
![Statics](https://github.com/AlexandreGazagnes/awdible/actions/workflows/statics.yaml/badge.svg)
![Doc](https://github.com/AlexandreGazagnes/awdible/actions/workflows/docs.yaml/badge.svg)
![Pypi](https://github.com/AlexandreGazagnes/awdible/actions/workflows/publish.yaml/badge.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AlexandreGazagnes/awdible)

# Awdible - Just the best free version of audible

## About
Awdible is a free and open-source software, app and python package that allows you to download music from youtube and convert it to mp3.

The idea is to provide a free version of awdible.

## Key Features

* Download music / audiobook from youtube
* Convert music to mp3
* Find music from a list of songs / audiobook names : Waka Waka, Happy, Harry potter and the philosopher's stone, ...
* Crop a long audio file to a specific duration

## Installation

Using regular pip and venv tools :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install awdible
```

## Usage


### Local


#### As executable :

In a terminal :
* ```awdible [youtube-url] ``` standard usage : download and convert to mp3

* ```awdible -d my/dest [youtube-url] ``` specify a destination folder

* ```awdible -f my_file.txt -d my/dest ``` specify a file list song  / audibooks **urls** and specify destination folder

The my_file.txt file must contain one youtube url per line.
my_file.txt example :
```
https://www.youtube.com/watch?v=3y5A4paFOb4
https://www.youtube.com/watch?v=3y5A4paFOb4
https://www.youtube.com/watch?v=3y5A4paFOb4
```
* ```awdible -f my_file.txt -d my/dest -p ``` specify a file list song  / audibooks **ids** and specify destination folder

The my_file.txt file must contain one youtube id per line.
my_file.txt example :
```
3y5A4paFOb4
3y5A4paFOb4
3y5A4paFOb4
```
* ```awdible -f my_file.txt -s -d my/dest``` specify a file list song / audioobks **names** (not just yourube url) and specify destination folder.

**WARNING**:
- Please note that for the `-s` option, you must have a set up your **[youtube rapid api](https://rapidapi.com/herosAPI/api/youtube-data8)** account. You need to add in your environment variables or export directly from a terminal the following :

```bash
export RAPID_API_KEY="*********"
export RAPID_API_HOST="youtube-data8.p.rapidapi.com"
```


#### As library

In a python file :

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

In a terminal :

* ```awdible gui ``` launch local streamlit

### On line

* The on line web app is temporarily unavailable. It will be available in the `0.2.5` release.


## Documentation

Please visit [Documentation](https://alexandregazagnes.github.io/awdible/) page.


## Changelog, Roadmap and Releases

Please visit [Changelog, Roadmap and Release](https://alexandregazagnes.github.io/awdible/CHANGELOG/) page.

<!-- ## Troubleshooting

Please visit [Troubleshooting](https://alexandregazagnes.github.io/awdible/TROUBLESHOOTING/) page. -->


## Contributing

Awdible is an open-source project and we are always looking for more people to contribute to its development.

It could be by adding new features, fixing bugs, improving the documentation, or any other way you see fit.

Any help is welcome, and we will do our best to help you get started.

Any feedback is also welcome.

Please visit [Contributing](https://alexandregazagnes.github.io/awdible/CONTRIBUTING/) page.
