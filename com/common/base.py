#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time,os
class Base():
    '''二次封装'''
    def __init__(self,driver):
        #self.driver=webdriver.Firefox()
        self.driver=driver
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(20)
        self.driver.implicitly_wait(20)
        self.timeout=20
    def open(self,url):
        u'''打开网站'''
        self.driver.get(url)
#     def find_element(self,loctor):
#         u'''查找元素,loctor可传元祖,比如('id','kw')'''
#         ele=WebDriverWait(self.driver,self.timeout,1).until(EC.presence_of_element_located(loctor))
#         return ele
    def find_element(self, locator):
       
        if "timeout" in locator:
            timeout = int(locator["timeout"])   # 转int
        else:
            timeout = 30
        if "name" in locator:
            print("正在定位元素名称\"%s\"" %locator['name']+",定位方法: %s-->%s"% (locator['by'], locator['value']))

        if locator["by"] == "id":
            value = locator["value"]
            element =  WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_id(value))
        elif locator["by"] == "xpath":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_xpath(value))
        elif locator["by"] == "name":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_name(value))
        elif locator["by"] == "class":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_class_name(value))
        elif locator["by"] == "tag":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_tag_name(value))
        elif locator["by"] == "link":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_link_text(value))
        elif locator["by"] == "partial_link":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_partial_link_text(value))
        elif locator["by"] == "css":
            value = locator["value"]
            element = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element_by_css_selector(value))
        else:
            loc = (locator["by"], locator["value"])  # 元祖
            element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(loc))
        return element
