#!/usr/bin/env python
# encoding: utf-8
import requests,urllib,json,hashlib
# 模拟投放
def ad_simulation(host):
    param={'adZoneId':1,'positionId':1,'bidTime':'2017-07-04'}
    url='http://'+host+'/ad_simulation.do?'
    print url
    s=requests.session()
    r=s.get(url,params=param)
    print len(r.json()['data']['1'])
    # r=s.get('http://admin.adhudong.com:17071/user/ListUser.htm?username=coldman&status=1&descn=jack&create_time=1')
    return r
# 返回奖品列表
def allmethod(url):
    # url='https://apidisplay.adhudong.com/notice/list.htm?adzoneId=101&act_id=166'
    s=requests.session()
    s.get('http://172.16.105.11:17081/site_login_ijf.htm?app_key=adhub3dbfbcee89b4821&user_id=not_login&sign=4e2de116fe879d49064a2627616f08e1',verify=False)
    r=s.get(url,verify=False)
    print r.text
    return r.json()['code']
if __name__ == '__main__':
    # ad_simulation('123.59.17.85:17200')
    x=allmethod('https://apidisplay.adhudong.com/activity/recommended.htm?act_id=168&adzone_id=101')
    print type(x)
    print x