import unittest,hdtapi
# from nose_parameterized import parameterized, param
# import parameterized
from parameterized import  parameterized,param

def custom_name_func(testcase_func, param_num, param):
    x=parameterized.to_safe_name("_".join(str(x) for x in param.args))

    print 11111111
    print x
    return "%s_%s" %(
        testcase_func.__name__,
        parameterized.to_safe_name(str(param.args[-1])),
    )

class TestAdd(unittest.TestCase):
    # mylist=[
    #     param("12", '12'),
    #     param("test", 'test'),
    #     param([1], [1]),
    #     param([2], [2])
    #     # param("10", 16, base=16),
    # ]
    mylist=hdtapi.getparam_excel()
    print type(mylist)
    @parameterized.expand(mylist,testcase_func_name=custom_name_func)
    def test_int(self, str_val, expected,type,casename):
        if str(type)=='A':
            self.assertEqual(str(str_val),str(expected))
        else:
            self.assertTrue(str_val>expected)
        # self.assertEqual(int(str_val, base), expected)
if __name__ == '__main__':
    unittest.main()