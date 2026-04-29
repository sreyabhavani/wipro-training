import re
'''
#password
password = input('password:')
pat=r"^(?=.*[A-z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]){8,}$"
if re.match(pattern=pat,string=password):
    print('Valid')
else:
    print('Invalid')
'''

txt=input('text:')
pat=r"\s+"
print(re.split(pattern=pat,string=txt))