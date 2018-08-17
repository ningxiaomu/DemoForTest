#coding:utf-8
import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.DEBUG)
logging.debug('debug')
logging.warning('warning')
logging.info('info')
'''
日志级别： debug < info < warning < error < critical
'''

logging.debug('最低级别，一般开发用来打印一些调试信息')
logging.info('正常输出')
logging.warning('打印警示级别')
logging.error('一般用来打印一些错误信息')
logging.critical('一般用来打印一些致命的错误信息,等级最高')

'''利用logging.basicConfig()保存log到文件，
如果在logging.basicConfig()设置filename 和filemode，则只会保存log到文件，不会输出到控制台'''
logging.basicConfig(level=logging.DEBUG,
                    filename='new.log',
                    filemode='w',
                    #format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    #logging.debug('最低级别，一般开发用来打印一些调试信息'),
                    #logging.info('正常输出'),
                    #logging.warning('打印警示级别'),
                    #logging.error('一般用来打印一些错误信息'),
                    #logging.critical('一般用来打印一些致命的错误信息,等级最高')
                    )
log_file = "./new.log"
 
logging.basicConfig(filename = log_file, level = logging.DEBUG)
 
logging.debug("this is a debugmsg!")
logging.info("this is a infomsg!")
logging.warn("this is a warn msg!")
logging.error("this is a error msg!")
logging.critical("this is a critical msg!")
                    