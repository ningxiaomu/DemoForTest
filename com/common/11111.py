from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.select import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=Firefox()
driver.get('http://console.ezparking.com.cn/console/a?login')
title=driver.title
print(title)
#selector = Select(driver.find_element_by_id("selectdemo"))
#selector.select_by_index("2")

driver.find_element_by_id('username').send_keys('15123532344')
driver.find_element_by_id('password').send_keys('Luobo123')
driver.find_element_by_xpath(".//*[@id='normal_login']/div/div/div[3]/button").click()
'''
driver.find_element_by_xpath(".//*[@id='main-sidebar']/section/ul/li[2]/a/span[1]").click()  #停车场管理
driver.find_element_by_xpath(".//*[@id='main-sidebar']/section/ul/li[2]/ul/li[1]/a").click()
driver.switch_to_frame('mainFrame')
print('iFrame切换成功')

a=WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath(".//*[@id='searchForm']/div[1]/div[2]/div/div/span/span[1]/span/span[2]"))
print('1111111111')
a.click()
driver.find_elements_by_css_selector('[role="treeitem"]')[2].click()
driver.find_element_by_xpath(".//*[@id='btnSubmit']").click()
a=driver.find_element_by_xpath(".//*[@id='contentTable']/tbody/tr[2]/td[8]")
print(a.text)

driver.find_element_by_xpath(".//*[@id='main-sidebar']/section/ul/li[4]/a/span").click()
driver.switch_to_frame('mainFrame')
'''
driver.find_element_by_xpath(".//*[@id='main-sidebar']/section/ul/li[4]/a/span").click()
driver.switch_to_frame('mainFrame')
WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath("html/body/div[1]/ul/li[3]/a")).click()
a=WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath(".//*[@id='inputForm']/div[2]/div/span/span[1]/span/span[2]"))
a.click()
driver.find_elements_by_css_selector('[role="treeitem"]')[9].click()
driver.find_element_by_xpath(".//*[@id='inputForm']/div[3]/div/span/span[1]/span/span[2]").click()
driver.find_elements_by_css_selector('[role="treeitem"]')[6].click()
driver.find_element_by_id('tel').send_keys('15123532346')
driver.find_element_by_id('carNo').send_keys('川A56LB7')
driver.find_element_by_id('btnSubmit').click()

a=WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath(".//*[@id='searchForm']/div[1]/div[2]/div/div/span/span[1]/span/span[2]"))
print('1111111111')
a.click()
driver.find_elements_by_css_selector('[role="treeitem"]')[9].click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='searchForm']/div[1]/div[3]/div/div/span/span[1]/span/span[2]").click()
driver.find_elements_by_css_selector('[role="treeitem"]')[6].click()
driver.find_element_by_id('btnSubmit').click()


    