#     def find_elements(self,loctor):
#         u'''查找元素,loctor可传元祖,只不过查找多个元素'''
#         eles=WebDriverWait(self.driver,self.timeout,1).until(EC.presence_of_all_elements_located(loctor))
#         return eles
    def find_elements(self, locator):
       
        if "timeout" in locator:
            timeout = int(locator["timeout"])   # 转int
        else:
            timeout = 30
        if "name" in locator:
            print("正在定位元素名称\"%s\"" %locator['name']+",定位方法: %s-->%s"% (locator['by'], locator['value']))

        if locator["by"] == "id":
            value = locator["value"]
            elements =  WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_id(value))
        elif locator["by"] == "xpath":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_xpath(value))
        elif locator["by"] == "name":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_name(value))
        elif locator["by"] == "class":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_class_name(value))
        elif locator["by"] == "tag":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_tag_name(value))
        elif locator["by"] == "link":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_link_text(value))
        elif locator["by"] == "partial_link":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_partial_link_text(value))
        elif locator["by"] == "css":
            value = locator["value"]
            elements = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_elements_by_css_selector(value))
        else:
            loc = (locator["by"], locator["value"])  # 元祖
            elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_all_elements_located(loc))
        return elements
    
    
    def click(self,loctor):
        u'''点击操作'''
        ele=self.find_element(loctor)
        ele.click()
    def clear(self,loctor):
        u'''清除操作'''
        ele=self.find_element(loctor)
        ele.clear()
    def sendkeys(self,loctor,text):
        u'''输入文本框操作'''
        ele=self.find_element(loctor)
        ele.send_keys(text)
    def is_text_in_ele(self,loctor,text,timeout=20):
        u'''判断元素里是否包含text,没有则返回False'''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(loctor,text))
            return result
        except:
            return False
    def is_value_in_ele(self,loctor,value,timeout=20):
        u'''判断元素的value值，没有则返回False'''
        try:
            result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(loctor,value))
            return result
        except:
            return False
    def is_title(self,title):
        u'''判断title完全等于,不等于则返回False'''
        try:
            result=WebDriverWait(self.driver,self.timeout,1).until(EC.title_is(title))
            return result
        except:
            return False
    def is_title_contains(self,title):
        u'''判断title里面是否包含,没有则返回False'''
        try:
            result=WebDriverWait(self.driver,self.timeout,1).until(EC.title_contains(title))
            return result
        except:
            return False
    def is_selected(self,loctor):
        u'''判断元素是否被选中,返回的是布尔值'''
        result=WebDriverWait(self.driver,self.timeout,1).until(EC.element_located_to_be_selected(loctor))
        return result
    def is_selected_be(self,loctor,select=True):
        u'''判断元素的状态,selected是期望的参数True/False,返回布尔值'''
        result =WebDriverWait(self.driver,self.timeout,1).until(EC.element_located_selection_state_to_be(loctor,select))
        return result
    def is_alert_present(self):
        u'''判断是否有弹窗,有则返回alert'''
        alert=WebDriverWait(self.driver,self.timeout,1).until(EC.alert_is_present())
        return alert
    def is_visibility(self,loctor):
        u'''判断元素可见,可见返回本身,不可见返回False'''
        result=WebDriverWait(self.driver,self.timeout,1).until(EC.visibility_of_element_located(loctor))
        return result
    def is_invisibility(self,loctor):
        u'''判断元素不可见,不可见返回本身,可见返回False'''
        result=WebDriverWait(self.driver,self.timeout,1).until(EC.invisibility_of_element_located(loctor))
        return result
    def is_clickable(self,loctor):
        u'''判断元素是否可悲点击,不可点击返回False'''
        result=WebDriverWait(self.driver,self.timeout,1).until(EC.element_to_be_clickable(loctor))
        return result
    def is_iframe(self,loctor):
        u'''判断iframe,有就切进去'''
        result=WebDriverWait(self.driver,self.timeout,1).until(EC.frame_to_be_available_and_switch_to_it(loctor))
        return result
    def move_to_element(self,loctor):
        u'''鼠标悬停操作'''
        ele=self.find_element(loctor)
        ActionChains(self.driver).move_to_element(ele).perform()
    def get_text(self,loctor):
        u'''获取文本'''
        t=self.find_element(loctor)
        return t.text
    def get_attribute(self,loctor,name):
        u'''获取元素属性'''
        ele=self.find_element(loctor)
        return ele.get_attribute(name)
    def js_execute(self,js):
        u'''执行js'''
        return self.driver.execute_script(js)
    def is_focus_element(self,locator):
        u'''元素聚焦'''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
    def is_scroll_end(self):
        u'''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
    def select_by_index(self,loctor,index=0):
        u'''通过索引选择，默认从0开始'''
        ele=self.find_element(loctor)
        Select(ele).select_by_index(index)
        #ele.click()
    def select_by_value(self,loctor,value):
        u'''通过value属性选择'''
        ele=self.find_element(loctor)
        Select(ele).select_by_value(value)
    def select_by_text(self,loctor,text):
        u'''通过文本定位'''
        ele=self.find_element(loctor)
        Select(ele).select_by_visible_text(text)
    def deselect_all(self,loctor):
        u'''清除所有选择的类容'''
        ele=self.find_element(loctor)
        Select(ele).deselect_all()
    def deselect_by_index(self,loctor,index):
        u'''通过索引来取消选择'''
        ele=self.find_element(loctor)
        Select(ele).deselect_by_index(index)
    def deselect_by_value(self,loctor,value):
        u'''通过value取消选择'''
        ele=self.find_element(loctor)
        Select(ele).deselect_by_value(value)
    def get_current_handle(self):
        u'''获取当前窗口'''
        return self.driver.current_window_handle
    def get_all_handles(self):
        u'''获取所有窗口'''
        time.sleep(1)
        h=self.driver.window_handles
        if len(h)<=1:
            print('当前只有1个窗口，等待2s后重新获取')
            time.sleep(2)
            h=self.driver.window_handles
        return h
    def get_screenhost(self,image_path):
        u'''截图'''
        now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
        try:
            filepath=os.path.join(image_path,now_time+'.png')
            self.driver.get_screenshot_as_file(filepath)
        except Exception as msg:
            print('截图时发生错误:%s' % msg)
    def switch_window(self,window_name):
        u'''切换窗口'''
        self.driver.switch_to_window(window_name)
    def switch_alert(self):
        alert=self.is_alert_present()
        if alert is not False:
            return alert
        else:
            print('not found alert')
    def switch_iframe(self,loctor):
        return self.is_iframe(loctor)    
    
if __name__=='__main__':
    url='https://www.baidu.com/'
    driver=webdriver.Firefox()
    A=Base(driver)
    A.open(url)
    loc=['id','su']  #百度一下
    loc1=['id','kw'] #搜索框,
    loctor=('xpath',".//*[@id='u1']/a[1]")
    A.sendkeys(loc1, '111')
    A.click(loc)
    print('点击成功')
#     b=A.get_text(loctor)
#     print(b)
    
    