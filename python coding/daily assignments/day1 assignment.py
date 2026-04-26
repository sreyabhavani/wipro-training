'''#question 1-eligible or not

s=int(input('enter your age:'))
if(s>=18):
    print('you are eligible')
else:
    print('yor are not eligible')
'''



from math import factorial

'''# question 2-leap year or not
c=int(input('Enter a year:'))
if(c%4==0 and c%100!=0) or (c%400==0):
    print('Leap year')
else:
    print('Not a leap year')
'''

'''#question-3divisible by 5 or not
s=int(input('Enter a number:'))
if(s%5 == 0):
    print('number is divisible by 5')
else:
    print('number is not divisible by 5')
'''
'''#question 4-Vowel or consonant
char=input('Enter a letter:')
if 'aeiou' in char:
    print('vowel')
else:
    print('consonant')
'''

'''#question 5-password strong or weak
s=input('Enter your password:')
if len(s)>=8:
    print('Strong password')
else:
    print('Week password')
'''


'''#question 6-Grade using matchcase
grade=input('Enter grade (A,B,C,D,E,F):')
match grade:
   case 'A':
     print('Excellent')
   case 'B':
       Print('Good')
   case 'C':
       print('Average')
   case 'D':
       print('Below average')
   case 'E':
       print('Fail')
   case 'F':
       print('Invalid garde')
'''

'''#question 7 -Traffic light using match case
s=input('Enter your light:')
match s:
    case 'red':
        print('stop')
    case 'green':
        print('start')
    case 'yellow':
        print('wait')
    case _:
        print('Invalid colour')
'''

'''#question 8 - Caluculating factorial
s=int(input('Enter your number:'))
factorial=1
for i in range(1,s+1):
    factorial *=i
print('Factorial',factorial)
'''


'''#question 9 - even numbers from 1-20
for i in range(1,21):
  if i %2==0:
        print(i)
'''



'''#question 10-Countdown using loop
i=10
while i>=0:
    print(i)
    i-=1
'''


'''#question 11- Count vowels in string
word=input('Enter a string:')
vowels='aeiou'
count=0
for char in word.lower():
    if char in vowels:
        count+=1
print('num of vowels',count)
'''

'''#question 12-printing numbers
for i in range(1,11):
     if i==5:
         continue
     if i ==8:
         break
     print(i)
'''

