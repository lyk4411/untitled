
from selenium import webdriver#导入库


browser = webdriver.Firefox()
url = 'https://www.zhihu.com/explore'
browser.get(url)

# print(browser.page_source)

input = browser.find_element_by_class_name('AppHeader-inner')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
print(input.text)

