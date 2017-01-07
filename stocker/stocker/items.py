# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Stock(scrapy.Item):
    symbol = scrapy.Field()
    volume = scrapy.Field()
    value = scrapy.Field()
    last_price = scrapy.Field()
    updated = scrapy.Field()
