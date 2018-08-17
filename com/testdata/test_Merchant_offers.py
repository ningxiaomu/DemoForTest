#coding:utf-8
import unittest
from selenium import webdriver
from com.common.Level_1_menu import Leftpage1
from com.common.Level_2_menu import Leftpage2
from com.common.base import Base
from com.common.login import Login
from com.common.logger import Log
loctor=('xpath',".//*[@id='contentTable']/tbody/tr/td[3]")
class Test(unittest.TestCase):
    u'''测试商户优惠'''  
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login=Login(cls.driver)
        cls.level_1=Leftpage1(cls.driver)
        cls.level_2=Leftpage2(cls.driver)
        cls.base=Base(cls.driver)
        cls.log=Log()
    def testName(self):
        self.log.info('-----商户优惠测试开始-----')
        self.login.login_console()
        result=self.base.is_title("测试物业智慧停车管理平台")
        self.log.info(u'登录结果:%s' % result)
        self.level_1.click_pri()
        self.level_2.click_Merchants_preferential()
        self.base.is_iframe('mainFrame')
        self.level_2.click_Statu_button()
        self.level_2.click_xbktytcc()
        self.level_2.click_third_button()
        self.level_2.click_luobotest()
        self.level_2.click_search_button()
        result=self.base.find_elements(loctor)
        a=[]
        for i in result:
            a.append(i.text)
        b=list(set(a))
        self.log.info('商户名称:%s' % b[0])
        ex='罗波测试'
        self.assertEqual(ex, b[0])
        self.log.info('-----商户优惠测试结束-----')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()