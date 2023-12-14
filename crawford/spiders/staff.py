import scrapy


class StaffSpider(scrapy.Spider):
    name = "staff"
    allowed_domains = ["www.crawfordsville.net"]
    start_urls = ["https://www.crawfordsville.net/egov/apps/staff/directory.egov?eGov_searchName=&eGov_searchDepartment=&app=6&sect=public&path=browse&act=&id=&page=6_3&order="]

    def parse(self, response):
        rows = response.xpath('//tbody/tr')
        for row in rows :
            name = row.xpath('td/a/text()').extract_first()
            title = row.xpath("td[@class='eGov_DataCell2']/text()").get()
            department = row.xpath("td[@class='eGov_DataCell3']/text()").get()
            email = row.xpath("td[@class='eGov_DataCell4']/a").get()
            phone = row.xpath("td[@class='eGov_DataCell5']/text()").get()
          


            # Everything in the yield section does not need to be touched.
            yield {
                'Name' : name,
                'Title' : title,
                'Department' : department,
                'Email' : email,
                'Phone' : phone,
            }