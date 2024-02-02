# Petco Web Scraping Assessment
Follow the steps to run this Scrapy File. 

## Pre-Requesite: You should have Python compiler installed on the system which you are going to use. 
To install, go to the official Python website page and to the downloads sections 

`Python Compiler - https://www.python.org/downloads`

## Step 1 - Install your python virtual environment (If you want to run this in venv).
Here are some guides for every Operating System you might use. 

For Mac: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-macos

For Windows: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-windows

For Linux: https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-2-scrapy-environment/#setting-up-your-python-virtual-environment-on-linux

Then to activate it so that any new modules that are installed are installed into this virtual environment:

`source venv/bin/activate`

You can skip the first Step if you don't want to use virtual environment to run this project. 

## Step 2 - Install the required python modules
To install the required modules for this python project to run you need to install the required python modules using the following command:

`pip install -r requirements.txt`

If you encounter issues on running the requirements.txt, you can install the framework and modules used in this project. 

`pip install scrapy`
`pip install mysql-connector-python`
`pip install scrapeops-scrapy-proxy-sdk`

## Step 3 - Add your API key.
You need to register at https://scrapeops.io before you get yout own API key. 
After you register, put your API key in the `SCRAPEOPS_API_KEY = 'your_api'` and it is inside the `settings.py` file of the project. 

## Step 4 - Running the project 
After Scrapy framework and the required library and module is installed, you can now run this project. 

Change directory to the CatTreats:

`cd CatTreats`

Run the spider to start scraping: 

`scrapy crawl cat_treats_spider`

### If you want to debug the errors on requirements.txt, you can run this commands: 

`pip install --upgrade pip`




