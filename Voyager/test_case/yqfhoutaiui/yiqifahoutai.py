#!/usr/bin/env python
# encoding: utf-8
# coding=gbk
import os,time,datetime,re
import mydriverpath
from selenium import webdriver
from selenium.webdriver.support.select import Select
def yesterday():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=7)
    print type(yesterday)
    return yesterday
def getweek():
    d = datetime.datetime.now()
    dayscount = datetime.timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = datetime.timedelta(days=6)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    # date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    # date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
    # return str(date_from)[0:10],str(date_to)[0:10]
    return date_from
# 返回一个距离当前日期days天前的一个j天数组
def getweeknew(days,j):
    d = datetime.datetime.now()
    dayscount = datetime.timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = datetime.timedelta(days=days)
    dayfrom = dayto - sixdays
    date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    tmplist=[]
    for i in range(0,j,1):
        tmpdate_from=date_from+datetime.timedelta(days=i)
        tmplist.append(str(tmpdate_from)[0:10])
        print tmplist[i]
    return tmplist
# 返回一个距离当前日期days天前的一个j天数组
def getweeknew1(days,j):
    date_from = datetime.datetime.now()
    tmplist=[]
    for i in range(1,j,1):
        tmpdate_from=date_from+datetime.timedelta(days=-i)
        tmplist.append(str(tmpdate_from)[0:10])
        print tmplist
    return tmplist
def mywebdriver():
    chromedriver = mydriverpath.drvierpath()
    # chromedriver = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver =  webdriver.Chrome(chromedriver)
    driver.get("http://221.122.127.226:19100/mgrLoginForm.do")
    driver.set_page_load_timeout(5)
    driver.find_element_by_id('userName').clear()
    driver.find_element_by_id('userName').send_keys('autocheck')
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('Emar2017')
    driver.find_element_by_id('loginbtn').click()
    return driver
# 验证订单数
def yqfcpsordershishihuizonggeshu(campaignId,elementname,days,j,costType,huizongxpath,mingxixpatch):
    driver=mywebdriver()
    driver.set_page_load_timeout(30)
    listweek=getweeknew(days,j)
    cpshuizonglist=[]
    cpsmingxilist=[]
    n=0
    for fr in listweek:
        try:
            driver.get('http://221.122.127.226:19100/mgrSimpleCpsReport.do')
            time.sleep(5)
            # 查找前一个自然周的数据,查询当天的时间
            endDatejs="$(\"input[name='endDate']\").removeAttr('readonly');$(\"input[name='endDate']\").attr('value','"+fr+"')"
            startDatejs="$(\"input[name='startDate']\").removeAttr('readonly');$(\"input[name='startDate']\").attr('value','"+fr+"')"
            driver.execute_script(startDatejs)
            driver.execute_script(endDatejs)
            driver.find_element_by_id('campaignId').clear()
            driver.find_element_by_id('campaignId').send_keys(campaignId)
            # 计费方式
            sel = driver.find_element_by_xpath(r'//*[@id="costType"]')
            if (costType=='cps'):
                Select(sel).select_by_value('cps')
            else:
                Select(sel).select_by_value('cpa')
            driver.find_element_by_name('Submit2').click()
            time.sleep(3)
            # cps汇总页面  收订订单额
            # cpshuizong=driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[10]').text
            cpshuizong=driver.find_element_by_xpath(huizongxpath).text
            driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[25]/a').click()
            time.sleep(2)
            n=n+1
            driver.switch_to_window(driver.window_handles[n])
            # CPS订单明细页面  收订订单额
            # 提交状态：
            seltijiaozhuangtai = driver.find_element_by_xpath(r'//*[@id="searchForm"]/table/tbody/tr/td/table[1]/tbody/tr[5]/td[4]/select')
            Select(seltijiaozhuangtai).select_by_value('已提交')
            # 明细页面查询
            driver.find_element_by_xpath('//*[@id="searchForm"]/table/tbody/tr/td/table[1]/tbody/tr[10]/td/input[2]')
            cpsmingxi=driver.find_element_by_xpath(mingxixpatch).text
            time.sleep(2)
        except Exception,e:
            print '\n访问url找不到指定的元素:%s'%e.message
        print(driver.current_url)
        # print '活动:%s，CPS订单实时汇总页面 收订订单额是:%sCPS订单明细页面 收订订单额是:%s'%(campaignId,cpshuizong,cpsmingxi)
        print '查询开始日期：',fr,'查询结束日期：',fr,'活动: ',campaignId,'\n汇总数据转换前 CPS订单实时汇总页面  计费方式按照： ',costType,'查询',elementname,'是:',cpshuizong,'\nCPS订单明细页面  ',elementname,'是:',cpsmingxi
        # 2,187 转换成 2187
        cpsmingxi=cpsmingxi.replace(',','')
        cpsmingxilist.append(cpsmingxi)
        cpshuizonglist.append(cpshuizong)
        chae=int(cpshuizong)-int(cpsmingxi)
        print '活动: ',campaignId,'\n汇总数据转换后 CPS订单实时汇总页面 ',elementname,'是:',cpshuizong,'CPS订单明细页面 计费方式按照： ',costType,'查询',elementname,'是:',cpsmingxi,'\n数据相差:',chae,'\n\n'
    driver.quit()
    return cpshuizonglist,cpsmingxilist
