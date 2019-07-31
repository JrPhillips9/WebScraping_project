from scrapy import Spider, Request
from crms.items import CrmsItem
import re

class CrmsSpider(Spider):
    name = 'crms_spider'
    allowed_domains = ['www.g2.com']
    start_urls = ['https://www.g2.com/categories/crm?order=g2_score#product-list']

    def parse(self, response):
        total = int(response.xpath('//div[@class="ws-nw"]/strong/text()').extract_first())
        per_page = len(response.xpath('//div[@class="paper pt-half pb-0 my-1"]'))
        total_pages = total // per_page + 1
        
        # List comprehension to construct all the urls
        result_urls = ['https://www.g2.com/categories/crm?order=g2_score&page={}#product-list'.format(x) for x in range(1,total_pages+1)]
        
        # Yield the requests to different search result urls, 
        # using parse_result_page function to parse the response.
        for url in result_urls:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):
        # We are looking for url of the detail page.
        detail_urls = response.xpath('//div[@class="product-listing__title"]/div/div/a[1]/@href').extract()

        # Yield the requests to the details pages, 
        # using parse_detail_page function to parse the response.

        for url in detail_urls:
            yield Request(url='https://www.g2.com' + url, callback=self.parse_detail_page)



    # another method

    def parse_detail_page(self, response):

        CRM = response.xpath('//h4[@class="font-weight-bold color-dark-blue word-wrap-word"]/text()').extract()
        Description = response.xpath('//p[@itemprop="description"]/text()').extract()
        OverallRating = response.xpath('//div[@class="mr-4th border px-4th color-primary font-weight-bold border-radius--low bg-white h6"]/text()').extract()
        TotalReviewCount = response.xpath('//div[@class="as-fe"]/text()').extract()
        Review = response.xpath('//h3[@class="review-list-heading m-0 mb-half word-break-word"]/text()').extract() 
        Stars = response.xpath('//span[@itemprop="reviewRating"]/meta[3]/@content').extract()
        Date = response.xpath('//div[@class="time-stamp text-small pl-4th ws-nw"]/span/time/text()').extract()

        

        
        item = CrmsItem()
        item['CRM'] = CRM
        item['Description'] = Description
        item['OverallRating'] = OverallRating
        item['TotalReviewCount'] = TotalReviewCount
        item['Review'] = Review
        item['Stars'] = Stars
        item['Date'] = Date


        yield item    
