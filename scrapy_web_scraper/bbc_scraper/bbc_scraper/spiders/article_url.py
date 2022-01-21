import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field
import re
from ..items import BbcArticleItem

class BbcArticleUrlSpider(scrapy.Spider):
    name = 'bbc_article_url'
    allowed_domains = ['www.bbc.com']
    start_urls = ['http://www.bbc.com/']

    def parse(self, response):
        items = BbcArticleItem()
        urls = response.css('.media__link::attr(href)').extract()
        titles = response.css('a.media__link::text').extract()
        
        for url, title in zip(urls,titles):
            items['titles'] = title
            if re.match('^/.*$',url):
                #these are the two methods through which urls can be formed
                #items['urls'] = 'https://www.bbc.com'+url
                items['urls'] = self.start_urls[0]+url
            else:
                items['urls'] = url
            print(" ********************* \n\n\n\n\n\n\n\n\nHERE IS YOUR URL ",items['urls'],"********************* \n\n\n\n\n\n\n\n\n")
            articles = response.css(items['urls'])
            yield items
        # print(" ********************* \n\n\n\n\n\n\n\n\nHERE IS YOUR COUNTER ",c,"********************* \n\n\n\n\n\n\n\n\n")