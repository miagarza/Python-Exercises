#print("tester")
#from math import sqrt
from math import sqrt
import math



def sum3Numbers (x, y, z):
    """Return the sum of the three parameters."""
    return x + y + z


def multiply3Numbers( x, y, z ):
    return(x*y*z)


def sumUpTo3Numbers(x, y=0, z=0):
    return (x+y+z)


def multiplyUpto3Numbers(x, y=1, z=1):
    return(x*y*z)


def printInOrder( x, y ):
    if y<x:
        print(y,x)
    elif x<y or x==y:
        print(x,y)


def areaOfSquare(side):
    if side>0:
        return side**2
    if side<0:
        print("Side cannot be negative. Try another number")

    
def perimeterOfFigure( k, side ):
    if k<0 or side<0:
        print("Side cannot be negative. Try another number")
        return
    else:
        return k*side 
    
def diagonalOfRectangle( h, w ):
    if h<0 or w<0:
        print("Side cannot be negative. Try another number")
        return
    else:
        h=h**2
        w=w**2
        return sqrt(h+w)


def areaOfCircle( radius ):
    if radius<0:
        print("Side cannot be negative. Try another number")
        return
    else:
        return math.pi * radius**2


def circumferenceOfCircle( radius ):
    if radius<0:
        print("Side cannot be negative. Try another number")
        return
    else:
        return 2 * math.pi * radius


def bothFactors( d1, d2, x ):
    if x%d1==0 and x%d2==0:
        return True
    else:
        return False

def squareAndCircle( x ):
    print()
    print("Circle with radius", x, "has: \n"\
          " Area:", areaOfCircle(x), "\n" \
          " Circumference:", circumferenceOfCircle(x), "\n" \
          "Square with side", x, "has:\n"
          " Area:", areaOfSquare(x), "\n" \
          " Perimeter:", perimeterOfFigure(x), \
          )
    print()

    
def factorial(n):
    #print=int(input("whats n: "))
    """

    n=int(n)
    if n<0:
        print("Sinde cannot be negative. Try another number")
        return None
    else:
        for i in n:
            n=n(n-1)
        print(n)
    """
    for i in n:
        n=n(n-1)
    print(n)




def numberLength(n):
    n=int(n)
    for i in range(n):
        print(n)
    







def sumPositiveNumbers():
    sum=0
    numbers=int(input("Enter a number: "))
    while numbers>0 or numbers<0 or numbers==0:
        if numbers==0:
            print(sum)
            break
        if numbers<0:
            print("Illegal input. ")
        if numbers>0: 
            sum+=numbers
        numbers=int(input("Enter a number: "))
    

""" 
def sumSeries(n):
    n=int(n)
    #while n<1:
    for i in range(n):
        a=n-1
        a+=a*(n)

    print(a)
"""

def sumSeries(n):
    total=0
    for i in range(n):
        total+=(i*(i+1))
    print(total)



def isPrime(num):
    """ Test whether num is prime . """
    # Deal with evens and numbers < 2.

    if ( num < 2 or num % 2 == 0 ):
        print("got to here 1")
        return ( num == 2 )     

    # See if there are any odd divisors
    # up to the square root of num.
    divisor = 3

    while ( divisor <= math . sqrt ( num )):
        if ( num % divisor == 0 ) :
            print("got to here 2")
            return False
        else :
            divisor += 2
            print("got to here 3")
    print("got to here 4")
    return True



"""
def seriesSum(n):
    total = 0
    for i in range(1, n):
        total += i * (i + 1)
    return total
"""


"""
sum3Numbers()
multiply3Numbers()
sumUpTo3Numbers()
multiplyUpto3Numbers()
printInOrder()
areaOfSquare()
perimeterOfFigure()
diagonalOfRectangle()
areaOfCircle()
circumferenceOfCircle()
bothFactors()
squareAndCircle()
factorial(5)
numberLength(8)
sumPositiveNumbers()
"""

"""
#sumSeries(100)

#sumPositiveNumbers()
isPrime(4)
isPrime(3)
isPrime(12)
"""

numberLength(5)