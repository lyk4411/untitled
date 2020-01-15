import sys

from scrapy.utils.project import get_project_settings
# from scrapyuniversal.spiders.universal import UniversalSpider
# from scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess

from os.path import realpath, dirname
import json

def get_config(name):
    path = dirname(realpath(__file__)) + '\\scrapyuniversal\\configs\\' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())

def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()
