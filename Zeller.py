# Assignment: HW4
# File: Zeller.py
# Student: Mia Garza
# UT EID: mkg2545
# Course Name: CS303E
# 
# Date: 1/29/26
# Description of Program: User inputs the data numerically and the program responds with the
#day of the week it falls on 


def main():
    print()
    
    #gets year from  user and checks if its in range 
    y=int(input("Enter year (e.g., 2025): "))
    if (y<1753):
        print("Year must be after 1752. Illegal year entered:", y)
        return
    
    #gets month from user and checks if its in range 
    m=int(input("Enter month (1-12): "))
    if (m<1 or m>12):
        print("Month must be in [1..12]. Illegal month entered:", m)
        return
    
    #gets day from user and checks if its in range
    d=int(input("Enter day (1-31): "))
    if (d<1 or d>31):
        print("Day must be in [1..31]. Illegal month entered:", d)
        return

    #makes conversions if necessary
    if (m== 1 or m==2):
        m=m+12
        y=y-1


    #calculating the k and j values, which represent the year within the century and
    #the century, respectively 
    k=y%100              
    j=int((y-k)/100)    
    

    #calculates h and puts a day of a week to a number
    h = ( d + (13 * (m + 1))//5 + k + k//4 + j//4 + 5*j ) % 7
    if (h==0):
        x="Saturday"
    elif (h==1):
        x="Sunday"
    elif (h==2):
        x="Monday"
    elif (h==3):
        x="Tuesday"
    elif (h==4):
        x="Wednesday"
    elif (h==5):
        x="Thursday"
    elif (h==6):
        x="Friday"
    print("Day of the week is", x)
 
        
main()



