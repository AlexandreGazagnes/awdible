![image](./docs/assets/img/image.png)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python](https://img.shields.io/badge/python-3.10.x-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/AlexandreGazagnes/audible)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
![Coverage](https://github.com/AlexandreGazagnes/audible/blob/main/docs/assets/img/cov.svg?raw=true)
![Tests](https://github.com/AlexandreGazagnes/audible/actions/workflows/tests.yaml/badge.svg)
![Statics](https://github.com/AlexandreGazagnes/audible/actions/workflows/statics.yaml/badge.svg)
![Doc](https://github.com/AlexandreGazagnes/audible/actions/workflows/docs.yaml/badge.svg)
![Pypi](https://github.com/AlexandreGazagnes/audible/actions/workflows/publish.yaml/badge.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AlexandreGazagnes/audible)

# Audible

## About 
Audible is a free and open-source software that allows you to download music from youtube and convert it to mp3.

The idea is to provide a free version of audible.

## Key Features

* Download music from youtube
* Convert music to mp3
* Find music from a list of songs names

## Installation

Using regular pip and venv tools :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install audible
```

## Usage

### On line 

Please visit [Audible on Streamlit]("https://audible.streamlit.app/") web app


### Local


As executable : 

* ```audible [youtube-url]``` standard usage

* ```audible -o mp3 -d my/dest [youtube-url]``` standard usage

* ```aubible -f my_file.txt -o mp3 -d my/dest``` specify a file list of **youtube urls** and output format and destination folder
  
* ```aubible -f my_file.txt -o mp3 -r -d my/dest``` specify a file list ***song names** and output format and destination folder



As library : 

```python
from audible import Audible
Audible.download("https://www.youtube.com/watch?v=3y5A4paFOb4")
```

As web app : 



* ```audible gui``` : launch local streamlit 



## Documentation

Please visit [Documentation](https://alexandregazagnes.github.io/audible/) page.


## Changelog, Roadmap and Releases

Please visit [Changelog, Roadmap and Release](https://alexandregazagnes.github.io/audible/CHANGELOG/) page.

## Troubleshooting

Please visit [Troubleshooting](https://alexandregazagnes.github.io/audible/TROUBLESHOOTING/) page.


## Contributing

Please visit [Contributing](https://alexandregazagnes.github.io/audible/CONTRIBUTING/) page.


