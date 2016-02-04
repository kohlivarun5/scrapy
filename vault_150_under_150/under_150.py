import scrapy
import urlparse

class FirmItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    page = scrapy.Field()
    url = scrapy.Field()
    size = scrapy.Field()

class VaultSpider(scrapy.Spider):
    name = 'vault'
    allowed_domains = ["vault.com"]
    start_urls = [
        "http://www.vault.com/company-rankings/law/best-small-and-mid-size-firms-to-work-for/"
    ]

    def parse(self, response):
      divs = response.xpath('//tr')
      items = []

      count = 0

      for div in divs:
        count+=1
        if count == 1:
          continue

        item = FirmItem()
        item["name"] = div.xpath('td[1]/a/text()').extract()[0]
        item["location"] = div.xpath('td[2]/text()').extract()[0].strip()

        full_url = urlparse.urljoin(response.url, div.xpath('td[1]/a/@href').extract()[0])
        item['page'] = full_url
        
        items.append(item)

        yield scrapy.Request(full_url, callback=(lambda response,val=item: self.parse_firm_page(response, val)))



    def parse_firm_page(self, response,item):

        try:
            item['url'] = response.xpath('//div[@id="ContentPlaceHolderDefault_SectionContent_EntityTabInfo_RightDivInfo"]/div[2]/p/a/@href').extract()[0]

            for stats in response.xpath('//div[@id="ContentPlaceHolderDefault_SectionContent_EntityTabInfo_RightDivInfo"]/ul/li'):
                
                stat_text = stats.xpath('text()').extract()[0]

                if 'Total' in stat_text:
                    item['size'] = stat_text.split()[-1]
        except:
            pass


        yield item


#import scrapy
#
#class DmozSpider(scrapy.Spider):
#    name = "dmoz"
#    allowed_domains = ["vault.com"]
#    start_urls = [
#        "http://www.vault.com/company-rankings/law/best-small-and-mid-size-firms-to-work-for/",
#    ]
#
#    def parse(self, response):
#      divs = response.xpath('//tr')
#      items = []
#
#      count = 0
#
#      for div in divs:
#        count+=1
#        if count == 1:
#          continue
#
#        item = TestBotItem()
#        item['name'] = div.select('./td/a/text()').extract()
#
#        items.append(item)
#        return items
