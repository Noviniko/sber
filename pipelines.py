# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class SberPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        item['name'] = item['name'].strip()
        item['price'] = int(item['price'].strip().replace(' ', ''))
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item



