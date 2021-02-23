import scrapy
from scrapy_amazon.items import ScrapyAmazonItem

class AmazonCrawlerSpider(scrapy.Spider):
    name = 'amazon_crawler'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/Xbox-Wireless-Controller-Robot-White/dp/B08K3GW17S/?_encoding=UTF8&pd_rd_w=DlLZO&pf_rd_p=25041c4e-bc5b-4063-99b1-635043c8cad4&pf_rd_r=EGT7674ZAC3X6Q1D4Q1F&pd_rd_r=9ca7fe64-a538-40ea-b01b-b025d0b89fa7&pd_rd_wg=62JmG&ref_=pd_gw_ci_mcx_mr_hp_d']

    def parse(self, response):
        items = ScrapyAmazonItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        image_url = response.xpath('//img[@id="landingImage"]/@src').extract()
        price = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()
     
        discount = discount = response.xpath('//*[@class="a-span12 a-color-price a-size-base priceBlockSavingsString"]/text()').extract()
        
        items['product_name'] = ''.join(title).strip()
        items['image_url'] = ''.join(image_url).strip()
        items['price'] = ''.join(price).strip()
        items['discount'] = ''.join(discount).strip()
        yield items
        
       
        

   