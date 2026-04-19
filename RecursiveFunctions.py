# File: RecursiveFunctions.py
# Student: Mia Garza
# UT EID: mkg2545
# Course Name: CS303E
# 
# Date: 4/11/26
# Description of Program: Variety of recursive functions



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
    if n<1:
        return 0
    else:
        return n + addToN(n-1)



def findSumOfDigits( n ):
    """ Return the sum of the digits in a non-negative integer. 
   E.g., findSumOfDigits( 1234 ) = 10 """
    if n == 0:
        return 0
    else:
        return findSumOfDigits(n//10)+ n%10


def integerToBinary( n ):
    """ Given a nonnegative integer n, return the 
   binary representation as a string. E.g., 
   integerToBinary( 10 ) = '1010' """
    if n == 0:
        return "0"
    if n==1:
        return "1"
    return integerToBinary(n//2)+ str(n%2)



def integerToList( n ):
    """ Given a nonnegative integer, return a list of the 
   digits (as strings). 
   E.g., integerToList( 123 ) = ['1', '2', '3'] """
    if n==0:
        return []
    else:
        return integerToList(n//10)+ [str(n%10)]



def isPalindrome( s ):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome.
    Case counts: 'abA' is not a palindrome. """
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return isPalindrome(s[1:-1])



def findFirstUppercase( s ):
    """ Return the first uppercase letter in 
   string s, if any. Return None if there
   is none. """
    if s=="":
        return None
    if 65<=ord(s[0])<=90:
        return s[0]
    return findFirstUppercase(s[1:])


def findLastUppercase( s ):
    """ Return the last uppercase letter in 
    string s, if any. Return None if there
    is none. """
    if s=="":
        return None
    if 65<=ord(s[-1])<=90:
        return s[-1]
    return findLastUppercase(s[:-1])
    


def negateItems( lst ):
    """Assume lst is a list of numbers.  Return a list
    of the negations of those numbers."""
    if lst==[]:
        return []
    return [lst[0]*-1]+ negateItems(lst[1:])



def findLargest( lst ):
    """Assume lst is a list of numbers. Recursively find
   and return the largest element."""
    if lst==[]:
        return None
    if len(lst)==1:
        return lst[0]
    largest=findLargest(lst[1:])
    if lst[0]>largest:
        return lst[0]
    return largest
    


def makeChange( d, cash ):
   
    """Given coins with values of 25, 10, 5, 1, return a 
    dictionary that associates a count with each coin so that
    the total added matches cash and you added the minimum total
    number of coins.  You might assume that in the top-leval call of 
    makeChange d has value {25: 0, 10: 0, 5: 0, 1: 0}, but there's
    nothing that guarantees that."""

    if cash==0:
        return d
    elif (cash/25)>=1:
        d[25]+=1
        return makeChange( d, cash-25 )
    elif (cash/10)>=1:
        d[10]+=1
        return makeChange( d, cash-10 )
    elif (cash/5)>=1:
        d[5]+=1
        return makeChange( d, cash-5 )
    elif (cash/1)>=1:
        d[1]+=1
        return makeChange( d, cash-1 )



def findFirstUppercaseIndexHelper( s, index ):
    """ Helper function for findFirstUppercaseIndex.
    Return the offset of the first uppercase letter;
    assume you are starting at index. Return -1 
    if there is none."""
    if s=="":
        return -1
    if 65<=ord(s[0])<=90:
        return index
    else:
        return findFirstUppercaseIndexHelper( s[1:], index+1 )
   



def findFirstUppercaseIndex( s ):
    """ Return the index of the first uppercase letter in 
    string s, if any. Return -1 if there is none. This one 
    requires a helper function, which is the recursive 
    function. """
    return findFirstUppercaseIndexHelper( s, 0 )
