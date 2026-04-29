#function with type error
'''def add(a,b):
    try:
        return a+b
    except TypeError:
        print('Error:only num allowed')
print(add(10,20))
print(add('a',5))
'''

while True:
    try:
        num=int(input('Enter integer:'))
        print('Vlaid number:',num)
        break
    except ValueError:
        print('Invalid input,try again')