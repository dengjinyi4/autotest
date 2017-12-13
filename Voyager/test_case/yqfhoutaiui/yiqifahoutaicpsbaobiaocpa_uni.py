#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver

import unittest
import yiqifahoutai as y

class mytest(unittest.TestCase):
    
    ##初始化工作
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testcpashouding254(self):
    	'''进入https://admin.yiqifa.com/mgrSimplecpaReport.do 按照活动查询汇总记录，和cpa明细，计费方式按照cpa 对比明细中的收订订单额和汇总中的收订订单额是否相等'''
        (cpahuizong,cpamingxi)=y.yqfcpsordershishihuizong(254,'收订订单金额',6,5,'cpa','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
        self.assertTrue(y.difflist(cpahuizong,cpamingxi))
    def testcpashouding17222(self):
    	'''进入https://admin.yiqifa.com/mgrSimplecpaReport.do 按照活动查询汇总记录，和cpa明细，计费方式按照cpa 对比明细中的收订订单额和汇总中的收订订单额是否相等'''
        (cpahuizong,cpamingxi)=y.yqfcpsordershishihuizong(17222,'收订订单金额',6,5,'cpa','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
        self.assertTrue(y.difflist(cpahuizong,cpamingxi))
    def testcpashouding18318(self):
    	'''进入https://admin.yiqifa.com/mgrSimplecpaReport.do 按照活动查询汇总记录，和cpa明细，计费方式按照cpa 对比明细中的收订订单额和汇总中的收订订单额是否相等'''
        (cpahuizong,cpamingxi)=y.yqfcpsordershishihuizong(18318,'收订订单金额',6,5,'cpa','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
        self.assertTrue(y.difflist(cpahuizong,cpamingxi))
    def testcpashouding139(self):
    	'''进入https://admin.yiqifa.com/mgrSimplecpaReport.do 按照活动查询汇总记录，和cpa明细，计费方式按照cpa 对比明细中的收订订单额和汇总中的收订订单额是否相等'''
        (cpahuizong,cpamingxi)=y.yqfcpsordershishihuizong(139,'收订订单金额',6,5,'cpa','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
        self.assertTrue(y.difflist(cpahuizong,cpamingxi))
    def testcpashouding6489(self):
    	'''进入https://admin.yiqifa.com/mgrSimplecpaReport.do 按照活动查询汇总记录，和cpa明细，计费方式按照cpa 对比明细中的收订订单额和汇总中的收订订单额是否相等'''
        (cpahuizong,cpamingxi)=y.yqfcpsordershishihuizong(6489,'收订订单金额',6,5,'cpa','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
        self.assertTrue(y.difflist(cpahuizong,cpamingxi))
    def testcpashouding17971(self):
    	'''进入https://admin.yiqifa.com/mgrSimplecpaReport.do 按照活动查询汇总记录，和cpa明细，计费方式按照cpa 对比明细中的收订订单额和汇总中的收订订单额是否相等'''
        (cpahuizong,cpamingxi)=y.yqfcpsordershishihuizong(17971,'收订订单金额',6,5,'cpa','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
        self.assertTrue(y.difflist(cpahuizong,cpamingxi))
    def testcpashouding247(self):
    	'''进入https://admin.yiqifa.com/mgrSimplecpaReport.do 按照活动查询汇总记录，和cpa明细，计费方式按照cpa 对比明细中的收订订单额和汇总中的收订订单额是否相等'''
        (cpahuizong,cpamingxi)=y.yqfcpsordershishihuizong(247,'收订订单金额',6,5,'cpa','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
        self.assertTrue(y.difflist(cpahuizong,cpamingxi))
if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()