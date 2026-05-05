import os

import pytest

from src.test_logic import multiply, contains_pytest, get_sample_dict, get_element, is_even, create_temp_file


def test_math_operations():
    assert multiply(15,3)==45
    assert contains_pytest("learning pytest is fun")

#Fixture
@pytest.fixture
def sample_dict():
    return get_sample_dict()


def test_dict_keys(sample_dict):
    assert "role" in sample_dict
    assert sample_dict["name"]=="Alice"

def test_index_error():
    with pytest.raises(IndexError):
        get_element([1,2,3],10)

@pytest.mark.parametrize("num",[2,10,22])
def test_is_even(num):
    assert is_even(num)

def test_file_content():
    filename=create_temp_file()
    try:
        with open(filename,"r") as f:
            content=f.read()
        assert content=="Hello World"
        print("Test passed")
    finally:
        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted")
