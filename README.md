# final-grocery-script

# Credits:

Script for scraping data for the online grocery project at Duke University.

Pages used (included in CSV file):
http://www.publix.com/product-catalog/ (Cookies)

Software Used:
Selenium,http://www.seleniumhq.org/
mySQL, https://www.mysql.com/
SequelPro, https://www.sequelpro.com/
CSVreader, http://opencsv.sourceforge.net/apidocs/com/opencsv/CSVReader.html
Python, https://www.python.org/

# Developer Guide
Database creation: credit to Publix.com
On a high level, we have set up a database using mySQL and SequelPro as a method of storing all of our data. We are utilizing two scripts (written in python) in order to crawl through the web pages.

Details:

# Web scraping:
The web pages we are scraping from are all dynamically generated, meaning their HTML is generated by javascript at runtime (and may change based on user data such as cookies, location etc). As a result, instead of downloading a pure HTML response, which would omit the javascript generated html, we are utilizing an automation software called Selenium to open the webpage in a virtual browser so we are able to access the generated HTML. 

Utilizing a python framework called Scrapy, we will begin our web crawl on the list product category pages (for example, the list of Dairy products). Because Harris teeter and most other robust online grocery stores hide the HREF (the URL that takes you to the next page when you click on an item) on their items publicly (even invisible after downloading javascript generated HTML), we will utilize Selenium to identify and automate click on the individual products (ex. Yoplait yogurt) that exist on the page.

After arriving on the subsequent page, will pass-back the resulting product-page URL link through Scrapy, which we will write to a file. These automated clicks and resulting pass-back of URLs would be performed asynchronously by default (meaning they will not necessarily execute in order and may be performed at the same time) through Scrapy’s protocols, which most web-scrapers use without issue. However, Sydney and I were planning on writing some simple throttling functionality that would create a delay between each click/request and a synchronous ordering, in order to make the program function more similarly to a human-being. This will avoid the program creating too many requests to a given grocery store’s server at once. Scrapy will then utilize a link extractor to follow the category to next page of the pagination (ex. Dairy items, page 2), and repeat the process until there are no more product pages.

Next, we will have a second script through Scrapy that will utilize Selenium to open each product URL that we found. We will then download the HTML for each of the products, and utilize regular expressions and a python formatting extension called BeautifulSoup to parse through the HTML and extract the important information: item name, description, price, nutrition facts, etc. We will then pass these pieces of information to our pipeline to be written to our database. Next, we will utilize Scrapy to visit the hosted-image URL, where we use python extension cStringIO to read the raw unicode string of the image. We will then use cStringIO to convert the unicode to an image, which we will create in a new file and download to the database pipeline.

High level: 
We’re 1) extracting the URLs of all the product pages  and 2) following those urls, downloading the resulting HTML, and parsing the necessary data to save to a database.

# Getting Started
- clone repo
- npm install
- pip install Selenium
- pip install csv

# Configuration Set-up
- On Pycharm, select configuration from left-most drop down menu.
- Select python 2.7 interperter (virtual env)

# Running the Script
- Point the script to a starting page on Publix to begin the webscrawl. All subsequent pages reachable from this page will be inclduded in the scrape. 
- For example, http://www.publix.com/product-catalog/productlisting?ch=9.12.&page=1&count=96 