# 汇总实时收订订单比较
def yqfcpsordershishihuizong(campaignId,elementname,days,j,costType,huizongxpath,mingxixpatch):
    driver=mywebdriver()
    driver.set_page_load_timeout(30)
    # 获取一个时间段
    listweek=getweeknew(days,j)
    cpshuizonglist=[]
    cpsmingxilist=[]
    n=0
    for fr in listweek:
        try:
            driver.get('http://221.122.127.226:19100/mgrSimpleCpsReport.do')
            time.sleep(5)
            # 查找前一个自然周的数据,查询当天的时间
            endDatejs="$(\"input[name='endDate']\").removeAttr('readonly');$(\"input[name='endDate']\").attr('value','"+fr+"')"
            startDatejs="$(\"input[name='startDate']\").removeAttr('readonly');$(\"input[name='startDate']\").attr('value','"+fr+"')"
            driver.execute_script(startDatejs)
            driver.execute_script(endDatejs)
            driver.find_element_by_id('campaignId').clear()
            driver.find_element_by_id('campaignId').send_keys(campaignId)
            # 计费方式
            sel = driver.find_element_by_xpath(r'//*[@id="costType"]')
            if (costType=='cps'):
                Select(sel).select_by_value('cps')
            else:
                Select(sel).select_by_value('cpa')
            driver.find_element_by_name('Submit2').click()
            time.sleep(3)
            # cps汇总页面  收订订单额
            cpshuizong=driver.find_element_by_xpath(huizongxpath).text
            # 点击cps明细链接
            driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[1]/td[25]/a').click()
            time.sleep(2)
            # 窗口切换
            n=n+1
            driver.switch_to_window(driver.window_handles[n])
            # CPS订单明细页面  收订订单额
            cpsmingxi=driver.find_element_by_xpath(mingxixpatch).text
            time.sleep(2)
        except Exception,e:
            print '\n访问url找不到指定的元素:%s'%e.message
        print(driver.current_url)
        # print '活动:%s，CPS订单实时汇总页面 收订订单额是:%sCPS订单明细页面 收订订单额是:%s'%(campaignId,cpshuizong,cpsmingxi)
        print '查询开始日期：',fr,'查询结束日期：',fr,'活动: ',campaignId,'\n汇总数据转换前 CPS订单实时汇总页面 计费方式按照： ',costType,'查询',elementname,'是:',cpshuizong,'\nCPS订单明细页面  ',elementname,'是:',cpsmingxi
        # ￥2,355,303.07 转换成 2355303
        cpsmingxi=cpsmingxi[1:]
        cpsmingxi=cpsmingxi.split('.')[0]
        cpsmingxi=cpsmingxi.replace(',','')
        cpsmingxilist.append(cpsmingxi)
        # ￥2355303.30 转换成 2355303
        cpshuizong=cpshuizong[1:].split('.')[0]
        cpshuizonglist.append(cpshuizong)
        chae=int(cpshuizong)-int(cpsmingxi)
        print '活动: ',campaignId,'\n汇总数据转换后 CPS订单实时汇总页面 ',elementname,'是:',cpshuizong,'CPS订单明细页面 按照 ',costType,'查询',elementname,'是:',cpsmingxi,'\n数据相差:',chae,'\n\n'
    driver.quit()
    return cpshuizonglist,cpsmingxilist
