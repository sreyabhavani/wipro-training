'''import pytest
from src.dailyassignment import sum,uppercase,number_list,square,div

#basic test function
def test_sum():
    res=sum(3,5)
    assert res==8,"Sum Error"

#assertion failures
def test_uppercase_fail():
    assert "hello".upper()=="hello"


#Fixture usage

def test_list_length(number_list):
    assert len(number_list)==3

#parameterized test

@pytest.mark.parametrize("input,expval",
                         [(2,4),(3,9),(4,16)])
def test_square(input,expval):
    assert square(input)==expval

#exception handling

def test_div():
    with pytest.raises(ZeroDivisionError):
         res=div(10, 0)
         assert res==
'''


