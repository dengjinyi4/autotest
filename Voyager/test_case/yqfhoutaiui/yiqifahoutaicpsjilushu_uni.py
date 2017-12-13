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
    def testcpsshoudingdingdanshu254(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的收订订单数和汇总中的收订订单数'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(254,'收订订单数',4,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    # def testcpsshoudingdingdanshu17222(self):
    #     '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的收订订单数和汇总中的收订订单数'''
    #     (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(17222,'收订订单数',4,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
    #     self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsshoudingdingdanshu18318(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的收订订单数和汇总中的收订订单数'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(18318,'收订订单数',4,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsshoudingdingdanshu139(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的收订订单数和汇总中的收订订单数'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(139,'收订订单数',4,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsshoudingdingdanshu6489(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的收订订单数和汇总中的收订订单数'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(6489,'收订订单数',4,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsshoudingdingdanshu17971(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的收订订单数和汇总中的收订订单数'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(17971,'收订订单数',4,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    def testcpsshoudingdingdanshu247(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的收订订单数和汇总中的收订订单数'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(247,'收订订单数',60,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
        self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
    # def testcpsxujiadan(self):
    #     '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 查询虚假单金额'''
    #     (cpshuizong,cpsmingxi)=y.yqfxjd('虚假订单额',6,7,'/html/body/div[2]/table/tbody/tr[2]/td[12]','/html/body/div/table[2]/tbody/tr[22]/td[14]')
    #     self.assertTrue(y.difflist(cpshuizong,cpsmingxi))
if __name__ =='__main__':
    unittest.main()
    #testunit = unittest.TestSuite()