# 虚假单对比
def yqfxjd(elementname,days,j,xujiadingdanxpath,xujiadanbiaoshixpatch):
    driver=mywebdriver()
    driver.set_page_load_timeout(30)
    listweek=getweeknew(days,j)
    cpshuizonglist=[]
    cpsmingxilist=[]
    for fr in listweek:
        try:
            driver.get('https://admin.yiqifa.com/mgrSimpleCpsReport.do')
            time.sleep(5)
            # 查找前一个自然周的数据,查询当天的时间
            endDatejs="$(\"input[name='endDate']\").removeAttr('readonly');$(\"input[name='endDate']\").attr('value','"+fr+"')"
            startDatejs="$(\"input[name='startDate']\").removeAttr('readonly');$(\"input[name='startDate']\").attr('value','"+fr+"')"
            driver.execute_script(startDatejs)
            driver.execute_script(endDatejs)
            # driver.find_element_by_id('campaignId').clear()
            # driver.find_element_by_id('campaignId').send_keys(campaignId)
            driver.find_element_by_name('Submit2').click()
            time.sleep(3)
            # cps汇总页面  收订订单额
            # cpshuizong=driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[10]').text
            cpshuizong=driver.find_element_by_xpath(xujiadingdanxpath).text
            # 虚假单标识页面
            driver.get('https://admin.yiqifa.com/mgrFalseCpsReport.do')
            xjdstartDatejs="$(\"input[name='startDate']\").removeAttr('readonly');$(\"input[name='startDate']\").attr('value','"+fr+"')"
            xjdendDatejs="$(\"input[name='endDate']\").removeAttr('readonly');$(\"input[name='endDate']\").attr('value','"+fr+"')"
            driver.execute_script(xjdstartDatejs)
            driver.execute_script(xjdendDatejs)
            sel = driver.find_element_by_xpath(r'//*[@id="SignFrame"]/tbody/tr[4]/td[2]/select')
            # 虚假单标识选择虚假单
            Select(sel).select_by_value('1')
            # 查询
            driver.find_element_by_xpath('//*[@id="SignFrame"]/tbody/tr[9]/td/input[1]').click()
            time.sleep(2)
            # 查看查询结果是多少页
            allcount=driver.find_element_by_xpath('/html/body/div/table[3]/tbody/tr/td/table/tbody/tr/td/div[3]').text
            print allcount
            tmp=getcount(allcount)
            print tmp
            print type(int(tmp))
            # 判断是否翻页
            if (int(tmp)>=20):
                # 虚假单标识页面，收订订单额
                cpsmingxi=driver.find_element_by_xpath(xujiadanbiaoshixpatch).text
            else:
                tmpcount=int(getcount(allcount))+2
                cpsmingxi=driver.find_element_by_xpath(replacestr_xujiadanbiaoshi(xujiadanbiaoshixpatch,str(tmpcount))).text
        except Exception,e:
            print '\n访问url找不到指定的元素:%s'%e.message
        print(driver.current_url)
        # print '活动:%s，CPS订单实时汇总页面 收订订单额是:%sCPS订单明细页面 收订订单额是:%s'%(campaignId,cpshuizong,cpsmingxi)
        print '查询开始日期：',fr,'查询结束日期：',fr,'\n汇总数据转换前 CPS订单实时汇总页面  ',elementname,'是:',cpshuizong,'虚假单标识页面  ',elementname,'是:',cpsmingxi
        # ￥2,355,303.07 转换成 2355303
        cpsmingxi=cpsmingxi[1:]
        cpsmingxi=cpsmingxi.split('.')[0]
        cpsmingxi=cpsmingxi.replace(',','')
        cpsmingxilist.append(cpsmingxi)
        # ￥2355303.30 转换成 2355303
        cpshuizong=cpshuizong[1:].split('.')[0]
        cpshuizonglist.append(cpshuizong)
        chae=int(cpshuizong)-int(cpsmingxi)
        print '\n汇总数据转换后 CPS订单实时汇总页面 ',elementname,'是:',cpshuizong,'虚假单标识页面 ',elementname,'是:',cpsmingxi,'\n数据相差:',chae,'\n\n'
    driver.quit()
    return cpshuizonglist,cpsmingxilist
