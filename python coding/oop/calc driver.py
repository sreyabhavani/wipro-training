

from oop.calculation import calculation

calculationobj = calculation()
print(calculationobj.add(10,5))
print(calculationobj.sub(10,5))
print(calculationobj.mul(10,5))
numbers = [10, 20, 30, 40]
count=len(numbers)
print(f'lenth:{count}')
try:
    res=calculationobj.fdiv(10,0)
    for i in range(0,count+1):
        print(numbers[i])

except IndexError:
    print('check the index')

except ZeroDivisionError:
    print('0 in denominator')
except:
    print('oops....')
else:
    print(res)
finally:
    print('Done!!')










