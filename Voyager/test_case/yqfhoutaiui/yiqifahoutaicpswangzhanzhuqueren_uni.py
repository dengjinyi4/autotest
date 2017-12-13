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
    def testcpswangzhanzhuqueren254(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(254,'网站主确认佣金',90,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpswangzhanzhuqueren17222(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(17222,'网站主确认佣金',90,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpswangzhanzhuqueren18318(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(18318,'网站主确认佣金',90,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpswangzhanzhuqueren139(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(139,'网站主确认佣金',90,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpswangzhanzhuqueren6489(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(6489,'网站主确认佣金',90,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpswangzhanzhuqueren17971(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(17971,'网站主确认佣金',90,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpswangzhanzhuqueren247(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比数据是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizong(247,'网站主确认佣金',60,3,'/html/body/div[2]/table/tbody/tr[2]/td[18]','/html/body/center/div/table/tbody/tr[21]/td[22]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsxujiadan(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 查询虚假单金额'''
        (cpshuizong,cpsmingxi)=y.yqfxjd('虚假订单额',6,7,'/html/body/div[2]/table/tbody/tr[2]/td[12]','/html/body/div/table[2]/tbody/tr[22]/td[14]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
if __name__ =='__main__':
    unittest.main()
    #testunit = unittest.TestSuite()