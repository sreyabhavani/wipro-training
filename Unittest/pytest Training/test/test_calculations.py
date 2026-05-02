'''import pytest
from src.calculations import Calculations

class TestCalculations:
    calc = Calculations()

    @pytest.fixture(scope='module',autouse=True)
    def setup(self):
        print('Fixture')


    @pytest.mark.parametrize("n1,n2,exval",[
                                 (5,5,10),(-5,-5,-10),(0,5,5)])


    def test_add(self,n1,n2,exval):
        res=self.calc.add(10,5)
        assert res==15,'Addition Err'


    @pytest.mark.parametrize("n1,n2,exval",[
                                 (5,5,0),(-5,-5,0),(0,5,-5)])

    def test_sub(self,n1,n2,exval):
        res=self.calc.sub(10,5)
        assert res==5,'Subtraction Err'

    def test_mul(self):
        res=self.calc.mul(10,5)
        assert res==50,'Multiplication Err'

    def test_div(self):
        res=self.calc.div(10,5)
        assert res==2.0,'Division Err'

    @pytest.mark.skip(reason='NIY')
    def test_ne(self):
        res=self.calc.ne(10,10)
        assert res==True, 'Not Equal'

    @pytest.mark.xfail(reason='NDY')
    def test_diverr(self):
        #with pytest.raises(ZeroDivisionError)
        res=self.calc.div(10,0)
        assert res==0
'''

