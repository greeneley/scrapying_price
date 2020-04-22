import scrapy
class fptshop(scrapy.Spider):
    name = 'examplespider1'
    allowed_domains = ['fptshop.com.vn']
    keysearch = input("Key search:")
    start_urls = ['https://fptshop.com.vn/tim-kiem/'+keysearch]

    def parse(self, response):
        self.logger.info('A response from {} just arrived'.format(response.url))
        # self.logger.debug('Nothing wrong in {}'.format(response.url))
        LAPTOP_NAME_SELECTOR = 'h3.fs-icname ::text'
        PRICE_SELECTOR = 'p.fs-icpri ::text'
        for laptop, price in zip(response.css(LAPTOP_NAME_SELECTOR).getall(), response.css(PRICE_SELECTOR).getall()) :
            for r in (("\r", ""), ("\n", ""), (" ",""), ("₫", "VND"), ('"',"")):
                price = price.replace(*r)
            yield {'laptop': laptop, 'price': price}
            pass
        #     yield {'laptop': laptop}

class thegioididong(scrapy.Spider):
    name = 'thegioididong'
    allowed_domains = ['thegioididong.com']
    keysearch = input("Key search:")
    start_urls = ['https://www.thegioididong.com/tim-kiem?key='+keysearch]

    def parse(self, response):
        self.logger.info('A response from {} just arrived'.format(response.url))
        SET_SELECTOR = '.laptop'
        # # PRICE_SELECTOR = 'p.fs-icpri ::text'
        for laptop  in response.css(SET_SELECTOR):
            # yield {'laptop': laptop}
            NAME_SELECTOR = 'h3 ::text'
            PRICE_SELECTOR = 'div.price strong ::text'
            yield {'laptop': laptop.css(NAME_SELECTOR).extract_first(),
            'price': laptop.css(PRICE_SELECTOR).extract_first() }

class xuanvinh(scrapy.Spider):
    name = 'xuanvinh'
    allowed_domains = ['xuanvinh.vn']
    keysearch = input("Key search:")
    start_urls = ['http://xuanvinh.vn/search?cat=0&key='+keysearch]

    def parse(self, response):
        self.logger.info('A response from {} just arrived'.format(response.url))
        SET_SELECTOR = '.product-info'
        # # PRICE_SELECTOR = 'p.fs-icpri ::text'
        for laptop  in response.css(SET_SELECTOR):
            # yield {'laptop': laptop}
            NAME_SELECTOR = 'h3.product-title a::text'
            PRICE_SELECTOR = 'div.product-price p::text'
            yield {'laptop': laptop.css(NAME_SELECTOR).extract_first(),
            'price': laptop.css(PRICE_SELECTOR).extract_first() }

# class xuanvinh(scrapy.Spider):
#     name = 'xuanvinh'
#     allowed_domains = ['phongvu.vn']
#     keysearch = input("Key search:")
#     start_urls = ['https://phongvu.vn/searchpves/'+keysearch]

#     def parse(self, response):
#         self.logger.info('A response from {} just arrived'.format(response.url))
#         PRODUCT_NAME_SELECTOR = '.product-name ::text'

#         # # PRICE_SELECTOR = 'p.fs-icpri ::text'
#         for laptop  in response.css(SET_SELECTOR):
#             NAME_SELECTOR = 'h3.product-title a::text'
#             PRICE_SELECTOR = 'div.product-price p::text'
#             yield {'laptop': laptop.css(NAME_SELECTOR).extract_first(),
#             'price': laptop.css(PRICE_SELECTOR).extract_first() }