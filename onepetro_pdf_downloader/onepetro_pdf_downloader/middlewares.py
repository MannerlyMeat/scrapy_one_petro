# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from scrapy.downloadermiddlewares.retry import RetryMiddleware

import time
import random


class OnepetroPdfDownloaderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class OnepetroPdfDownloaderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


# class CloudflareBypass(RetryMiddleware):
#     USER_AGENTS = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#         'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
#     ]

#     def process_response(self, request, response, spider):
#         if response.status in [403, 429, 503] or self.is_cloudflare_challenge(response):
#             time.sleep(5)
#             new_headers = dict(request.headers)
#             new_headers[b'User-Agent'] = random.choice(self.USER_AGENTS).encode()
#             new_headers[b'Accept'] = b'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
#             new_headers[b'Accept-Language'] = b'en-US,en;q=0.9,ru;q=0.8'
#             new_headers[b'Accept-Encoding'] = b'gzip, deflate, br'
#             new_headers[b'Connection'] = b'keep-alive'
            
#             # Создаем новый запрос с обновленными заголовками
#             new_request = request.copy()
#             new_request.headers = new_headers
            
#             # Увеличиваем счетчик попыток
#             retry_times = request.meta.get('retry_times', 0) + 1
#             if retry_times <= self.max_retry_times:
#                 new_request.meta['retry_times'] = retry_times
#                 new_request.dont_filter = True  # Не фильтровать как дубликат
#                 return new_request
            
#         return response
    
#     def is_cloudflare_challenge(self, response):
#         """Определяем, это Cloudflare челлендж или нет"""
#         text = response.body.lower()
#         headers = {k.lower(): v for k, v in response.headers.items()}
        
#         cloudflare_indicators = [
#             'cloudflare',
#             'cf-ray',
#             'challenge',
#             'attention required',
#             'just a moment...'
#         ]
        
#         # Проверка в тексте
#         for indicator in cloudflare_indicators:
#             if indicator in text:
#                 return True
        
#         # Проверка заголовков
#         if any('cf-' in str(k) for k in headers.keys()):
#             return True
            
#         return False


# class CustomHeadersMiddleware:
#     """Middleware для установки кастомных заголовков"""
    
#     def process_request(self, request, spider):
#         # Устанавливаем Referer если его нет
#         if b'Referer' not in request.headers and request.meta.get('previous_url'):
#             request.headers[b'Referer'] = request.meta['previous_url']
        
#         # Добавляем заголовки для обхода WAF
#         if b'Sec-Fetch-Dest' not in request.headers:
#             request.headers[b'Sec-Fetch-Dest'] = b'document'
#             request.headers[b'Sec-Fetch-Mode'] = b'navigate'
#             request.headers[b'Sec-Fetch-Site'] = b'none'
#             request.headers[b'Sec-Fetch-User'] = b'?1'
        
#         # Добавляем случайную задержку между запросами
#         time.sleep(random.uniform(1, 3))