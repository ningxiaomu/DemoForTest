#coding:utf-8
import unittest
from selenium import webdriver
from com.common.base import Base
from com.common.login import Login
from com.common.logger import Log
from com.common.Level_1_menu import Leftpage1
from com.common.Level_2_menu import Leftpage2
loctor=("xpath",".//*[@id='contentTable']/tbody/tr/td[8]")

class Test(unittest.TestCase):
    u'''测试停车场查询'''
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login=Login(cls.driver)
        cls.level_1=Leftpage1(cls.driver)
        cls.level_2=Leftpage2(cls.driver)
        cls.base=Base(cls.driver)
        cls.log=Log()
    def testName(self):
        self.log.info('-----停车场查询测试开始-----')
        self.login.login_console() #登录
        result=self.base.is_title("测试物业智慧停车管理平台")
        self.log.info(u'登录结果:%s' % result)
        self.level_1.click_pak()
        self.level_2.click_Parking_enquiry()
        self.base.is_iframe('mainFrame')
        self.level_2.click_Statu_button()
        self.level_2.click_Disable()
        self.level_2.click_search_button()
        result=self.base.find_elements(loctor)
        a=[]
        for i in result:
            a.append(i.text)
        b=list(set(a))
        self.log.info('状态显示:%s' % b[0])
        ex='禁用'
        self.assertEqual(ex, b[0], '状态不全是  禁用')
        self.log.info('-----停车场查询测试结束-----')
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()