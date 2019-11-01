#!/usr/bin/env python
# encoding: utf-8
import requests,random,json,sys,datetime,time,mydriverpath
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from PIL import Image
import logging
import db,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from log import common_log as l
from collections import OrderedDict
# from requests_toolbelt import MultipartEncoder
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
# 模拟投放
reload(sys)
sys.setdefaultencoding('utf8')


# 本地imge
def mywebdriver(creative_id,url):
    mobile_emulation = {"deviceName":"iPhone 6"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # 去掉 “Chrome 正在受到自动化软件控制”
    chrome_options.add_argument('disable-infobars')
    time.sleep(2)
    # chromedriver="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    chromedriver = mydriverpath.drvierpath()
    desired_capabilities = DesiredCapabilities.CHROME
    # 不加载完就结束get
    desired_capabilities["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
    driver.set_page_load_timeout(10)
    # driver.get("http://www.baidu.com")
    url=url.replace('${click_tag}','123')
    print 'replace url：{0}'.format(url)
    # 为了能打开活动，需要先请求一次广告位链接，在浏览器中缓存数据
    driver.get('https://display.intdmp.com/site_login_ijf.htm?app_key=adhu21fab394150d4e95')
    driver.implicitly_wait(15)
    try:
        # driver.get('https://display.intdmp.com/site_login_ijf.htm?app_key=adhu21fab394150d4e95')
        time.sleep(5)
        # 如果是亿起发的链接就多等一会，
        if isyiqifaurl(url):
            driver.get(url)
            time.sleep(20)
        else:
            driver.get(url)
            time.sleep(6)
        driver.implicitly_wait(15)
        # picdir=u'C:/auto/Voyageractivity_production_actactive/pic'
        # picdir=u'D:/work/互动推/pic/'
        picdir=u'D:/auto/pic/'
        picname=picdir+str(creative_id)+'_'+str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))+'.png'
        driver.get_screenshot_as_file(picname)
        croppic(picname)
        driver.quit()
    except Exception as e:
        print 'open url error {0}'.format(e.message)
        driver.quit()
        driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)

    return picname
# 重新截取一下尺寸
def croppic(picname):
    # picdir=u'D:/work/互动推/pic/637_2019_10_30_15_50_12.png'
    im=Image.open(picname)
    print im.size
    im=im.crop((0,0,470,668))
    im.save(picname)
    return 1
# 看请求地址里是否有亿起发链接，如果有就让浏览器多等一会
def isyiqifaurl(url):
    tmplist=["p.yiqifa.com","p.eqifa.com","p.gouwubang.com","p.egou.com","p.gouwuke.com","p.yiqiso.com","p.jiuxinban.com","p.yijifen.com",'p.yiqifa.org']
    for i in tmplist:
        if i in url:
            return True
    return False

# 取得活动id和活动url list
def getacturl():
    tmpsql='''SELECT DISTINCT act_id from voyagerstat.summary_act_hour{0} where `hour`={1} AND act_show_num>20 and act_id<>100 limit 3000  '''.format(time.strftime("%Y%m%d", time.localtime()),time.strftime("%H", time.localtime()))
    reactid=db.selectsql("voyagerstatdev",tmpsql)
    tmpactid_all=''
    for i in reactid:
        tmpactid_all=tmpactid_all + str(i[0])+','
    print tmpactid_all
    tmpsqllocation_addresss='''SELECT  a.id,v.location_adress,a.act_name  FROM voyager.base_act_info a
    INNER JOIN voyager.base_template_info t ON a.template_id = t.id
    LEFT JOIN voyager.template_type v ON t.template_type_id = v.id
    WHERE a.status=1 and a.id in ({0})'''.format(tmpactid_all[0:-1])
    print tmpsqllocation_addresss
    # 查找活动和活动对应的html地址
    res_acturl=db.selectsql('devvoyager',tmpsqllocation_addresss)
    tmpact_url=[]
    for i in res_acturl:
        stract='''{0}?logId=B0H2YDC01JPO44JW9T&adzoneId=5177&actId={1}&ref=&mediaId=2&ctm_code=Mi8vODQwLy8yLy8yLy8yNDAzMC8vMTU2NjgxOTM4MDEyMy8vYmNmZDliMmQ1NWY1M2M2NzNmZDZjNDFkZTk3OTcyMjcvLzQwMTkxYTgyNjM4Mg==&isIntercept=1'''
        tmplist=[]
        # 数据库中的template_type表中目标地址有display.adhudong.com display.eqigou.com开头的地址，需要都替换成display.intdmp.com
        if 'adhudong' in str(i[1]):
            stract=stract.format(str(i[1]).replace('adhudong','intdmp'),str(i[0]))
        if 'eqigou' in str(i[1]):
            stract=stract.format(str(i[1]).replace('eqigou','intdmp'),str(i[0]))
        if 'intdmp' in str(i[1]):
            stract=stract.format(str(i[1]),str(i[0]))
        tmplist.append(i[0])
        tmplist.append(stract)
        tmplist.append(i[2])
        tmpact_url.append(tmplist)
    print tmpact_url
    return tmpact_url
# 抓取活动图片并存库
def actpic():
    r=requests.session()
    tmpactpic=getacturl()
    for i in tmpactpic:
        localpic=mywebdriver(i[0],i[1])
        # localpic=mywebdriver(34443,'http://ak01.263917.com')
        # localpic=u'D:/work/互动推/pic/605_2019_10_30_16_05_31.png'
        imageurl=getimgurl(localpic)
        time.sleep(2)
        url="http://open.adhudong.com/addPageMonitor.htm"
        para={"type":"2","url":i[1],"actId":i[0],"imageUrl":imageurl}
        res=r.get(url,params=para,verify=False)
        # print res.json()
    return 1

