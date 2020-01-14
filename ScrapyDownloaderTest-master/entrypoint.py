from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', 'httpbin'])
#
#
# print("===============================================================================================")
# cmdline.execute(['scrapy', 'runspider', 'scrapydownloadertest/spiders/httpbin.py'])

spider_list = [['scrapy', 'crawl', 'httpbin'],['scrapy', 'runspider', 'scrapydownloadertest/spiders/httpbin.py']]

for name in spider_list:
    cmdline.execute(name)
    print("===============================================================================================")
