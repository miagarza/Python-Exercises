
def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   if n<=1:
      return 1
   else:
      return n + addToN(n-1)
   """ Return the sum of the non-negative integers to n.
   E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5 """



def findSumOfDigits( n ):
   """ Given a list of numbers, return the sum. """
   if n == 0:
      return 0
   else:
      return n + sumItemsInList( n-1 )


    
def testcode():
   sumItemsInList([1,2,3,4])
   countOccurrencesInList( "a", ["banana"] )

   #addToN( 10 )
   #addToN( 100 )

#testcode()

