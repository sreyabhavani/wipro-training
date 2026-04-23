def areaofsquare(side):
    return side*side

def perimeterofsquare(side):
    return 4*side

def areaofrect(l,b):
    return l*b

si=int(input('enter side of sq'))
print('area: ',areaofsquare(side=si))
print('peri: ',perimeterofsquare(side=si))

l=int(input('enter length'))
b=int(input('enter breadth'))
print('area:  ',areaofrect(l,b))
