#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver
# --------------------------------
# ----对比有效订单额是否正确--------
# --------------------------------
import unittest
import yiqifahoutai as y

class mytest(unittest.TestCase):
    
    ##初始化工作
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testcpyxddj254(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中：有效订单额是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(254,'有效订单额',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[11]','/html/body/center/div/table/tbody/tr[21]/td[16]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpyxddj17222(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中：有效订单额是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(17222,'有效订单额',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[11]','/html/body/center/div/table/tbody/tr[21]/td[16]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpyxddj18318(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中：有效订单额是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(18318,'有效订单额',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[11]','/html/body/center/div/table/tbody/tr[21]/td[16]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpyxddj139(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中：有效订单额是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(139,'有效订单额',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[11]','/html/body/center/div/table/tbody/tr[21]/td[16]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpyxddj6489(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中：有效订单额是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(6489,'有效订单额',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[11]','/html/body/center/div/table/tbody/tr[21]/td[16]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpyxddj17971(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中：有效订单额是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(17971,'有效订单额',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[11]','/html/body/center/div/table/tbody/tr[21]/td[16]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpyxddj247(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中：有效订单额是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(247,'有效订单额',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[11]','/html/body/center/div/table/tbody/tr[21]/td[16]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()