import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
import typer
import questionary


def main():
    typer.echo(
        typer.style("Starting Youtube title checker", fg=typer.colors.GREEN)
        )
    
    operation_type = questionary.select("Choose Chrome behavior", choices=[
                typer.style("Headless - It won't show the browser but maybe some titles will be missing", fg=typer.colors.YELLOW),
                typer.style('Normal - Show the browser and you may be able to prevent errors such as "before you continue..."', fg=typer.colors.YELLOW),
        ]).ask()
    input_file = questionary.select("Enter the path to the text file: ", choices=os.listdir(os.getcwd())).ask()
    
    if operation_type == 'Headless':
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
        
    date_format = "%Y-%m-%d (Result)"
    with open(input_file) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        a = 0
        with typer.progressbar(lines, label="Checking titles") as bar:
            for line in bar:
                driver.get(line)
                time.sleep(3)
                # wait a bit for the page to load and the title to be visible
                # use this time to accept youtube's tems and conditions otherwise it will not get the correct title
                title = driver.title
                with open('%s' % datetime.datetime.now().strftime(date_format), 'a+') as result:
                    a += 1
                    result.write("%s:   %s - %s\n" % (a, title, line))
                    time.sleep(0.01)
        typer.echo(
            typer.style(f"Added total {a} urls", fg=typer.colors.GREEN)
        )
    driver.quit()

if __name__ == "__main__":
    typer.run(main)