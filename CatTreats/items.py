# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CattreatsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# Data items used in containing the scraped data. 
class CatTreatItem(scrapy.Item):
    product_name = scrapy.Field()
    price_usd = scrapy.Field()
    brand_name = scrapy.Field()
    ratings = scrapy.Field()
    product_labels = scrapy.Field()
    ingredient_formula = scrapy.Field()