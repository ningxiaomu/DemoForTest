# -*- coding: utf-8 -*-

from com.page.pageelement import tools

pages = tools.parseyaml()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class Level_1:
    点击账户信息 = get_locater('Level_1', '点击账户信息')
    账户信息_退出 = get_locater('Level_1', '账户信息_退出')
    账户信息_退出_确定 = get_locater('Level_1', '账户信息_退出_确定')

    
class Level_2:
    账号 = get_locater('Level_2', '账号')
    密码 = get_locater('Level_2', '密码')
    登录按钮 = get_locater('Level_2', '登录按钮')

    