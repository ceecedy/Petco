import scrapy

# this import is to use the class with data item entities/attributes. 
from CatTreats.items import CatTreatItem

class CatTreatsSpiderSpider(scrapy.Spider):
    name = "cat_treats_spider"
    start_urls = ["https://www.petco.com/shop/en/petcostore/category/cat/cat-treats"]
    page_number = 1 # counter for page 
    
    
    def parse(self, response): 
        # if the x attribute is not 3 then continue the execution. 
        if self.page_number <= 2:
            # the li tag with a specific class "ProductTile-styled__ProductCard-sc-9ac5643b-3 hPvoIK"
            # has the link for broader details about all products. So the first method is to go to that link. 
            items = response.xpath(
                '//ul[@class="product-list__Wrapper-sc-53fb6819-0 ikwtOK"]'
                '//li[@class="ProductTile-styled__ProductCard-sc-9ac5643b-3 hPvoIK"]'
            )
            
            # loop over the items list 
            for item in items: 
                # get the href attribute for every item card 
                href = item.css('a ::attr(href)').get()
                
                # if href is not None
                if href:
                    # join the href link to the domain of the e-commerce site. 
                    relative_link = 'https://www.petco.com' + href
                    # go to the relative link and call the function to scrape for the relative link. 
                    yield response.follow(relative_link, callback = self.parse_required_details)
            
            self.page_number += 1
            next_page_link = f'https://www.petco.com/shop/en/petcostore/category/cat/cat-treats?params=page%3D{self.page_number}'
            yield response.follow(next_page_link, callback = self.parse)
        
    
    # method for scraping the required details in the relative link.
    def parse_required_details(self, response): 
        item = CatTreatItem()
        
        item['product_name'] = response.xpath('//h1[@class="product-name-styled__EllipsisTextContainer-sc-52c6fcb-3 fdkWtY"]/text()').get()
        item['price_usd'] = response.xpath('//div[@class="price-row-styled__PriceRowContainer-sc-da3b5f0a-1 dutiAF"]/text()').get()
        item['brand_name'] = response.xpath('//a[@class="ratings-row-styled__RedesignBrandLink-sc-1e73d82-2 bcTMqX"]/text()').get()
        item['ratings'] = response.xpath('//ul[@class="rating-styled__RatingsList-sc-761ed730-0 gOMNvV"]/@title').get()
        item['product_labels'] = response.xpath('//ul[@data-testid="breadcrumbs"]/li[last()]/a[1]/text()').get()
        item['ingredient_formula'] = response.xpath('//p[@class="ingredients-tab___StyledP-sc-42a41f37-1 jjTncQ"]/text()').get()
        
        yield item
        