import time
from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('https://www.jd.com/')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("123")')
# browser.close()
#
#
#
# print("=================================================")
bro = webdriver.Firefox()

bro.get('https://www.taobao.com')

#节点定位 find系列的方法
input_text = bro.find_element_by_id('q')
#节点交互
input_text.send_keys('苹果')
time.sleep(2)

#执行js程序(js注入)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)

btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

time.sleep(3)
bro.quit()