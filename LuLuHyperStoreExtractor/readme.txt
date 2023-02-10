please run the scrape.py file to scrape from the website automatically or manually execute the following in the following order,

0. scrapy crawl categorySpider -o categorySpider.json
1. scrapy crawl birdSpider -o birdSpider.json
2. scrapy crawl smallSpider -o smallSpider.json
3. scrapy crawl bigSpider -o bigSpider.json

categorySpider.json file lists all the CATEGORIES
birdSpider.json file lists the SUBCATEGORIES
smallSpider.json file lists the  INDIVIDUAL PRODUCTS
& bigSpider.json file lists all the DETAIL OF THE PRODUCTS