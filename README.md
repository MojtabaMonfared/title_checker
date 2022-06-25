# Youtube Links Title Checker 🔎

A Python script for checking the titles of each links in a text file and logging it in another file :)

_it may not be useful for you but for me it was a good help_ 💡

---------------------------------

## 🔹Features

- Using [Selenium](https://selenium-python.readthedocs.io/) for scraping the titles of the links
- Using [typer](https://typer.tiangolo.com/) and [questionary](https://questionary.readthedocs.io/en/stable/) for CLI
- You can choose between `headless` and `normal` mode for browser behaviour
- Creates a new file with the date for name to log the results
- You can easily give it any file that contains several links that are unknown to you

## 🔹Installation

```bash
pip install --upgrade title_checker
```

## 🔹Usage

- **CLI:**

    ```bash
     title_checker start
    ```

- **In your python script:**

    ```python
    from title_checker.title_checker import checker
    checker('PATH_TO_YOUR_URL_LIST')
    ```

-------------------

### Any contribution is welcomed! 🤞
