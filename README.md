# Youtube Links Title Checker
A Python script for checking the titles of each links in a text file and logging it in another file :)
<br></br>

_it may not be useful for you but for me it was a good help_

---------------------------------

## Features
- Using [Selenium](https://selenium-python.readthedocs.io/) for scraping the titles of the links
- Using [typer](https://typer.tiangolo.com/) and [questionary](https://questionary.readthedocs.io/en/stable/) for CLI
- You can choose between `headless` and `normal` mode for browser behaviour
- Creates a new file with the date for name to log the results
- You can easily give it any file that contains several links that are unknown to you

---------------------------------

## Requirements
- `Python 3.7+`
- `typer`
- `questionary`
- `selenium`
  
```bash
$ pip install -r requirements.txt
```

---------------------------------

## Usage

**Copy the script and your batch links file to the same folder like this:**
```bash
$ ls
title_checker.py
playlist.txt
```
**and run it with this command:**
```bash
$ python3 title_checker.py
```

<br></br>
### Any contribution is welcomed! 🤞