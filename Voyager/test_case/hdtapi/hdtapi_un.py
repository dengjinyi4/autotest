#!/usr/bin/env python
#encoding: utf-8

import unittest
import hdtapi as h
class mytest(unittest.TestCase):
    
    ##初始化工作
    def setUp(self):
        pass
    
    #退出清理工作
    def tearDown(self):
        pass
    
    #具体的测试用例，一定要以test开头
    def testnoticelist(self):
    	'''虚假的中奖信息接口 是否返回200'''
        url='''http://172.16.105.11:17081/notice/list.htm?adzoneId=101&act_id=166'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testrecommended(self):
    	'''广告位上返回活动信息是否返回200'''
        url='''http://172.16.105.11:17081/activity/recommended.htm?act_id=168&adzone_id=101'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testlottery_list(self):
    	'''我的奖品页面是否返回200'''
        url='''http://172.16.105.11:17081/record/lottery_list.htm?logId=B3W1CD6H1HJ9X99JUP&mediaId=55'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testlottery(self):
    	'''出广告跳转链接200'''
        url='''http://172.16.105.11:17081/lottery.htm?act_id=145&adzone_click_id=B3W1CD6H1HJX1DKRHD&device=IOS'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testactivity(self):
    	'''活动详情接口返回详情200'''
        url='''http://172.16.105.11:17081/activity/163.htm?adzoneId=101&logId=B3W1CD6H1HJXPHGC01'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testuser_lottery_info(self):
    	'''抽奖次数接口200'''
        url='''http://172.16.105.11:17081/user_lottery_info.htm?act_id=163&adzoneId=101&timeSign=1510811182682'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    # def testadzone_getLinkAct(self):
    # 	'''根据广告位id返回活动接口否返回200 http://api.admin.adhudong.com'''
    #     url='''http://172.16.105.11:17071/adzone/getLinkAct.htm?id=101'''
    #     vaule=h.allmethod(url)
    #     print '请求地址是：'+url
    #     self.assertEqual(vaule, 200)
if __name__ =='__main__':
    unittest.main()
	#testunit = unittest.TestSuite()