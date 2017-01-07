# -*- coding: utf-8 -*-
"""
:author: Harold Dennis C Batocael
:contact: hardistones@gmail.com
"""

import scrapy
from datetime import datetime
from stocker.items import Stock


class StocksphSpider(scrapy.Spider):
    name = "stocksph"
    start_urls = ["https://stocksph.com/market-activity"]

    def parse(self, response):
        top_gainers = response.css('.panel-green tbody tr')
        top_losers = response.css('.panel-red tbody tr')
        most_active = response.css('.panel-danger tbody tr')

        for gainer in top_gainers + top_losers + most_active:
            info = gainer.css('td')
            yield Stock({
                'symbol': info[0].css('td a::text').extract_first(),
                'volume': info[1].css('td::text').extract_first(),
                'value': info[2].css('td::text').extract_first(),
                'last_price': info[3].css('td::text').extract_first(),
                'updated': str(datetime.now())
            })
