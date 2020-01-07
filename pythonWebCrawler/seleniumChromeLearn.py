from selenium import webdriver
driver = webdriver.Chrome(r'F:\software\chromedriver_win32')
driver.get('http://www.baidu.com')
print (driver.title)
driver.quit()