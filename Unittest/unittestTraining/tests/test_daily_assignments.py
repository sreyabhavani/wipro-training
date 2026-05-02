import unittest


#Basic Test Case
class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2+3,5)
#setup  and Teardown
class TestList(unittest.TestCase):
    def setUp(self):
        self.my_list=[1,2,3]

    def  tearDown(self):
        print('Test completed')
    def test_list(self):
        self.assertEqual(len(self.my_list),3

#Multiple Assertions
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(),'HELLO')
    def test_isupper(self):
        self.assertFalse('hello'.isupper())

#Excepion Testing
class TestExceptions(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            result = 10/0

#Test suite Execution
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3+5,8)

class TestSubtract(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(5-3,2)

if __name__=="__main__":
    suite=unittest.TestCase()
    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))
    runner=unittest.TextTestRunner()
    runner.run(suite)


