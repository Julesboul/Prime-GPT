[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
# Prime GPT project (Flask)

This application was made for the Prime Engineering compagny in order to support it recruitement process.

It summarizes a resume in a few lines using ChatGPT's API. There are 2 different abstract formats to choose from.

## Prerequisites

* Install Python 3 : [Download Python 3](https://www.python.org/downloads/)
* Install git : [Download Git](https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git)

## Installation

### 1. Download the project on your local repository : 
```
git clone git@github.com:Julesboul/Prime-GPT.git 
```
### 2. Setup a virtual environment :
* Create the virtual environment: `python -m venv venv`
* Active it:
    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`

    
### 3. Install project dependencies
```
pip install -r requirements.txt
```

### 4. Install Tesseract

Install Tesseract to process pictures : https://tesseract-ocr.github.io/tessdoc/Installation.html

Check that the link to tesseract in "Utils.py" service line 70 is correct.

### 5. Put your ChatGPT's API key

Create a .env file like the .env_template

Put your ChatGPT's API key linked to your Open AI's account in the .env file

## Launch
* Launch the app with the command line : `flask run`

## Tests

* Launch tests with the command line : `pytest`