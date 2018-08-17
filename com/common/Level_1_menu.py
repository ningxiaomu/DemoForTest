#coding:utf-8

from com.common.base import Base
class Leftpage1(Base):
    u'''物管页面左侧界面+隐藏按钮+收银台按钮+姓名按钮'''
    pro_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[1]/a")  #物业管理
    pak_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[2]/a")  #停车场管理
    bus_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[3]/a")  #商户管理
    own_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[4]/a")  #车主管理
    ord_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[5]/a")  #订单管理
    cro_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[6]/a")  #过车管理
    cla_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[7]/a")  #班次管理
    pri_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[8]/a")  #优惠管理
    sta_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[9]/a")  #统计管理
    dev_m=('xpath',".//*[@id='main-sidebar']/section/ul/li[10]/a") #设备管理
    sys_s=('xpath',".//*[@id='main-sidebar']/section/ul/li[11]/a") #系统设置
    log_o=('xpath',".//*[@id='main-sidebar']/section/ul/li[12]/a") #注销
    hid_b=('xpath',".//*[@id='mainWrapper']/header/nav/a[1]")      #隐藏按钮
    cas_b=('xpath',".//*[@id='checkout']")                         #收银台按钮
    nam_b=('xpath',".//*[@id='mainWrapper']/header/nav/div/ul/li[2]/a") #姓名按钮
    
    
    
    def click_pro(self):
        self.click(self.pro_m)
     
    def click_pak(self):
        self.click(self.pak_m)
        
    def click_bus(self):
        self.click(self.bus_m)
        
    def click_own(self):
        self.click(self.own_m)
        
    def click_ord(self):
        self.click(self.ord_m)
        
    def click_cro(self):
        self.click(self.cro_m)
    
    def click_cla(self):
        self.click(self.cla_m)
    
    def click_pri(self):
        self.click(self.pri_m)
    
    def click_sta(self):
        self.click(self.sta_m)
        
    def click_dev(self):
        self.click(self.dev_m)
    
    def click_sys(self):
        self.click(self.sys_s)
        
    def click_log(self):
        self.click(self.log_o)
        
    def click_hid(self):
        self.click(self.hid_b)
        
    def click_cas(self):
        self.click(self.cas_b)
        
    def click_nam(self):
        self.click(self.nam_b)
        

        
        
    
    
