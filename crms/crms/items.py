# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrmsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CRM = scrapy.Field()
    Description = scrapy.Field()
    OverallRating = scrapy.Field()
    TotalReviewCount = scrapy.Field()
    Review = scrapy.Field()
    Stars = scrapy.Field()
    Date = scrapy.Field()
   
   
