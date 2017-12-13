#!/usr/bin/env python
#encoding: utf-8
# from appium import webdriver
# --------------------------------
# ----对比有效订单数 和 收订商品数 是否正确--------
# --------------------------------
import unittest
import yiqifahoutai as y

class mytest(unittest.TestCase):
    
    ##初始化工作
    #退出清理工作
    def tearDown(self):
        pass
    #具体的测试用例，一定要以test开头
    def testcpsyouxiaodingdanshu254(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的有效商品数和汇总中的收订商品数是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(254,'有效订单数',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[7]','/html/body/center/div/table/tbody/tr[21]/td[15]')
        self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
    # def testcpsyouxiaodingdanshu17222(self):
    #     '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的有效商品数和汇总中的收订商品数是否相等'''
    #     (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(17222,'有效订单数',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[7]','/html/body/center/div/table/tbody/tr[21]/td[15]')
    #     self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
    def testcpsyouxiaodingdanshu18318(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的有效商品数和汇总中的收订商品数是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(18318,'有效订单数',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[7]','/html/body/center/div/table/tbody/tr[21]/td[15]')
        self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
    def testcpsyouxiaodingdanshu139(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的有效商品数和汇总中的收订商品数是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(139,'有效订单数',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[7]','/html/body/center/div/table/tbody/tr[21]/td[15]')
        self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
    def testcpsyouxiaodingdanshu6489(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的有效商品数和汇总中的收订商品数是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(6489,'有效订单数',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[7]','/html/body/center/div/table/tbody/tr[21]/td[15]')
        self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
    def testcpsyouxiaodingdanshu17971(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的有效商品数和汇总中的收订商品数是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(17971,'有效订单数',105,10,'cps','/html/body/div[2]/table/tbody/tr[2]/td[7]','/html/body/center/div/table/tbody/tr[21]/td[15]')
        self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
    def testcpsyouxiaodingdanshu247(self):
        '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 按照活动查询汇总记录，和cps明细，对比明细中的有效商品数和汇总中的收订商品数是否相等'''
        (cpshuizong,cpsmingxi)=y.yqfcpsordershishihuizonggeshu(247,'有效订单数',60,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[7]','/html/body/center/div/table/tbody/tr[21]/td[15]')
        self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
    # def testcpsxujiadan(self):
    #     '''进入https://admin.yiqifa.com/mgrSimpleCpsReport.do 查询虚假单金额'''
    #     (cpshuizong,cpsmingxi)=y.yqfxjd('虚假订单额',6,7,'/html/body/div[2]/table/tbody/tr[2]/td[12]','/html/body/div/table[2]/tbody/tr[22]/td[14]')
    #     self.assertTrue(y.difflistcout(cpshuizong,cpsmingxi))
if __name__ =='__main__':
    unittest.main()
    #testunit = unittest.TestSuite()