import scrapy
from scrapy_splash import SplashRequest 

class CarsByYearMakeSpider(scrapy.Spider):
    name = 'cars_by_year_make'
    allowed_domains = ['baierl.com']
    start_urls = ['http://www.baierl.com/new-inventory/']

    def start_requests(self):
        filter_scripts
    def parse(self, response):
        
