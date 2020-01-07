#导入动作链对应的模块
from selenium import webdriver#导入库
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
bro = webdriver.Firefox()

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果定位的节点是被包含在iframes节点之中的，则必须使用switch_to进行frame的切换
bro.switch_to.frame('iframeResult')

div_tag = bro.find_element_by_id('draggable')

#实例化一个动作链对象(需要将浏览器对象作为参数传递给该对象的构造方法)
action = ActionChains(bro)
#单击且长按
action.click_and_hold(div_tag)

for i in range(5):
    #让div向右移动
    action.move_by_offset(17,0).perform()
    #perform()立即执行动作链
    time.sleep(0.5)

time.sleep(2)
bro.quit()