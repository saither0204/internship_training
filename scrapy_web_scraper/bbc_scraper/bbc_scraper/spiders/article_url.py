import scrapy


class ArticleUrlSpider(scrapy.Spider):
    name = 'article_url'
    allowed_domains = ['bbc.com']
    start_urls = ['http://bbc.com/']

    def parse(self, response):
        pass
