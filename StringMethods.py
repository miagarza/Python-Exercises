# Description of Program: Variety of strings functions 



#1- Adds ch onto s string
def myAppend(s, ch):
    return s+ch


#2- returns the amount of times ch appears
def myCount( s, ch ):
    count=0
    for i in s:
        if i==ch:
            count+=1
    return count


#3- adds strings s1 and s2 together
def myExtend( s1, s2 ):
    return s1+s2



#4- returns the character with the lowest ASCII value
def myMin(s):
    min=127

    if s=="":
        print("Empty string: no min value")
        return
    for i in s:
        new=ord(i)
        if new<min:
            min=new
    return(chr(min))


#5- gives a new string where ch is inserted at the ith position
def myInsert(s,i,ch):
    if i> len(s):
        print("Invalid index")
        return None
    
    x=s[ :i]
    y=s[i: ]
    
    if i==0:
        return ch+x+y
    if i==len(s):
        return x+y+ch
    else:
        return x+ch+y


#6- returns a string like s but with the ith element removed and the value that was removed 
def myPop(s,i):
    if i>= len(s):
        print("Invalid index")
        return s, None
    else:
        x2=s[ :i]
        y2=s[i+1: ]
        letter=s[i]
        return x2+y2, letter


#7- finds the first occurance of ch in s
def myFind(s, ch):
    count=-1
    if ch not in s:
            return count
    for i in range(len(s)):
        count+=1
        if s[i]==ch:
            return count


#8- returns the index of the last occurance of ch in s
def myRFind(s,ch):
    count=-1
    if ch not in s:
            return count
    for i in range(1, len(s)+1):
        if s[-i]==ch:
            return (len(s)-i)
            break


#9- returns the index of the last occurance of ch in s removed 
def myRemove(s, ch):
    if ch not in s:
        return s
    for i in range(len(s)):
        if s[i]==ch:
            x2=s[ :i]
            y2=s[i+1: ]
            return x2+y2 
             
        
            
#10- removes all instances of ch in s
def myRemoveAll( s, ch ):
    newstr=""
    if ch not in s:
        return s
    for i in range(len(s)):
        if s[i]!=ch:
            newstr=newstr+s[i]
    return newstr




#11- determines is s1 is equal to s2, returns boolean
def myEqual(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True 



#12- returns boolean determining whether s is nonempty and consists of only decimal digits
def myIsdigit(s):
    if s=="":
        return False
    for i in range(len(s)):
        if not 48<=ord(s[i])<=57:
            return False
    return True
            


    
#13- returns the reverse of string s
def myReverse(s):
    newstr=""
    for i in s:
        newstr=i+ newstr
    return newstr


#14- deterines if string s is read the same backwards and forwards
def isPalindrome(s):
    newlist=""
    for i in s:
        newstr=i+newstr

    for i in range(len(s)):
        nums=ord(s[i])
        nums2=ord(newstr[i])
        if nums!=nums2:
            return False 
    return True



#15- counts the number of times s1 occurs within s2
def countOccurrences( s1, s2 ):
    count=0
    for i in range(len(s2)-(len(s1)-1)):
        if s1==s2[i:i+len(s1)]:
            count+=1
    return count



"""
    #strings=strings[].lower()
    for strings in strings:
        okay= -1
        for i in range(len(strings)):
            if strings[i] in vowels:
                okay=i 
        final[strings]=okay
    
    return final 
     
"""
