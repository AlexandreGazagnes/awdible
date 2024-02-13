# Usage


## Local


## As executable :

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


## As library

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

## As web app

In a terminal :

* ```awdible gui ``` launch local streamlit

## On line

* The on line web app is temporarily unavailable. It will be available in the `0.2.5` release.

## New features

Awdible is an open-source project and we are always looking for more people to contribute to its development.

It could be by adding new features, fixing bugs, improving the documentation, or any other way you see fit.

Any help is welcome, and we will do our best to help you get started.

Any feedback is also welcome.

Please visit [Contributing](https://alexandregazagnes.github.io/awdible/CONTRIBUTING/) page.
