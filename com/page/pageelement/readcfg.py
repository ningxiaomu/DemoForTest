#coding:utf-8
u'''获取某个元素'''
import os
import yaml
curpath=os.path.realpath(__file__)
dirpath=os.path.dirname(curpath)
filepath=os.path.join(dirpath,'baiduyuedu_Level2.yaml')
f=open(filepath,'r',encoding='utf-8')
ele=f.read()
f.close()
element=yaml.load(ele)
print(element)
# for i in element['test']['loctors']:
#     print(i)

# def get_ele(name):
#     locs=element['Level_2']
#     for i in locs:
#         if name ==i['name']:
#             return i
#         
# if __name__=='__main__':
#     print(get_ele(name='百度搜索框'))
        