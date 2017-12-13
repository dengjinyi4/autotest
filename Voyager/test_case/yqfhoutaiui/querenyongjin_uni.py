#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver
# --------------------------------
# ----对比确认佣金是否正确--------
# --------------------------------
import unittest
import yiqifahoutai as y

class mytest(unittest.TestCase):
    
    ##初始化工作
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testcpsqryj254(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中的：网站主确认佣金 是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(254,'网站主确认佣金',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsqryj17222(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中的：网站主确认佣金 是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(17222,'网站主确认佣金',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsqryj18318(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中的：网站主确认佣金 是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(18318,'网站主确认佣金',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsqryj139(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中的：网站主确认佣金 是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(139,'网站主确认佣金',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsqryj6489(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中的：网站主确认佣金 是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(6489,'网站主确认佣金',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsqryj17971(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中的：网站主确认佣金 是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(17971,'网站主确认佣金',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsqryj247(self):
    	'''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，计费方式按照cps 对比明细和汇总中的：网站主确认佣金 是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(247,'网站主确认佣金',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()