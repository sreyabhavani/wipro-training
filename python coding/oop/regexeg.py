'import re'

'''#beg & end program
txt=(input('Enter a text:')) #india is my country
bpat =input('Enter behinning  pattern:')#India
epat=input('Enter ending pattern:')#India
bpat='^'+bpat
epat=epat+'$'

if re.search(pattern=bpat,string=txt):
    print('Beginning pat found')
else:
    print('Beginning not avaialble')
if re.search(pattern=epat,string=txt):
    print('ending pat found')
else:
    print('ending pat not found')
'''

'''#digit
mbno=(input('Enter a text:'))
pat= r"\d"

if re.fullmatch(pattern=pat,string=mbno):
    print('only digits')
else:
    print('only char found')
'''

'''#username
username=(input('Enter a UN:'))
pat=r"^[a-z]_{8,}$"
if re.match(pattern=pat,string=username):
    print('valid')
else:
    print('Invalid')
'''

#email
'''
emailadd=input('emai:')
pat=r"^[a-z-Z0-9_]+X@[a-z]+\.[a-z]+$"
if re.match(pattern=pat,string=emailadd):
    print('Valid')
else:
    print('Invalid')
'''

#password
pass=input('password:')
pat=r"^(?=.*[A-z])(?=[a-z])(?=[0-9])(?=[_?@_-]){8,}$"
if re.match(pattern=pat,string=pass):
    print('Valid')
else:
    print('Invalid')
