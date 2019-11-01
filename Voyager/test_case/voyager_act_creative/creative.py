#!/usr/bin/env python
# encoding: utf-8
import requests,random,json,sys,datetime,time
import creative_act_pic as cp
import logging
import db
reload(sys)
sys.setdefaultencoding('utf8')
# def getcreativeid():
# #     tmpsql='''SELECT adv.`name`,ao.id,ao.advertiser_id,aoc.creative_id,acl.link_common
# # from voyager.ad_order_creative aoc,voyager.ad_creative_link acl,voyager.ad_order ao,voyager.advertiser adv,voyager.report_order reo
# # where ao.state=4 and aoc.order_id=ao.id and aoc.creative_id=acl.creative_id and acl.is_valid=1 and adv.id=ao.advertiser_id and aoc.state=1
# # and reo.adorder_id=ao.id and reo.ad_consume>100 AND reo.date='2019-10-18'
# # and reo.update_time>adddate(now(),interval -30 minute);'''
#     tmpsql='''SELECT adv.name,ao.advertiser_id,ao.id,roh.creative_id,acl.link_common from voyager.report_order_hour roh,voyager.ad_order ao,voyager.ad_creative_link acl,voyager.advertiser adv
#             where roh.adorder_id=ao.id and roh.ad_consume>100 and date='{0}' and `hour`='{1}'
#             and roh.advertiser_id=adv.id and roh.creative_id=acl.creative_id and acl.is_valid=1 and acl.link_common<>'';'''.format(time.strftime("%Y-%m-%d", time.localtime()),time.strftime("%H", time.localtime()))
#     print tmpsql
#     result=db.selectsql('devvoyager',tmpsql)
#     return result
def getcreativehttpcode():
    # creative=(('广告主名称1','1111','1222','123','https://www.jimujia.com/'),('广告主名称2','2222','2222','456','https://www.baidu.com/'),('广告主名称3','333','3222','789','https://mob.0792gdst.com/e11/'))
    creative=cp.getcreativeid()
    r=requests.session()
    r.keep_alive = False
    tmplist=[]
    for i in creative:
        # time.sleep(3)
        tmpcaseresult=[]
        # 广告主名称
        tmpcaseresult.append(i[0])
        # 广告主id
        tmpcaseresult.append(i[1])
        # 订单id
        tmpcaseresult.append(i[2])
        # 创意id
        tmpcaseresult.append(i[3])
        # 创意url
        tmpcaseresult.append(i[4])
        try:
            # 创意中如果存在${click_tag}就替换成字符串
            result=r.get(i[4].replace('${click_tag}','123'),verify=False)
            # 实际返回结果
            tmpcaseresult.append(result.status_code)
            print 'check httpcode advertiser_name:{0}, order_id{1},advertiser_id{2},ad_creaveid{3},ad_creave_url:{4}'.format(str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]))
            r.close()
        except Exception as e:
            print 'error creavi_id {0},creaveid_url:{1}'.format(str(i[3]),str(i[4]))
            print e.message
            tmpcaseresult.append(e.message)
        tmpcaseresult.append(200)
        tmplist.append(tuple(tmpcaseresult))
    print tmplist
    return tmplist

def getacthttpcode():
    # acturl=(('123','https://www.jimujia111.com/','aaaa'),)
    acturl=cp.getacturl()
    r=requests.session()
    r.keep_alive = False
    tmplist=[]
    for i in acturl:
        tmpcaseresult=[]
        # 活动id
        tmpcaseresult.append(i[0])
        # 活动url
        tmpcaseresult.append(i[1])
        # 活动名称
        tmpcaseresult.append(i[2])
        try:
            # 创意中如果存在${click_tag}就替换成字符串
            r.get('https://display.intdmp.com/site_login_ijf.htm?app_key=adhu21fab394150d4e95')
            result=r.get(i[1].replace('${click_tag}','123'),verify=False)
            # 实际返回结果
            tmpcaseresult.append(result.status_code)
            print 'check act httpcode act id:{0}, 活动url{1}'.format(str(i[0]),str(i[1]))
            r.close()
        except Exception as e:
            print 'error act id为{0},url:{1}'.format(str(i[0]),str(i[1]))
            tmpcaseresult.append(e.message)
        tmpcaseresult.append(200)
        tmplist.append(tuple(tmpcaseresult))
    print tmplist
    return tmplist

if __name__ == '__main__':
    # getacthttpcode()
    getcreativehttpcode()
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print time.strftime("%H", time.localtime())
    # print time.strftime("%Y-%m-%d", time.localtime())
    # print type(time.strftime("%Y-%m-%d", time.localtime()))
    # print 1
    # tmpstr='321,445,555,444,443'
    # print tmpstr.split(',')
    # url='http://be10.liqijt.com/#_0'
    # i=0
    # while i<13300:
    #     r=requests.session()
    #     try:
    #         res=r.get(url)
    #     except Exception as e:
    #         print e.message
        # if res.status_code<>200:
        #     print res.status_code
        # res.status_code
        # print res.status_code
        # i=i+1
    print 'ok1111111111111111111111111111111111111111111111111111111111111111111111111111111111'