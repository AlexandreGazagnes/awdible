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

# Awdible

## About
Awdible is a free and open-source software that allows you to download music from YouTube and convert it to an MP3.

The idea is to provide a free version of Audible.

## Key Features

* Download music from YouTube
* Convert music to MP3
* Find music from a list of songs names

## Installation

Using regular pip and venv tools :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install awdible
```

## Usage

### Online

Please visit [Awdible on Streamlit]("https://awdible.streamlit.app/") web app


### Local


As executable :

* ```awdible [youtube-url]``` standard usage

* ```awdible -o mp3 -d my/dest [youtube-url]``` standard usage

* ```awdible -f my_file.txt -o mp3 -d my/dest``` specify a file list of **YouTube urls** and output format and destination folder

* ```awdible -f my_file.txt -o mp3 -s -d my/dest``` specify a file list ***song names** and output format and destination folder



As library :

```python
from awdible import Awdible
Awdible.download("https://www.youtube.com/watch?v=3y5A4paFOb4")
```

As web app :

* ```awdible gui``` : launch local streamlit



## Documentation

Please visit [Documentation](https://alexandregazagnes.github.io/awdible/) page.


## Changelog, Roadmap and Releases

Please visit [Changelog, Roadmap and Release](https://alexandregazagnes.github.io/awdible/CHANGELOG/) page.

## Troubleshooting

Please visit [Troubleshooting](https://alexandregazagnes.github.io/awdible/TROUBLESHOOTING/) page.


## Contributing

Awdible is an open-source project and is far from perfect. We are constantly aiming to improve, so contribution and feedback from developers with any level of experience is greatly appreciated! Issues are marked with various tag, some of which are good first issues, making it a great place for beginners and new open-source contributors to start. Areas that you could look to contribute towards may range from adding or suggesting new app features, debugging, and documentation revision. Feedback and testing regarding any of the features will help our overall development process, so feel free to suggest anything that you can think of.

If you have any questions about the project or don't know where to start, feel free to reach out and we'll help you get started! Otherwise, you can check out the Issues tab to see the open issues that currently need to be fixed. If you find any bugs or would like to request new features, you can click on "New Issue" and note the deatils accordingly. If there is a bug, please describe the bug in the issue and the steps that are needed to replicate it so that it can be fixed in a timely manner.

For major changes and new requests, please open an issue first so that we can reach out and discuss the changes before implementing it into the project. In the future, we may create other forms of communication through apps such as Slack or Discord, but for now please refer to the Issues tab for project communication purposes. 

Please visit [Contributing](https://alexandregazagnes.github.io/awdible/CONTRIBUTING/) page.
