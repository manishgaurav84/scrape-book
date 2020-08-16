import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['bangalore.craigslist.org']
    start_urls = ['http://bangalore.craigslist.org/search/jjj?']

    def parse(self, response):
        pass
        