# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time,os


class Base():

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

    def find(self, locator):
       
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

    def click(self, locator):
        u'''单个元素点击操作'''
        ele = self.find(locator)
        ele.click()

    def send_text(self, locator, text):
        u'''输入文本'''
        el = self.find(locator)
        el.send_keys(text)

    
if __name__=='__main__':
    url='https://www.baidu.com/'
    driver=webdriver.Firefox()
    A=Base(driver)
    A.open(url)
#     loc=['id','su']  #百度一下
#     loc1=['id','kw'] #搜索框,
    loctor=('xpath',".//*[@id='u1']/a[1]")
    loc={'by':'id','value':'kw'}
    loc1={'by':'id','value':'su'}
    A.send_text(loc, '111')
    A.click(loc1)
    print('点击成功')
   
        
        
    
