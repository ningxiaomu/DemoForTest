#coding:utf-8

from com.common.base import Base

class Leftpage2(Base):
    u'''物管页面左侧界面，具有二级按钮'''
    Parking_enquiry=("xpath",".//*[@id='main-sidebar']/section/ul/li[2]/ul/li[1]/a") #停车场查询
    Truckspace_enquiry=("xpath",".//*[@id='main-sidebar']/section/ul/li[2]/ul/li[2]/a") #车位查询
    Lease_order=("xpath",".//*[@id='main-sidebar']/section/ul/li[5]/ul/li[1]/a")  #长租订单
    Deal_manage=("xpath",".//*[@id='main-sidebar']/section/ul/li[5]/ul/li[2]/a")  #交易管理
    Order_new=("xpath",".//*[@id='main-sidebar']/section/ul/li[5]/ul/li[3]/a") #订单新建
    Order_repair=("xpath",".//*[@id='main-sidebar']/section/ul/li[5]/ul/li[4]/a") #订单修复
    Long_rent=("xpath",".//*[@id='main-sidebar']/section/ul/li[6]/ul/li[1]/a") #长租过车
    Temporary_rent=("xpath",".//*[@id='main-sidebar']/section/ul/li[6]/ul/li[2]/a") #临停过车
    Shift_query=("xpath",".//*[@id='main-sidebar']/section/ul/li[7]/ul/li[1]/a") #班次查询
    Frequency_statistics=("xpath",".//*[@id='main-sidebar']/section/ul/li[7]/ul/li[2]/a") #班次统计
    Merchants_preferential=("xpath",".//*[@id='main-sidebar']/section/ul/li[8]/ul/li[1]/a") #商户优惠
    Preferential_use_query=("xpath",".//*[@id='main-sidebar']/section/ul/li[8]/ul/li[2]/a") #优惠使用查询
    Free_inquiry=("xpath",".//*[@id='main-sidebar']/section/ul/li[8]/ul/li[3]/a")  #免费查询
    Coupon_query=("xpath",".//*[@id='main-sidebar']/section/ul/li[8]/ul/li[4]/a")  #优惠券查询
    GuoChe_statistics=("xpath",".//*[@id='main-sidebar']/section/ul/li[9]/ul/li[1]/a") #过车统计
    Trade_statistics=("xpath",".//*[@id='main-sidebar']/section/ul/li[9]/ul/li[2]/a")  #交易统计
    Favorable_tatistics=("xpath",".//*[@id='main-sidebar']/section/ul/li[9]/ul/li[3]/a") #优惠统计
    Controller_management=("xpath",".//*[@id='main-sidebar']/section/ul/li[10]/ul/li[1]/a") #控制器管理
    Device_management=("xpath",".//*[@id='main-sidebar']/section/ul/li[10]/ul/li[2]/a")  #设备管理
    Video_surveillance =("xpath",".//*[@id='main-sidebar']/section/ul/li[10]/ul/li[3]/a") #视频监控
    User_control=("xpath",".//*[@id='main-sidebar']/section/ul/li[11]/ul/li[1]/a") #用户管理
    Role_control=("xpath",".//*[@id='main-sidebar']/section/ul/li[11]/ul/li[2]/a")  #角色管理
    Drop_out=('xpath',".//*[@id='mainWrapper']/header/nav/div/ul/li[2]/ul/li[3]/div/div") #姓名下的退出按钮
    Accept_button=('xpath',"/html/body/div[4]/div[2]/div/div/div/div/div[4]/button[1]")  #弹窗确定按钮
    Cancle_button=('xpath',"html/body/div[4]/div[2]/div/div/div/div/div[4]/button[2]") #弹窗取消按钮
    Status_button=('xpath',".//*[@id='searchForm']/div[1]/div[2]/div/div/span/span[1]/span/span[2]") #点击状态，让他弹出正常与禁用框(发现只要是第二个选择框，就是这个路径)
    Third_button=('xpath',".//*[@id='searchForm']/div[1]/div[3]/div/div/span/span[1]/span/span[2]") #第三个状态选择框
    Disable_select=('css selector','[role="treeitem"]')
    Search_button=('id','btnSubmit') #搜索按钮
    New_add_button=('xpath','html/body/div[1]/ul/li[3]/a') #新增车主按钮
    Choose_parking_button=('xpath',".//*[@id='inputForm']/div[2]/div/span/span[1]/span/span[2]") #新增车主下停车场选择1
    Merchants_choose=('xpath',".//*[@id='inputForm']/div[3]/div/span/span[1]/span/span[2]") #新增车主下商户选择按钮
    Save_button=('xpath',".//*[@id='btnSubmit']") #新增车主下保存按钮
    Owner_merchants=('xpath',".//*[@id='contentTable']/tbody/tr/td[10]/a[1]") #车主查询出来后的车主商户
    Untie_button=('xpath',".//*[@id='contentTable']/tbody/tr/td[6]/a") #解绑
    Untie_sure_button=('xpath',"html/body/div[2]/div[2]/div/div/div/div/div[4]/button[1]") #解绑确定按钮
    def click_Parking_enquiry(self):
        self.click(self.Parking_enquiry)
    def click_Truckspace_enquiry(self):
        self.click(self.Truckspace_enquiry)
    def click_Lease_order(self):
        self.click(self.Lease_order)
    def click_Deal_manage(self):
        self.click(self.Deal_manage)
    def click_Order_new(self):
        self.click(self.Order_new)
    def click_Order_repai(self):
        self.click(self.Order_repai)
    def click_Long_rent(self):
        self.click(self.Long_rent)
    def click_Temporary_rent(self):
        self.click(self.Temporary_rent)
    def click_Shift_query(self):
        self.click(self.Shift_query)
    def click_Frequency_statistics(self):
        self.click(self.Frequency_statistics)
    def click_Merchants_preferential(self):
        self.click(self.Merchants_preferential)
    def click_Preferential_use_query(self):
        self.click(self.Preferential_use_query)
    def click_Free_inquiry(self):
        self.click(self.Free_inquiry)
    def click_Coupon_query(self):
        self.click(self.Coupon_query)
    def click_GuoChe_statistics(self):
        self.click(self.GuoChe_statistics)
    def click_Trade_statistics(self):
        self.click(self.Trade_statistics)
    def click_Favorable_tatistics(self):
        self.click(self.Favorable_tatistics)
    def click_Controller_management(self):
        self.click(self.Controller_management)
    def click_Device_management(self):
        self.click(self.Device_management)
    def click_Video_surveillance(self):
        self.click(self.Video_surveillance)
    def click_User_control(self):
        self.click(self.User_control)
    def click_Role_control(self):
        self.click(self.Role_control)
    def click_Drop_out(self):
        self.click(self.Drop_out)
    def click_Accept_button(self):
        self.click(self.Accept_button)
    def click_Cancle_button(self):
        self.click(self.Cancle_button)
    def click_Statu_button(self):
        self.click(self.Status_button)
    def click_Disable(self):
        self.find_elements(self.Disable_select)[2].click()
    def click_search_button(self):
        self.click(self.Search_button)
    def click_xbktytcc(self):
        self.find_elements(self.Disable_select)[9].click()
    def click_third_button(self):
        self.click(self.Third_button)
    def click_luobotest(self):
        self.find_elements(self.Disable_select)[6].click()
    def click_New_add(self):
        self.click(self.New_add_button)
    def click_Choose_parking_button(self):
        self.click(self.Choose_parking_button)  
    def click_Merchants_choose(self):
        self.click(self.Merchants_choose)
    def click_Save_button(self):
        self.click(self.Save_button)
    def click_Owner_merchants(self):
        self.click(self.Owner_merchants)
    def click_Untie_button(self):
        self.click(self.Untie_button)
    def click_Untie_sure_button(self):
        self.click(self.Untie_sure_button)
    
        
        
        
        
    
        
