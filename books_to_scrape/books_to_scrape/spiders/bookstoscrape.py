import scrapy
from scrapy_splash import SplashRequest


class BookstoscrapeSpider(scrapy.Spider):
    name = 'bookstoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/category/books_1/index.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html')

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        books = response.xpath("//*[@class='product_pod']")
        for book in books:
            title = book.xpath(".//h3/a/@title").get()
            rating = book.xpath(".//p/@class").get().split()[1]
            img_path = response.urljoin(book.xpath(".//div[@class='image_container']/a/img/@src").get())
            price = book.xpath(".//div[@class='product_price']/p[@class='price_color']/text()").get()
            availability = book.xpath(".//div[@class='product_price']/p[@class='instock availability']/text()[2]").get().strip() 
            
            yield {
                'Title':title,
                "Rating":rating,
                'Image URL':img_path,
                'Price':price,
                'Availability':availability
            }
        script = """function main(splash)
                assert(splash:go(splash.args.url))
                splash:wait(0.3)
                button = splash:select("li[class=next] a")
                splash:set_viewport_full()
                splash:wait(0.1)
                button:mouse_click()
                splash:wait(1)
                return {url = splash:url(),
                        html = splash:html()}
            end"""
        print(response.url)
        yield SplashRequest(url=response.url,
                            callback=self.parse,
                            endpoint='execute',
                            args={'lua_source':script},
                            dont_filter=True)

