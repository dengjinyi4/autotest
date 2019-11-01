# encoding:utf-8
import unittest
from parameterized import  parameterized
import myparamtest
import creative
class uncreative(myparamtest.ParametrizedTestCase):
# class uncreative(unittest.TestCase):

    @parameterized.expand(creative.getcreativehttpcode())
    def test_check_creative(self,advertisername,orderid,advertiserid,creaveid,url,str_val,expected):
        print  'advername:{0}, order id{1},adverid{2},activeid为{3},activeurl:{4} 打开报错，请相关同事检查链接是否能正常打开'.format(advertisername,orderid,advertiserid,creaveid,url)
        print  '{0},{1},{2},{3},{4}'.format(advertiserid,orderid,creaveid,url,str_val)
        self.assertEqual(str_val,expected)
    @parameterized.expand(creative.getacthttpcode())
    def test_check_act(self,actid,acturl,actname,str_val,expected):
        print  'act id:{0}, actname{1},url{2} 打开报错，请相关同事检查链接是否能正常打开'.format(actid,actname,acturl)
        print  '{0},{1},{2},{3}'.format(actid,actname,acturl,str_val)
        self.assertEqual(str_val,expected)
if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(uncreative('testapi2'))
    # # suite.addTest(myparamtest.ParametrizedTestCase.parametrize(TestAdd, param=1023))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
