```python
import scrapy
from scrapy.http import Request
from bing_search import BingSearch
from nlp_processing import is_relevant_promotion

class PromotionSpider(scrapy.Spider):
    name = 'promotion_spider'
    allowed_domains = ['bing.com']
    start_urls = BingSearch().get_search_results('uk promotions free cash incentives')

    def parse(self, response):
        promotions = response.xpath('//li[@class="b_algo"]')
        for promo in promotions:
            promotion_name = promo.xpath('.//h2/a/text()').get()
            promotion_link = promo.xpath('.//h2/a/@href').get()
            promotion_description = promo.xpath('.//p/text()').get()

            if is_relevant_promotion(promotion_description):
                yield {
                    'promotion_name': promotion_name,
                    'promotion_link': promotion_link,
                    'promotion_description': promotion_description
                }

        next_page = response.xpath('//a[@class="sb_pagN"]/@href').get()
        if next_page:
            yield Request(url=next_page, callback=self.parse)
```
