import pytest
#Basic assertion
def multiply(a,b):
    return a*b

def contains_pytest(text):
    return "pytest" in text

#using ficture for setup
def get_sample_dict():
    return {
        "name":"Alice",
        "role":"Dev"
    }
#Exception function
def get_element(my_list,index):
    return my_list[index]

#Parameterized test
def is_even(num):
    return num % 2==0

#cleaning up with fixture yields
def create_temp_file():
    filename="text.txt"

    with open(filename,"w") as f:
        f.write("Hello World")
    return filename

