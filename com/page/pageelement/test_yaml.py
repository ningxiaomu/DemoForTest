#coding:utf-8
from com.page.pageelement.pages import *
from com.common.base import Base

from selenium import webdriver

driver=webdriver.Firefox()

#driver.get('https://www.baidu.com/')

a=Base(driver)
a.open('https://www.baidu.com/')
a.sendkeys(Level_2.百度搜索框, '11111111111111')


