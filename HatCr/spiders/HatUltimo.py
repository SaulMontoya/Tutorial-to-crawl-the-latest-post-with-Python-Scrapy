# -*- coding: utf-8 -*-
import scrapy

from HatCr.items import HatariItem

class HatSpider(scrapy.Spider):
    name = "HatUltimo"
    allowed_domains = ["gidahatari.com"]
    start_urls = (
        'http://www.gidahatari.com/ih-es',
    )

    def parse(self, response):
        for sel in response.xpath('(//article)[1]'):
            item = HatariItem()
            item['title'] = sel.xpath('h1/a/text()').extract()
            item['link'] = sel.xpath('h1/a/@href').extract()
            item['desc'] = sel.xpath('div[@class="entry-content"]/p/text()').extract()
            yield item


