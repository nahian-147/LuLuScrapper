import scrapy
import json

class CategorySpider(scrapy.Spider):
    name = 'categorySpider'

    start_urls = [
        'https://www.luluhypermarket.com/en-ae/'
    ]

    def parse(self, response):

        for item in response.selector.xpath('/html/body/main/main/header/section[2]/nav/div/div[1]/div[2]/div/ul/*/a/text()').getall():
            yield{
                'name' : item,
            }

class BirdSpider(scrapy.Spider):
    name = 'birdSpider'

    start_urls = [
        'https://www.luluhypermarket.com/en-ae/electronics'
    ]

    def parse(self, response):

        for item in response.xpath('/html/body/main/main/section[3]/section[3]/div/div[2]/div/*/a').getall():
            subcategoryElements = item.split("\"")
            yield{
                'name' : subcategoryElements[7],
                'url' : 'https://www.luluhypermarket.com/en-ae/electronics' + subcategoryElements[1]
            }

class SmallSpider(scrapy.Spider):
    name = 'smallSpider'

    start_urls = []
    
    def __init__(self):
        subcategories = json.load(open('birdSpider.json'))

        for subcategory in subcategories:
            self.start_urls.append(subcategory['url'])

    def parse(self, response):

        for item in response.selector.xpath('//*[@id="moreLoadedProducts"]/*/div'):
            yield{
                'url' : "https://www.luluhypermarket.com/en-ae/electronics/c/HY00214806" + item.attrib['data-url'],
            }

class BigSpider(scrapy.Spider):
    name = 'bigSpider'

    start_urls = []

    def __init__(self):
        products = json.load(open('smallSpider.json'))

        for product in products:
            self.start_urls.append(product['url'])

    def parse(self, response):

        price = 'AED '

        if response.css('span[class="item price"]').css('span::text').get() not in [None, '\n']:
            price += response.css('span[class="item price"]').css('span::text').get()
        else:
            price += response.css('div[class= "current-price"]::text').get()
        yield{
            'title' : response.css('h1[class= "product-name"]::text').get().strip(),
            'price' : price,
            'productSummary' : [item.get() for item in response.css('div[class="description-block mb-3 mt-md-0"]').css('li::text')]
        }