# 对比传入的list值
def difflist(huizonglis,mingxilist):
    if(len(huizonglis)!=len(mingxilist)):
        print '传入的两个list长度不等'
        return False
    i=len(huizonglis)
    j=0
    for j in range(i):
        chae=abs(int(huizonglis[j])-int(mingxilist[j]))
        yushu=int(huizonglis[j])/1000
        print ' CPS订单实时汇总页面虚假单金额是:%s,虚假单标识页面金额是：%s 汇总和差额：%s,余数是：%s'%(str(huizonglis[j]),str(mingxilist[j]),str(chae),str(yushu))
        if(chae>yushu):
            print '与原数据相差超过千分之1'
            return False
    return True
# 对比传入的list值
def difflistcout(huizonglis,mingxilist):
    if(len(huizonglis)!=len(mingxilist)):
        print '传入的两个list长度不等'
        return False
    i=len(huizonglis)
    j=0
    for j in range(i):
        chae=abs(int(huizonglis[j])-int(mingxilist[j]))
        # yushu=int(huizonglis[j])/1000
        print ' CPS订单实时汇总页面虚假单金额是:%s,虚假单标识页面金额是：%s 汇总和差额：%s'%(str(huizonglis[j]),str(mingxilist[j]),str(chae))
        if(chae!=0):
            print '汇总个数是%s'%huizonglis[j]+'明细个数是：%s'%mingxilist[j]+'差额是：%s'%chae
            return False
    return True
# 从字符串 “结果共17项”字符串中中提取出页数
def getcount(str):
    pattern = re.compile(r'\d+')
    res = re.findall(pattern,str)
    return res[0]
# 替换 xpath中 的21 为新值(项+2) /html/body/center/div/table/tbody/tr[21]/td[14]
def replacestr_xujiadanbiaoshi(str,count):
    tmp=str.replace(str[33:35],count)
    return tmp
if __name__ == '__main__':
    (cpshuizong,cpsmingxi)=yqfcpsordershishihuizong(17222,'收订订单金额',7,6,'cps','/html/body/div[2]/table/tbody/tr[2]/td[10]','/html/body/center/div/table/tbody/tr[21]/td[14]')
    # (cpshuizong,cpsmingxi)=yqfcpsordershishihuizonggeshu(254,'收订订单数',4,3,'cps','/html/body/div[2]/table/tbody/tr[2]/td[5]','/html/body/center/div/table/tbody/tr[21]/td[13]')
    # (cpshuizong,cpsmingxi)=yqfxjd('虚假订单额',6,7,'/html/body/div[2]/table/tbody/tr[2]/td[12]','/html/body/div/table[2]/tbody/tr[22]/td[14]')
    # rrr=￥2263476.06
    # print cpsmingxi,cpshuizong
    # getweeknew(5,2)

