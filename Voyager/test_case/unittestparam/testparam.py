import unittest,hdtapi
# from nose_parameterized import parameterized, param
# import parameterized
from parameterized import  parameterized,param
# def custom_name_func(testcase_func, param_num, param):
#     x=parameterized.to_safe_name("_".join(str(x) for x in param.args))
#
#     # print 11111111
#     # print x
#     return "%s_%s" %(
#         testcase_func.__name__,
#         parameterized.to_safe_name(str(param.args[0])),
#     )
class TestAdd(unittest.TestCase):
    # mylist=[
    #     ("12", '12'),
    #     ("test", 'test'),
    #     ([1], [1]),
    #     ([2], [2])
    #     ("10", 16, base=16),
    # ]
    # mylist=hdtapi.getparam_excel()
    mylist=hdtapi.getparam_db()
    print type(mylist)
    @parameterized.expand(mylist)
    def test_int(self,casename,str_val, expected,type):
        print 111111111111111
        print str(casename)
        if str(type)=='A':
            print 22222222222222222
            print str_val
            print expected
            self.assertEqual(str(str_val),str(expected))
        else:
            print 333333333333333333333
            self.assertTrue(str_val>expected)
        # self.assertEqual(int(str_val, base), expected)
if __name__ == '__main__':
    unittest.main()