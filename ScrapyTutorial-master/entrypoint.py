from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', 'quotes'])


print("===============================================================================================")
cmdline.execute(['scrapy', 'runspider', 'tutorial/spiders/quotes.py'])
