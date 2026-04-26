'''#largest and smallest
n=list(map(int,input('enter numbers:').split()))
print('largest number:',max(n))
print('shortest number:',min(n))
'''
'''#finding len of string
s=input('enter a string:')
print(len(s))
'''
'''#printing in alphabetical order
names=input('enter names :').split()
names.sort()
print('names in alphabetical order:',names)
'''
'''#sum of elements in the list
s=list(map(int,input('enter the numbers:').split()))
print('sum of numbers:',sum(s))
'''
'''#string into uppercase
s=input('Enter your string:')
s=s.upper()
print('uppercase:',s)
'''

'''# factorial function
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

n=int(input('Enter a number:'))
print('factorial:',factorial(n))
'''
#import math
#import random

'''#find the largest of 3 num
def find_largest(a,b,c):
    return max(a,b,c)
a,b,c=map(int,input('enter 3 numbers:').split())
print('largest numbers:',find_largest(a,b,c))
'''

'''#printing greet name
def greet(name):
    print('Hello,',name)
name=input('Enter your name:')
greet(name)
'''

'''#average of list
def average(numbers):
    return sum(numbers)/len(numbers)
l=list(map(int,input('enter numbers:').split()))
print('average:',average(l))
'''

'''#palindrome or not
def is_palindome(n):
    return n==n[::-1]

s=input('Enter a string:')
if is_palindome(s):
    print('It is palindrome')
else:
    print('It is not a palindrome')
'''

'''#math module

n=int(input('Enter a number:'))
print('square root:',math.sqrt(n))

s=float(input('Enter a number:'))
print('sine angle:',math.sin(s))

a,b=map(int,input('enter two numbers:').split())
print('gcd:',math.gcd(a,b))
'''

#import random

'''print('Random numbers:',random.randint(1,100))

#list of random numbers
l=[random.randint(1,100)for _ in range(6)]
print('random list:',l)

#shuffled list
num=[1,2,8,7,9]
random.shuffle(num)
print('shuffled list:',num)
'''
'''#datetime module
from datetime import datetime
now=datetime.now()
print(now)

# days between two dates
n1=datetime(2019,1,3)
n2=datetime(2026,4,3)
difference=n2-n1
print('days between 2 dates:',difference)

#format date
formatted_date=now.strftime('%d-%m-%y')
print('formatted date:',formatted_date)
'''

'''#os modules
import os
#printing current directory
print('current directory:',os.getcwd())

#creating a new directory
folder_name='test_directory'
os.makedirs(folder_name,exist_ok=True)

#verify existence
print('Directory exists:',os.path.exists(folder_name))

#list files and directories
print('Files and directories:')
print(os.listdir())
'''

#arthmetic.py
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    return 'cannot divide by zero'
#geometry.py
import math
def area_circle(r):
    return math.pi*r*r
def area_rectangle(l,w):
    return l*w

#main.py
import my_math.arithmetic as ar
import my_math.geometry as geo
def main():
    print('==My math pakage==')
    x=float(input('Enter first number:'))
    y=float(input('Enter second number:'))
    #arithmetic operations
    print('\nArithmetic:')
    print('Addition:',ar.add(x,y))
    print('Subtraction:',ar.subtract(x,y))
    print('Multiplication:',ar.multiply(x,y))
    print('Division:',ar.divide(x,y))
    #geometry input
    r=float(input('\nEnter radius of circle:'))
    l=float(input('Enter length of rectangle:'))
    w=float(input('Enter  width  of rectangle:'))
     #geometry operations
    print('\ngeometry:')
    print('Area of circle:',geo.area_circle(r))
    print('Area of rectangle:',geo.area_rectangle(l,w))
#driver.py
from main import main
if __name__=='__main__':
    main()


output:
==My math pakage==
Enter first number:23
Enter second number:45

Arithmetic:
Addition: 68.0
Subtraction: -22.0
Multiplication: 1035.0
Division: 0.5111111111111111

Enter radius of circle:34
Enter length of rectangle:3
Enter  width  of rectangle:4

geometry:
Area of circle: 3631.6811075498013
Area of rectangle: 12.0
