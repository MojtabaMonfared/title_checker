#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
import typer
import questionary

app = typer.Typer()


# Typer about command handler
@app.command('about')
def about():
    typer.echo(
        typer.style("""
                    
                Created by Mojtaba Monfared
                https://github.com/MojtabaMonfared/title_checker
                    
                    """, fg=typer.colors.CYAN)
        )

# Typer start command handler
@app.command('start')
def start():
    typer.echo(
        typer.style("Starting TitleChecker", fg=typer.colors.GREEN)
        )

    # get the links list
    input_file = questionary.select("Enter the path to the text file: ", choices=os.listdir(os.getcwd())).ask() 


    # Pass the info for main function to start
    checker(
        input_file=input_file,
    )

# Main function
def checker(input_file):
    
    # choose between chrome behavior
    operation_type = questionary.select("Choose Chrome behavior", choices=[
                    "Headless - It won't show the browser but maybe some titles will be missing",
                    'Normal - Show the browser and you may be able to prevent errors such as "before you continue..."',
            ]).ask()
    if 'Headless' in operation_type: # this will prevent the browser to show up
            options = Options()
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
        
    with open(input_file) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        a = 0
        with typer.progressbar(lines, label="Checking titles") as bar:
            for line in bar:
                driver.get(line)
                
                # wait a bit for the page to load and the title to be visible
                # use this time to accept youtube's tems and conditions otherwise it will not get the correct title
                time.sleep(3)
                
                title = driver.title
                
                # result file name format
                result_file_name = questionary.select('\nHow do you want to name result text file:', choices=[
                        '1. Date and Time as the name',
                        '2. Simple result name with a number'
                    ]).ask()
                
                if '1' in result_file_name:
                    date_format = "%Y-%m-%d (Result)"
                    name = datetime.datetime.now().strftime(date_format)
                else:
                    name = "result - (%s)" % a
                with open(name, 'a+') as result:
                    a += 1
                    result.write("%s:   %s - %s\n" % (a, title, line))
                    time.sleep(0.01)
        typer.echo(
            typer.style(f"Added total {a} urls", fg=typer.colors.GREEN)
        )
    driver.quit() # Quit the driver

if __name__ == "__main__":
    app()