# Usage

## 🏠 Local



### As executable


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


### As library


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

### As web app

Launch local streamlit : 

```shell
awdible gui 
``` 

## 🌏 On line

The on line web app is temporarily unavailable. 

It will be available in the `0.3.0` release.
