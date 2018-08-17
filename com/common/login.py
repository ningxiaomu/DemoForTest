#coding:utf-8
#from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from com.common.base import Base
from selenium import webdriver
from com.page.pageelement.pages import *
url='http://console.ezparking.com.cn/console/a/login'
class Login(Base):

    def input_usernme(self,username):
        u'''输入账号'''
        self.sendkeys(Level_2.账号,username)
    
    def input_psw(self,psw):
        u'''输入密码'''
        self.sendkeys(Level_2.密码, psw)
    
    def click_button(self):
        u'''点击登录按钮'''
        self.click(Level_2.登录按钮)
    
    def login_console(self,username='15123532344', psw='Luobo123'):
        u'''执行登录操作'''
        self.open(url)
        self.input_usernme(username)
        self.input_psw(psw)
        self.click_button()
    
    def get_result(self,title=u'测试物业智慧停车管理平台'):
        u'''断言'''
        try:
            if self.is_title(title):
                print(u'登录成功')
        except:
            print(u'登录失败')

if __name__ == "__main__":
    driver =webdriver.Firefox()
    loginpage=Login(driver)
    loginpage.login_console(username='15123532344', psw='Luobo123')
    title=u'测试物业智慧停车管理平台'
    loginpage.get_result(title)
    
            
    
    
    
    
    
    