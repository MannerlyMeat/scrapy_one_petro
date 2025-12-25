import scrapy


class OnepetroSearchQuerySpider(scrapy.Spider):
    name = "onepetro_search_query"
    allowed_domains = ["onepetro.org", "httpbin.io"]
    start_urls = ["https://onepetro.org/search-results?page=1&q=Laser%20Deep%20Tunneling"]
    # start_urls = ['https://httpbin.io/user-agent']

    def parse(self, response):
        # self.log(f'Response: {response.body}')
        print(response.body)
        # return response.body
        pass
        # pass
