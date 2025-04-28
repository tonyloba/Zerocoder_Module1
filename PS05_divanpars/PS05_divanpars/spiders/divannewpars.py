import scrapy


class DivannewparsSpider(scrapy.Spider):
    """
    scrapy startproject divanpars
    cd [путь] scrapy genspider divannewpars divan.ru
    pip install ipython
    scrapy shell
    fetch(’ссылка’) — используется, чтобы загрузить веб-страницу. После использования покажется статус-код;
    cd [путь] scrapy crawl divannewpars
    """
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]
    def parse(self, response):
        svets = response.css('div._Ud0k')
        for svet in svets:
            yield {
                'name': svet.css('div.lsooF span::text').get(),
                'price': svet.css('div.pY3d2 span::text').get(),
                'link': svet.css('a::attr(href)').get()

            }
