# -*- coding: utf-8 -*-
import scrapy
from sber.sber.items import SberItem

class avitoEkbSpider(scrapy.Spider):
    name = 'avitoEkb'
    allowed_domains = ['avito.ru']

    def __init__(self, custom_input=None, *args, **kwargs):
        super(avitoEkbSpider, self).__init__(*args, **kwargs)
        self.custom_input = custom_input

    def start_requests(self):
        params = {
            'user': str(2),
            'q': self.custom_input
        }
        yield scrapy.FormRequest(url="https://www.avito.ru/ekaterinburg", method='GET', formdata=params,
                                 callback=self.parse)

    def parse(self, response):
        for thing in response.xpath('//div[@class="item item_table clearfix js-catalog-item-enum  js-item-extended'
                                    ' item_table_extended snippet-experiment      item_hide-elements"]'):
            item = SberItem()
            item['name'] = thing.xpath('div[@class="description item_table-description\n   snippet-experiment-wrapper"]'
                                       '/div[@class="item_table-header"]'
                                       '/h3[@class="title item-description-title"]/a/text()').extract_first()
            item['price'] = thing.xpath('div[@class="description item_table-description\n   snippet-experiment-wrapper"]'
                                        '/div[@class="item_table-header"]'
                                        '/div[@class="about about_bold-price"]'
                                        '/span[@class="price"]/text()').extract_first()
            yield item




