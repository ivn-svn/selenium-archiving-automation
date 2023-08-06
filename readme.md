## Scripts for Web Archives or basic Web & Data Scraping 

These scripts are meant for archiving webpages. Please, avoid illegal use, e.g. downloads.

To create a venv environment the easiest and most popular way:
```
python -m venv venv
source new_env/bin/activate  # On Windows, use:
venv\Scripts\activate
```


### Use cases:

- as a base for automating screenshoting several websites
- as a script to screenshot several pages 
- to document webpages as JPG or PDF files

### Disclaimer
I can surely guarantee it works with
- urllib3 version 1.26.7
- selenium version 3.141.0
- Chrome browser on Windows

#### Prerequistites:

```
pip install urllib3==1.26.7
pip install selenium=3.141.0 


```
##### Only if about to upgrade to use newer features (mind that this will possibly break existing code.)

```
pip install --upgrade selenium
pip install --upgrade urllib3
```

#### Sources: 
1. [The official Selenium website](https://www.selenium.dev/downloads/)
<br>
2. [PyPi Selenium](https://pypi.org/project/selenium/)