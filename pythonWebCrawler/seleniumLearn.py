from selenium import webdriver#导入库
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
# 如果firefox没有安装在默认位置，就要手动指定位置
# location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox()

# 请求页面
driver.get('http://www.baidu.com')
input = driver.find_element_by_id('kw')
input.send_keys('Python')
input.send_keys(Keys.ENTER)
# wait = WebDriver(driver)
# wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
print(driver.current_url)
# print(driver.get_cookie())
print(driver.page_source)
print(driver.title)
driver.quit()