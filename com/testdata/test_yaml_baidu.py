#coding:utf-8
import unittest
from selenium import webdriver
from com.common.base import Base
from com.page.pageelement.pages import *

class Test01(unittest.TestCase):
    u'''测试百度_yaml'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.base=Base(cls.driver)
       
    def test_01(self):
        self.base.open('https://www.baidu.com/')
        self.base.send_text(Level_2.百度搜索框,'罗')
        self.base.click(Level_2.百度点击)

if __name__=='__main__':
    unittest.main()