def areaofcircle(rad):
    return 3.14*rad*rad

def perimeterofcircle(rad):
    return 2*3.14

radius=int(input('enter radius'))


print('area: ',areaofcircle(rad=radius))
print('peri: ',perimeterofcircle(rad=radius))

si=int(input('enter side of sq'))
print('area: ',areaofsquare(side=si))
print('peri: ',perimeterofsquare(side=si))

l=int(input('enter length'))
b=int
print('area:  ',areaofrect(l,b))
