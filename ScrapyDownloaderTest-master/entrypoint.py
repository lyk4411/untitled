from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'httpbin'])


print("===============================================================================================")
cmdline.execute(['scrapy', 'runspider', 'scrapydownloadertest/spiders/httpbin.py'])