import scrapy


class StaffSpider(scrapy.Spider):
    name = "staff"
    allowed_domains = ["www.crawfordsville.net"]
    start_urls = ["https://www.crawfordsville.net/"]

    def parse(self, response):
        pass
