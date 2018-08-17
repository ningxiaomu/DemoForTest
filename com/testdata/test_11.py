from com.common.readini import HanddleIni
import os,unittest

class Test(unittest.TestCase):

    def test_loc1(self):
        '''获取停车场查询'''
        parentpath=os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".")
        print(parentpath)
        filepath=os.path.join(parentpath,r'com\config\test.ini')
        ini1=HanddleIni(filepath)
        loc=ini1.readini('email', 'to_addrs')
        return loc
    def test_02(self):
        a=self.test_loc1()
        print(a)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()