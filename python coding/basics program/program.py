"""
Date :22-4-2026
desc: learning various if stmt formats
"""
#program
'''
num1= int(input('Enter a number'))
num2=int(input('Enter second number'))

if num1==num2:
    print('both are equal')
if num1 > num2:
    print(num1, 'is big')
else:
    print(num2,'is big')
'''

'''#big
num1= int(input('Enter a number'))
num2=int(input('Enter second number'))
num3=int(input('Enter third number'))

if num1==num2 and num2==num3:
    print('All values are equal')
elif num1>num2 and num1>num3:
    print(num1,'num2 is biggest')
elif num2>num1 and num2>num3:
    print(num2,'num1 is biggest')
elif num3>num2 and num3>num1:
    print(num3,'num3 is biggest')

'''
#weekday
s1=int(input('Enter a number between 1-7'))
match s1:
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')
    case _:
        print('Invalid choice')