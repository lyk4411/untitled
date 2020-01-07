import time
from selenium import webdriver#导入库

browser = webdriver.Firefox()
browser.get('https://baidu.com')  # 在当前浏览器中访问百度
browser.execute_script('window.open()')
# handles = browser.window_handles  # 获取当前窗口句柄集合（列表类型）

browser.switch_to_window(browser.window_handles[1])
browser.get('https://taobao.com')
time.sleep(2)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')  # 在当前浏览器中访问百度
    #browser.switch_to_window(handles[0]) #跳到第二个窗口