# 获取符合条件的创意地址 运行当前小时广告消耗大于10块钱的创意地址
def getcreativeid():
#     tmpsql='''SELECT adv.`name`,ao.id,ao.advertiser_id,aoc.creative_id,acl.link_common
# from voyager.ad_order_creative aoc,voyager.ad_creative_link acl,voyager.ad_order ao,voyager.advertiser adv,voyager.report_order reo
# where ao.state=4 and aoc.order_id=ao.id and aoc.creative_id=acl.creative_id and acl.is_valid=1 and adv.id=ao.advertiser_id and aoc.state=1
# and reo.adorder_id=ao.id and reo.ad_consume>100 AND reo.date='2019-10-18'
# and reo.update_time>adddate(now(),interval -30 minute);'''
    tmpsql='''SELECT adv.name,ao.advertiser_id,ao.id,roh.creative_id,acl.link_common from voyager.report_order_hour roh,voyager.ad_order ao,voyager.ad_creative_link acl,voyager.advertiser adv
        where roh.adorder_id=ao.id and roh.ad_consume>100 and date='{0}' and `hour`='{1}'
        and roh.advertiser_id=adv.id and roh.creative_id=acl.creative_id and acl.is_valid=1 and acl.link_common<>'' limit 2000;'''.format(time.strftime("%Y-%m-%d", time.localtime()),time.strftime("%H", time.localtime()))
    print tmpsql
    result=db.selectsql('devvoyager',tmpsql)
    return result

# 图片上传 返回图片服务器url
def getimgurl(localurl):
    r=requests.session()
    url='https://apidemand.adhudong.com/upload.htm'
    # data={"data":open("D:/work/pic/2.png",'rb')}
    # files={"uploadFile":("3.png",open(r"D:/work/pic/4.png","rb"),"image/png"), "dict":(None,"2")}
    files={"uploadFile":("3.png",open(localurl,"rb"),"image/png"), "dict":(None,"2")}
    re=r.post(url,files=files)
    imageurl=str(json.loads(re.json())['data'])
    # print type(str(json.loads(re.json())['data']))
    return imageurl
# 循环所有的创意地址,调用晁斌接口存储图片
def creativepic():
    r=requests.session()
    creativeid=getcreativeid()
    # creativeid=(("aaa",2112,20169,20951,"https://p.yiqifa.org/c?w=1017793&c=17994&i=42569&pf=y&e=${click_tag}&t=https://cs.m.jd.com/babelDiy/Zeus/FvKextEWVjwQWtpuw6ep2jX6Akp/index.html"),)
    for i in creativeid:
        # 本地img地址
        print '调用webdirver传参数活动id:{0},访问地址{1}'.format(i[3],i[4])
        picurl=mywebdriver(i[3],i[4])
        # picurl=mywebdriver(123,'http://xy36132.com/#')
        # print picurl
        # 服务器img地址
        imageurl=getimgurl(picurl)
        # print imageurl
        time.sleep(2)
        url="http://open.adhudong.com/addPageMonitor.htm"
        para={"type":"1","advertiserId":i[1],"adCreativeId":i[3],"adOrderId":i[2],"url":i[4],"imageUrl":imageurl}
        res=r.get(url,params=para)
        # print res.url
        # print res.json()
    return 1


if __name__ == '__main__':
    # getcreativehttpcode()
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print time.strftime("%Y%m%d%H%M%S", time.localtime())
    # print type(time.strftime("%Y%m%d%H%M%S", time.localtime()))
    # print time.strftime("%H", time.localtime())
    # print time.strftime("%Y-%m-%d", time.localtime())
    # print type(time.strftime("%Y-%m-%d", time.localtime()))
    # mywebdriver()
    # r=requests.session()
    # print getimgurl("D:/work/pic/4.png")
    # url='http://img1.egou.com/upload.php?s=brand'
    print 111111111111111111
    # l.CommonLog('ssssssssssssss')
    actpic()
    # creativepic()

    # print res.json()
    # r=requests.session()
    # url='https://apidemand.adhudong.com/upload.htm'
    # # data={"data":open("D:/work/pic/2.png",'rb')}
    # # files={"uploadFile":("3.png",open(r"D:/work/pic/4.png","rb"),"image/png"), "dict":(None,"2")}
    # # files={"uploadFile":("3.png",open('D:/auto/pic/1/28878_2019_10_31_20_29_31.png',"rb"),"image/png"), "dict":(None,"2")}
    # # files={"uploadFile":("3.png",open('D:/auto/pic/1/29378_2019_10_31_20_31_12.png',"rb"),"image/png"), "dict":(None,"2")}
    # # re=r.post(url,files=files)
    # # imageurl=str(json.loads(re.json())['data'])
    # r.get('https://display.intdmp.com/site_login_ijf.htm?app_key=adhu21fab394150d4e95')
    # re=r.get('https://display.intdmp.com/new/turntable_double.html?logId=B0H2YDC01JPO44JW9T&adzoneId=5177&actId=801&ref=&mediaId=2&ctm_code=Mi8vODQwLy8yLy8yLy8yNDAzMC8vMTU2NjgxOTM4MDEyMy8vYmNmZDliMmQ1NWY1M2M2NzNmZDZjNDFkZTk3OTcyMjcvLzQwMTkxYTgyNjM4Mg==&isIntercept=1')
    # print re.status_code

    # getcreativeid()
    # croppic()
    # getacturl()
    print 2222222222222222222
    print 1
