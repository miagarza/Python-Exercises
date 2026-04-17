n=[1,2,3,4,5]
a=12345

b=[6,7,8,9,11]
c=678911

sum=0
for i in n:
    sum=sum+i
    

sum1=0
for i in b:
    sum1=sum1+i

"""
print(sum)
print(a*a)
print((a%10)*3)
print(a//10)

print()

print(sum1)
print(c*c)
print(c%10)
print(c//10)
"""

def OfindSumOfDigits( n ):
    if n == 0:
        return 0
    else:
        return OfindSumOfDigits(n//10)+ OfindSumOfDigits(n%10)

#findSumOfDigits( 12345 )

"""
k=[1,2,3,4,5]
k2=12345
#print(k)

total=0
for i in k:
    total=total+i


all=0
for i in k2:
    ig=(i//10)+(i%10)
    all=all+ ig

print(total)
#print((k2//10)+(k2%10))
print(all)
"""

"""
g=12345
#print(g//10)
#print(g%10)


def findSumOfDigits( n ):
   if n <= 1:
      return 0
   else:
      return n%10

"""

"""
a=25
print(a//10)
print(a%10)

print(a//2)
print(a%2)
"""


def integerToBinary( n ):
    if n == 0:
        return "0"
    else:
        return integerToBinary(n//2)+ str(n%2)
    





"""
def integerToList( n ):
    if n==0:
        return [n]
    else:
        return [n]+integerToList((((n//10)+n%10)-1))
"""

"""
def integerToList( n ):
    if n<=0:
        return [n]
    else:
        return integerToList((((n//10)+n%10)-1))+ [n]
    
"""

"""

def integerToList( n ):
    if n<=0:
        print([str(0)])
    else:
        print(integerToList(n//10), n%10)
    
"""



#1205
def integerToList( n ):
    if n<=0:
        print([str(0)])
    else:
        print(integerToList(n//10), n%10)
    

print("here")
integerToList(0)
integerToList(123)