Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
>>> s1.capitalize()
'Hello'
>>> s1.upper()
'HELLO'
>>> s1.lower()
'hello'
>>> s1='hEllo'
>>> s1.casefold()
'hello'
>>> s2='SHREYA'
>>> s2.caseflod()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s2.caseflod()
AttributeError: 'str' object has no attribute 'caseflod'. Did you mean: 'casefold'?
>>> s2.casefold()
'shreya'
>>> s2.count(e)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s2.count(e)
NameError: name 'e' is not defined
>>> s2.count('e')
0
>>> s
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 's1'?
>>> File "<pyshell#14>", line 1, in <module>
SyntaxError: invalid syntax
>>>s
>>> 
>>> 
