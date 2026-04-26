import my_math.arthmetic  as ar
import my_math.geometry as geo

def main():
    print('==My math pakage==')

    x=float(input('Enter first number:'))
    y=float(input('Enter second number:'))


    #arithmetic operations
    print('\nArithmetic:')
    print('Addition:',ar.add(x,y))
    print('Subtraction:',ar.subtract(x,y))
    print('Multiplication:',ar.multiply(x,y))
    print('Division:',ar.divide(x,y))
    #geometry input
    r=float(input('\nEnter radius of circle:'))
    l=float(input('Enter length of rectangle:'))
    w=float(input('Enter  width  of rectangle:'))
     #geometry operations
    print('\ngeometry:')
    print('Area of circle:',geo.area_circle(r))
    print('Area of rectangle:',geo.area_rectangle(l,w))








