import scrapy


class FaqSpider(scrapy.Spider):
    name = "faq"
    allowed_domains = ["www.crawfordsville.net"]
    start_urls = ["https://www.crawfordsville.net/egov/apps/faq/list.egov?view=browse&page=1&eGov_searchAny=&eGov_searchType=37&eGov_searchDepartment=&eGov_searchCategory=&eGov_searchTopic=&eGov_searchSubmit=Search"]

    def parse(self, response):
        faqs = response.css('.eGov_faqItem')
        for faq in faqs :
            category = response.css('.eGov_formFieldValue::text').extract_first()
            question = faq.xpath("div[@class='eGov_faqQuestion']/text()").extract_first().strip()
            answer = faq.xpath("div[@class='eGov_faqAnswer']/text()").extract_first().strip()

            # Everything in the yield section does not need to be touched.
            yield {
                '*Category' : category,
                '*Question' : question,
                '*Answer' : answer,
            }