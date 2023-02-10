from os import system

def main():
    system("scrapy crawl categorySpider -o categorySpider.json")
    system("scrapy crawl birdSpider -o birdSpider.json")
    system("scrapy crawl smallSpider -o smallSpider.json")
    system("scrapy crawl bigSpider -o bigSpider.json")


if __name__ == '__main__':
    main()