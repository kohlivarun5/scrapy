import scrapy

class FirmItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    website = scrapy.Field()

class StackOverflowSpider(scrapy.Spider):
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
        item["name"] = div.xpath('./td/a/text()').extract()[0]
        item["location"] = div.xpath('./td/text()').extract()[0]
        yield item


#    start_urls = ['http://stackoverflow.com/questions?sort=votes']
#
#    def parse(self, response):
#        for href in response.css('.question-summary h3 a::attr(href)'):
#            full_url = response.urljoin(href.extract())
#            yield scrapy.Request(full_url, callback=self.parse_question)
#
#    #def parse_question(self, response):
#    #    yield {
#    #        'title': response.css('h1 a::text').extract()[0],
#    #        'votes': response.css('.question .vote-count-post::text').extract()[0],
#    #        'body': response.css('.question .post-text').extract()[0],
#    #        'tags': response.css('.question .post-tag::text').extract(),
#    #        'link': response.url,
#    #    }


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
