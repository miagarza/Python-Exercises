#recursion





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
   """ Return the sum of the non-negative integers to n.
   E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5 """

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. 
   E.g., findSumOfDigits( 1234 ) = 10 """

def integerToBinary( n ):
   """ Given a nonnegative integer n, return the 
   binary representation as a string. E.g., 
   integerToBinary( 10 ) = '1010' """

def integerToList( n ):
   """ Given a nonnegative integer, return a list of the 
   digits (as strings). 
   E.g., integerToList( 123 ) = ['1', '2', '3'] """

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome.
   Case counts: 'abA' is not a palindrome. """

def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any. Return None if there
   is none. """

# for this one, don't reverse the string.
def findLastUppercase( s ):
   """ Return the last uppercase letter in 
   string s, if any. Return None if there
   is none. """

def negateItems( lst ):
   """Assume lst is a list of numbers.  Return a list
   of the negations of those numbers."""

def findLargest( lst ):
   """Assume lst is a list of numbers. Recursively find
   and return the largest element."""

# This one is designed to see if you can think recursively on more
# "real world" problems.  Assume the dictionary d you pass in has
# 25, 10, 5, 1 as keys associated with integer values. It might be
# called like this:
#
# >>> dInit = {25: 0, 10: 0, 5: 0, 1: 0}
# >>> print( makeChange( dInit, 142 ) ) 
# {25: 5, 10: 1, 5: 1, 1: 2}

def makeChange( d, cash ):
   """Given coins with values of 25, 10, 5, 1, return a 
   dictionary that associates a count with each coin so that
   the total added matches cash and you added the minimum total
   number of coins.  You might assume that in the top-leval call of 
   makeChange d has value {25: 0, 10: 0, 5: 0, 1: 0}, but there's
   nothing that guarantees that."""

# I posted a short video on the class webpage explaining 
# helper functions.  If you're stuck on this one, view
# that video and see if it helps.

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the offset of the first uppercase letter;
   assume you are starting at index. Return -1 
   if there is none."""

# The following function is already completed for you. But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any. Return -1 if there is none. This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )
