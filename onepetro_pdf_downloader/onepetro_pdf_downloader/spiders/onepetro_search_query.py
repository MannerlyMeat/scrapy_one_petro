import scrapy


class OnepetroSearchQuerySpider(scrapy.Spider):
    name = "onepetro_search_query"
    allowed_domains = ["onepetro.org", "httpbin.io", "tls.browserleaks.com", "browserleaks.com"]
    start_urls = ["https://onepetro.org/search-results?page=1&q=Laser%20Deep%20Tunneling"]
    # start_urls = ['https://httpbin.io/user-agent']


    def start_requests(self):
        for _ in range(5):
            yield scrapy.Request(
                "https://onepetro.org/search-results?page=1&q=Laser%20Deep%20Tunneling",
                dont_filter=True,
                meta={
                    "impersonate": "chrome119",
                    "impersonate_args": {
                        "verify": False,
                        "timeout": 10,
                    },
                }
            )
        # return super().start_requests()


    def parse(self, response):

        yield response.body
