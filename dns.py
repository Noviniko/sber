# -*- coding: utf-8 -*-
import scrapy
from sber.sber.items import SberItem


class dnsEkbSpider(scrapy.Spider):
    name = 'dnsEkb'
    allowed_domains = ['dns-shop.ru']

    def __init__(self, custom_input=None, *args, **kwargs):
        super(dnsEkbSpider, self).__init__(*args, **kwargs)
        self.custom_input = custom_input

    def start_requests(self):
        params = {'q': str(self.custom_input)}
        yield scrapy.FormRequest(url="https://www.dns-shop.ru/search/", method='GET', formdata=params,
                                 callback=self.parse)

    def parse(self, response):
        for thing in response.xpath('//div[@class="product has-avails"]'):
            item = SberItem()
            item['name'] = thing.xpath('div[@class="product-info"]/div[@class="title"]/a/h3/text()').extract_first()
            item['price'] = thing.xpath('div[@class="product-price"]/div[@class="price"]/div[@class="price_g"]'
                                        '/span/text()').extract_first()
            yield item








