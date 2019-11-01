#encoding:utf-8

"Combine tests for gnosis.xml.objectify package (req 2.3+)"

import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("test_case")
import unittest, doctest
#这里需要导入测试文件

import HTMLTestRunner
import allcase_list
import Emar_SendMail_Attachments
import requests
#将用例组建成数组
alltestnames = allcase_list.caselistcreative()

suite = unittest.TestSuite()

if __name__ == '__main__':
	# 这里我们可以使用defaultTestLoader.loadTestsFromNames(),
	# 但如果不提供一个良好的错误消息时，它无法加载测试
	# 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
	for test in alltestnames:
		try:
			#最关键的就是这一句，循环执行数 据行中的用例。
			suite.addTest(unittest.TestLoader().loadTestsFromName(test))
			# suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
		except Exception:
			print 'ERROR: Skipping tests from "%s".' %test
			try:
				__import__(test)
			except ImportError:
				print 'Could not import the test moudle.'
			else:
				print 'Could not load the test suite.'
			from traceback import print_exc
			print_exc()
	print
	print 'Runnint the tests...'
# suite = doctest.DocTestSuite()
# suite.addTest(unittest.makeSuite(demotest.Test))
# suite.addTest(unittest.makeSuite(test_Cridetcard.Testcard))
	t = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
	# repopath='C:/auto/Voyageractivity_production_actactive/report'
	repopath='D:/work/auto/Voyager/report'
	filename = repopath+'/Report%s.html' %(t)
	fp = file(filename, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title='Report_title',
		description='Report_description')
	myresult=runner.run(suite)
	fp.close()
	# print myresult.__dict__
	# print myresult.success_count
	# print myresult.failure_count
	# print myresult.error_count
	# print myresult._previousTestClass
	# tmp=str(myresult._previousTestClass)[8:]
	# print tmp.replace('\'>','')
	if (myresult.failure_count>0):
		r=requests.session()
		url="http://open.adhudong.com/addPageMonitor.htm"
		# if (1>0):
		for i in myresult.result:
			errormsg=[]
			errormsg.append(i[2])
			# 测试结果构建了一个数组，分别存贮这广告主id,创意id等等d
			tmplist=i[2].split('\n')[1].split(",")
			# url="http://open.adhudong.com/addPageMonitor.htm"
			# case运行结果是失败 TestCase名字中包含creative
			if (i[0]==1 and 'creative' in i[1]._testMethodName ) :
				para={"type":"3","advertiserId":tmplist[0],"adCreativeId":tmplist[2],"adOrderId":tmplist[1],"url":tmplist[3],"httpcode":tmplist[4],"imageUrl":""}
				res=r.get(url,params=para)
				print res.text
				print errormsg
			if (i[0]==1 and 'act' in i[1]._testMethodName ) :
				# 活动http检测
				para={"type":"4","actId":tmplist[0],"url":tmplist[2],"httpcode":tmplist[3]}
				res=r.get(url,params=para)
				print res.text
				print errormsg
		sendfilename=repopath+'/Report%s.html'%t
		to_list=['dengjinyi@emar.com','zhaojing@emar.com']
		# to_list=['dengjinyi@emar.com','zhaoyu1@emar.com','xujingjing@emar.com','mahui@emar.com','sunli@emar.com','liuyujing@emar.com','wangyouju@emar.com']
		# Emar_SendMail_Attachments.sendTestreport(sendfilename,to_list,'检测创意链接是否正常','测试报告')
		Emar_SendMail_Attachments.sendTestreport(sendfilename,to_list,'生产环境检测创意活动链接是否正常','测试报告')
































