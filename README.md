# Petco Web Scraping Assessment
Follow the steps to run this Scrapy File. 

## Web-Scraping Strategy: 

The scrapy spider named `cat_treats_spider` is designed to systematically extract information about cat treats from the Petco website. Starting from the URL "https://www.petco.com/shop/en/petcostore/category/cat/cat-treats," the spider employs a pagination mechanism with a page counter `self.page_number` initially set to `1`. The parsing logic involves extracting product links from the current page using XPath, specifically targeting the `product-list__Wrapper` and `ProductTile-styled__ProductCard` elements.

For each product link, the spider constructs the absolute URL and follows it to gather more detailed information. This involves calling the `parse_required_details` method, which is responsible for extracting product details such as name, price in USD, brand name, ratings, product labels, and ingredient formula. The information is structured using the `CatTreatItem` class.

To handle pagination, the spider increments the page counter and constructs the URL for the next page, subsequently calling the `parse` method recursively. The spider continues this process until the specified page limit is reached, as controlled by the conditional check `self.page_number <= 2`. The overall strategy ensures systematic and comprehensive scraping of cat treats data from multiple pages, and the extracted information is outputted as structured data items. These items are then formatted and saved in CSV, JSON formats, and in MySQL database for further processing or storage, providing flexibility in data utilization and analysis.

## Tools and Library Used on this project: 

To this project I used `mysql-connector` to easily connect to my MySQL database and store the scraped data in a specific table. To improve web scraping, I incorporated `scrapeops-scrapy-proxy-sdk` for a rotating proxy, IP, and headers/user-agents, preventing errors during the process of accessing the website. Other tools and libraries are Scrapy provided such as ItemAdapter in `sipelines.py`. I also declare in `settings.py` that the `RETRY_TIMES` should be 10 and `DOWNLOAD_DELAY` should be 2.8 seconds. 

## Challenges faced and how they were solved: 

The first challenge I faced is the was dealing with the website's accessibility problem, consistently throwing a `HTTP Status 403` error that prevented me from reaching the crucial URL for scraping. Despite trying various fixes like custom IP lists to rotate it, raandommized user-agents, and randomized headers, the issue persisted. It was only when I integrated the `scrapeops-scrapy-proxy-sdk` library that things took a turn. This handy tool, acting as a proxy middleware, automated the rotation of IPs, headers, and user-agents. This automation proved to be the key to breaking through the access barrier, allowing me to finally retrieve the desired data from the website.

The second challenge I encountered was closely tied to the initial one, involving the extraction of product links per item. While the spider was running, some links triggered a `HTTP Status 429` response, indicating that I have too many requests made to the web server. Notably, some links that initially faced a 429 status succeeded upon retry, but others continued to failed on retrieval. Upon delving into the details of this status code, I realized the necessity of introducing a time delay between requests to the website's server. To address this, I strategically set the `DOWNLOAD_DELAY` to 2.8 seconds, thereby showing respect to the web server's limitations and ensuring a more reliable and accurate extraction of product links during the scraping process.

The final challenge revolved around extracting product labels, where 10 out of the 96 items failed to provide a valid product label value. This issue stemmed from either non-existent labels or errors, as indicated by the developer tools during inspection. To address this, I devised a solution: if the parsed product label returned `null`, I implemented a fallback strategy by setting it to the default value of `Cat Treats`. This approach ensured a more consistent and complete dataset, mitigating the impact of missing or erroneous product label values on the overall scraping process.

In my settings.py file, I've opted for faster scraping by setting ROBOTSTXT_OBEY to False. However, before making this adjustment, I took a precautionary step by reviewing the "https://www.petco.com/robots.txt" file to understand the allowed rules on the website. This ensures that the systematic process executed by the spider file aligns with the regulations specified by "https://www.petco.com," guaranteeing responsible and non-disruptive scraping that complies with the website's guidelines and avoids any potential harm.


## Instructions on how to run: 
You need Python compiler installed on your system. To install, go to the official Python website page and to the downloads sections 

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

### If you want to debug the errors on requirements.txt, you can run this command: 

`pip install --upgrade pip`










