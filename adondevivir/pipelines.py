# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import string

class ValidatorPipeline(object):
    authors = ['Douglas Adams']
    tags = ['life']
    printable = set(string.printable)

    def process_item(self, item, spider):
        if item['author'] in self.authors or set(self.tags) < set(item['tags']):
            item['text'] = filter(lambda x: x in self.printable, item['text'])
            return item
        raise DropItem("wrong author for item %s" % item)
