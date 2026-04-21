Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=8
y=9
type(x)
<class 'int'>
type(y)
<class 'int'>
x=9.89
type(x)
<class 'float'>
q="a"
type(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
q="a"
q
'a'
type(q)
<class 'str'>
s1='hello shreya'
s1
'hello shreya'
type(s1)
<class 'str'>
s2="'shreya"'
SyntaxError: unterminated string literal (detected at line 1)
s2="""shreya"""
s2
'shreya'
type(s2)
<class 'str'>

type(s2)
<class 'str'>
v1=4+j8
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    v1=4+j8
NameError: name 'j8' is not defined
v2=4+9j
v2
(4+9j)
type(v2)
<class 'complex'>
n=3
m=9
n+3
6
n+m
12
n-m
-6
n*m
27
n**m
19683
n/m
0.3333333333333333
n//m
0
n%m
3
10.5//3
3.0
b-=9
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b-=9
NameError: name 'b' is not defined
b=9
b-=9
b
0
5>8
False
7<9
True
u=8
h=8
u==h
True
u<h
False
u$h
SyntaxError: invalid syntax
u and h
8
u or h
8
8 and 9
9
9 or 8
9
8 or 9
8
>>> u>h and u>h
False
>>> u>h and u<h
False
>>> not u
False
>>> not h
False
>>> v=-7
>>> not v
False
>>> y=0
>>> not y
True
>>> s1=
SyntaxError: invalid syntax
>>> s1=
SyntaxError: invalid syntax
>>> s1="
SyntaxError: unterminated string literal (detected at line 1)
>>> not s1
False
>>> s1='
SyntaxError: unterminated string literal (detected at line 1)
>>> b1="
SyntaxError: unterminated string literal (detected at line 1)
>>> s=None
>>> s
>>> type(s)


<class 'NoneType'>


a=40
b=a
c=a+b
type(c)
a=9
b=0
a+b
