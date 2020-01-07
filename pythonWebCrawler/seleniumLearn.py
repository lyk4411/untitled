from selenium import webdriver#导入库

# 如果firefox没有安装在默认位置，就要手动指定位置
location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(firefox_binary=location)

# 请求页面
driver.get('http://www.baidu.com')

print (driver.title)
driver.quit()