#coding:utf-8
import unittest,time
from selenium import webdriver
from com.common.Level_1_menu import Leftpage1
from com.common.Level_2_menu import Leftpage2
from com.common.base import Base
from com.common.login import Login
from com.common.logger import Log

Tel_num=('id','tel') #新增车主下手机号输入
Car_no=('id','carNo') #新增车主下车牌号输入
tel='15523532345'
carnm='川A56LB6'
loctor=('xpath',".//*[@id='contentTable']/tbody/tr/td[3]") #查询出来的所有车牌号定位
class Test(unittest.TestCase):
    u'''新增车主'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login=Login(cls.driver)
        cls.level_1=Leftpage1(cls.driver)
        cls.level_2=Leftpage2(cls.driver)
        cls.base=Base(cls.driver)
        cls.log=Log()
    def test_01(self):
        u'''新增数据'''
        self.log.info('-----新增数据开始-----')
        self.login.login_console()
        result=self.base.is_title("测试物业智慧停车管理平台")
        self.log.info(u'登录结果:%s' % result)
        self.level_1.click_own()
        self.base.is_iframe('mainFrame')
        self.level_2.click_New_add()
        self.level_2.click_Choose_parking_button()
        self.level_2.click_xbktytcc()
        self.level_2.click_Merchants_choose()
        self.level_2.click_luobotest()
        self.base.sendkeys(Tel_num,tel)
        self.base.sendkeys(Car_no,carnm)
        self.level_2.click_Save_button()
        self.log.info('-----新增数据结束-----')
        #到这里保存成功了，接下来去页面查询是否真的保存成功
        self.level_2.click_Statu_button()
        self.level_2.click_xbktytcc()
        self.level_2.click_third_button()
        self.level_2.click_luobotest()
        time.sleep(3)
        self.level_2.click_Save_button()
        result=self.base.find_elements(loctor)
        a=[]
        for i in result:
            a.append(i.text)
        self.log.info('所有车牌号为:%s' % a)
        ex=carnm
        self.assertIn(ex,a)
    def test_02(self):
        u'''删除数据'''
        self.log.info('-----删除数据开始-----')
        self.level_2.click_Owner_merchants()
        self.level_2.click_Untie_button()
        time.sleep(2)
        self.level_2.click_Untie_sure_button()
        self.log.info('-----删除数据结束-----')
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()