
 #natural numbers

'''c=int(input('Enter  a number'))

value = 1
while value <= c:
    print(value)
    value+=1
'''


s=(input('Enter a number'))
count=len(s)
sum=0

ni=int(s)
comp =ni
while ni > 0:
    rem=ni%10
    sum=sum+rem**count
    ni=ni//10
if comp==sum:
    print('arm')
else:
    print('na')



