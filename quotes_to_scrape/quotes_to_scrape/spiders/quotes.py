# -*- coding: utf-8 -*-
import scrapy
from  scrapy_splash import  SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']
    quote_data = []
    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        
        for quote in quotes:
            q_text = quote.xpath('.//*[@class="text"]/text()').get()
            author = quote.xpath('.//*[@itemprop="author"]/text()').get()
            print(author)
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').get()
            self.quote_data.append({'Quote': q_text, 'Author':author,'Tags':tags} )
            
        yield {'all_quotes':self.quote_data}
        

        
        next_page = response.urljoin(response.xpath('//li[@class="next"]/a/@href').get())
        
        if next_page:
            print(next_page)
            yield scrapy.Request(next_page)
        