Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
id(s1)
2164408989904
list1=[1,2,3,4,5,6]
list1
[1, 2, 3, 4, 5, 6]
type(list1)
<class 'list'>
list1[2]
3
list[-2]
list[-2]
list[-1]
list[-1]
list1[-1]
6
s1
'hello'
list2=list(s1)
list2
['h', 'e', 'l', 'l', 'o']
list3=list1
list3
[1, 2, 3, 4, 5, 6]
id(list1)
2164367477696
2164367477696
2164367477696

list4=[100,'hello']
list4'
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> list4
[100, 'hello']
>>> list2.append(hey)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list2.append(hey)
NameError: name 'hey' is not defined. Did you mean: 'hex'?
>>> list1.append(hi)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list1.append(hi)
NameError: name 'hi' is not defined
>>> tuple1=(11,2,3,44,55)
>>> tuple1
(11, 2, 3, 44, 55)
>>> tuple[2]
tuple[2]
>>> tuple1[3]
44
>>> tuple1.index(3)
2
>>> tuple.count(2)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    tuple.count(2)
TypeError: descriptor 'count' for 'tuple' objects doesn't apply to a 'int' object
>>> tuple1.count(44)
1
>>> set1={10,20,30,40,
>>> set1
{50, 20, 40, 10, 30}


          
