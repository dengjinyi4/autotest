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
        url='''http://apidisplay.adhudong.com/notice/list.htm?adzoneId=101&act_id=166'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testrecommended(self):
    	'''广告位上返回活动信息是否返回200'''
        url='''http://apidisplay.adhudong.com/activity/recommended.htm?act_id=168&adzone_id=101'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testlottery_list(self):
    	'''我的奖品页面是否返回200'''
        url='''http://apidisplay.adhudong.com/record/lottery_list.htm?logId=B3W1CD6H1HJ9X99JUP&mediaId=55'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testlottery(self):
    	'''出广告跳转链接200'''
        url='''http://apidisplay.adhudong.com/lottery.htm?act_id=145&adzone_click_id=B3W1CD6H1HJX1DKRHD&device=IOS'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testactivity(self):
    	'''活动详情接口返回详情200'''
        url='''http://apidisplay.adhudong.com/activity/163.htm?adzoneId=101&logId=B3W1CD6H1HJXPHGC01'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def testuser_lottery_info(self):
    	'''刷新活动页面接口接口200'''
        url='''http://apidisplay.adhudong.com/user_lottery_info.htm?act_id=163&adzoneId=101&timeSign=1510811182682'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 200)
    def test_award_detail(self):
    	'''广告详情页接口200'''
        # url='''http://172.16.105.11:17081/record/award_detail/C3W1CD6H1HLY1FNJZ5.htm?choosen_tag=D3W1CD6R1HLY1FNJZ5'''
        url='''http://apidisplay.adhudong.com/record/award_detail/C3W1CD6H1HLY1FNJZ5.htm?choosen_tag=D3W1CD6R1HLY1FNJZ5'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertEqual(vaule, 303)
    def test_phone_login_ijf(self):
    	'''手机号注册登录接口 提供了用户基本信息查询功能 200'''
        # url='''http://172.16.105.11:17081/record/award_detail/C3W1CD6H1HLY1FNJZ5.htm?choosen_tag=D3W1CD6R1HLY1FNJZ5'''
        url='''http://apidisplay.adhudong.com/phone_login_ijf.htm?media_id=2&phone=13621348140&adzone_id=101'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule, [200])
    def test_sign(self):
    	'''签到接口200'''
        url='''http://apidisplay.adhudong.com/sign.htm?act_id=32&adzoneId=101'''
        vaule=h.actmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[401,200])
    def test_goldcoin_ex_list(self):
    	'''可兑换奖品接口200'''
        url='''http://apidisplay.adhudong.com/goldcoin_ex_list.htm?page_num=10&page_size=22'''
        vaule=h.actmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[401,200])
    def test_my_gold_list(self):
    	'''我的金币接口200'''
        url='''http://apidisplay.adhudong.com/my_gold_list.htm'''
        vaule=h.actmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[401,200])
    def test_act_more(self):
    	'''幸运抽奖接口接口200'''
        url='''http://apidisplay.adhudong.com/activity/act_more.htm?adzone_id=101&adzone_click_id=B3W1CD6H1HM5PG9QWX'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[200])
    def test_times(self):
    	'''换个活动-判断接口200'''
        url='''http://apidisplay.adhudong.com/activity/times.htm?act_id=59&adzoneId=101'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[200])
    def test_next(self):
    	'''换个活动接口200'''
        url='''http://apidisplay.adhudong.com/activity/next.htm?act_id=59&adzoneId=101&app_key=adhub3dbfbcee89b4821'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[200])
    def test_activity(self):
    	'''活动信息获取接口获取模板信息接口200'''
        url='''http://apidisplay.adhudong.com/preload/activity/59.htm?adzoneId=101&logId=B3W1CD6H1HM5PG9QWX'''
        vaule=h.allmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[200])
    def test_jfb_ex_userinfo(self):
    	'''兑换集分宝_用户信息金币兑换集分宝_获取用户信息接口200'''
        url='''http://apidisplay.adhudong.com/jfb_ex_userinfo.htm'''
        vaule=h.actmethod(url)
        print '请求地址是：'+url
        self.assertIn(vaule,[200])
    # def testadzone_getLinkAct(self):
    # 	'''根据广告位id返回活动接口否返回200 http://api.admin.adhudong.com'''
    #     url='''http://172.16.105.11:17071/adzone/getLinkAct.htm?id=101'''
    #     vaule=h.allmethod(url)
    #     print '请求地址是：'+url
    #     self.assertEqual(vaule, 200)
if __name__ =='__main__':
    unittest.main()


	#testunit = unittest.TestSuite()