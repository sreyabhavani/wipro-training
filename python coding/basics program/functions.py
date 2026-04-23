'''#functions
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div():
    pass

#driver
a=int(input('enter first number'))
b=int(input('enter second number'))
res=add(a,b)
print('add:',res)
res=sub(a,b)
print('sub:',res)
res=mul(a,b)
print('mul:',res)
'''

'''#arbitary
def add(nums):
    sum=0
    for n in nums:
        sum+=n
    return sum



numbers=list()
count=int(input('how many ?'))
for _ in range(1+count+1):
    numbers.append(int(input('no: ')))
'''
#lambdas
a=int(input('enter first number'))
b=int(input('enter second number'))
add=lambda n1,n2:n1+n2
print(add(a,b))