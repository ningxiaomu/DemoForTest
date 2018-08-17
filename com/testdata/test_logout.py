#coding:utf-8
import unittest
from com.common.base import Base
from com.common.logger import Log
from com.common.login import Login
from selenium import webdriver
from com.page.pageelement.pages import *

class Test(unittest.TestCase):
    u'''测试登出'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login=Login(cls.driver)
        cls.base=Base(cls.driver)
        cls.log=Log()

    def testName(self):
        self.log.info('-----登录开始-----')
        self.login.login_console()
        result=self.base.is_title("测试物业智慧停车管理平台")
        self.log.info(u'登录结果:%s' % result)
        self.base.click(Level_1.点击账户信息)
        self.base.click(Level_1.账户信息_退出)
        self.base.click(Level_1.账户信息_退出_确定)
        title=self.base.is_title("喜泊客智慧停车管理平台 登录")
        self.assertTrue(title)
        self.log.info(u'退出结果:%s' % result)
        self.log.info('-----退出结束-----')
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()