# Description of Program: Computes the amount of days between two dates 



#sets numbers to the months 
JAN =  1
FEB =  2
MAR =  3
APR =  4
MAY =  5
JUN =  6
JUL =  7
AUG =  8
SEP =  9
OCT = 10
NOV = 11
DEC = 12


#sets the amount of days per each month 
JAN_DAYS = 31
# Skipping February for now.
MAR_DAYS = 31
APR_DAYS = 30
MAY_DAYS = 31
JUN_DAYS = 30
JUL_DAYS = 31
AUG_DAYS = 31
SEP_DAYS = 30
OCT_DAYS = 31
NOV_DAYS = 30
DEC_DAYS = 31

#sets error message 
ERROR_MSG= "Invalid date entered. Try again."



#primary function that asks the user for dates, plus validates and checks it
def main():
    #gets first round of dates
    print("--------------------------------------------------")
    print()
    day1=int(input("Enter day 1 (1-31): "))
    month1=int(input("Enter month 1 (1-12): "))
    year1=int(input("Enter a year after 1752: "))

    #checks if user wants to exit
    if (day1 and month1 and year1)==0:
        print()
        print("Thanks for visiting! ")
        return
    
    #validates that the first batch of dates are within range 
    if not (validday(day1) and validmonth(month1) and validyear(year1)):
        print(ERROR_MSG)
        return
    #checks if user entered a bad february date if its a leap year
    if leapyear(year1,month1, day1) and month1==2 and day1==29:
        print(ERROR_MSG)
        return

    #prompts user for second round of dates
    print()
    day2=int(input("Enter day 2 (1-31): "))
    month2=int(input("Enter month 2 (1-12): "))
    year2=int(input("Enter a year after 1752: "))

    #validates dates
    if not (validday(day2) and validmonth(month2) and validyear(year2)):
        print(ERROR_MSG)
        return 
    #checks if user entered a bad february date if its a leap year
    if leapyear(year2, month2, day2) and month2==2 and day2==29:
        print(ERROR_MSG)
        return

    #determines if the dates are chronological, prints error message if not 
    if not datesinorder(day1,day2, month1, month2 ,year1, year2):
        print("Dates out of order: ", month1, "/", day1, "/", year1, \
          " ", month2, "/", day2, "/", year2, sep="")
        return

    #determines if leap year
    leapyear(day1, month1, year1)
    leapyear(day2, month2, year2)  

    #gets values from the daysinyear function for both sets of dates entered, needs for later calculation 
    ordinal1, remaining1= daysinyear(day1, month1,year1) 
    ordinal2, remaining2= daysinyear(day2, month2,year2)

    #defines finaldays
    finaldays=daysbetween(year1,year2,remaining1,ordinal2)

    #the final statement, gives days between dates and both dates again 
    print("There are ", finaldays , " days between ", month1, "/", day1, "/", year1, \
          " and ", month2, "/", day2, "/", year2, sep="")
    print()
    print("--------------------------------------------------")


    
#validates user inputted days
def validday(day):
    if 1<=day<=31:
        return True
    

#validates user inputted months
def validmonth(month):
    if JAN<=month<=DEC:
        return True


#validates user inputted years
def validyear(year):
    if year>1752:
        return True

    
#determines if leap year
def leapyear(day, month, year):
    if not (# month is February and a leap year.
            ( (month == FEB) and (( year % 4 == 0 ) and ( not ( year % 100 == 0 ) or ( year % 400 == 0 ))) and (1 <= day <= 29) ) \
            # Month is February and it's not a leap year
            or ( (month == FEB) and (1 <= day <= 28) ) \
            # Month is April, June, September, or November
            or ( ( (month == APR) or (month == JUN) or (month == SEP) or (month == NOV) ) and (1 <= day <= 30) ) \
            # All other months
            or ( (    (month == JAN) or (month == MAR) or (month == MAY) or (month == JUL)  \
            or (month == AUG) or (month == OCT) or (month == DEC) ) and (1 <= day <= 31 ) ) ):
        return leapyear

    
#determines ordinal date 
def daysinyear(day, month,year):
    FEB_DAYS = 29 if ( year % 4 == 0 ) and ( not ( year % 100 == 0 ) or ( year % 400 == 0 )) else 28

    ordinalDate=0

    #amount of days in the full year, depending if leap year or not
    if leapyear:
        fullyear=365
    else:
        fullyear=366
    
    #calculations to determine ordinal date 
    if month == JAN:
        ordinalDate = day
    elif month == FEB:
        ordinalDate = JAN_DAYS + day
    elif month == MAR:
        ordinalDate = JAN_DAYS + FEB_DAYS + day
    elif month == APR:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + day
    elif month == MAY:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + day
    elif month == JUN:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + MAY_DAYS + day
    elif month == JUL:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + MAY_DAYS + JUN_DAYS + day
    elif month == AUG:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + MAY_DAYS + JUN_DAYS + JUL_DAYS + day
    elif month == SEP:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + MAY_DAYS + JUN_DAYS + JUL_DAYS + AUG_DAYS + day
    elif month == OCT:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + MAY_DAYS + JUN_DAYS + JUL_DAYS + AUG_DAYS + SEP_DAYS + day
    elif month == NOV:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + MAY_DAYS + JUN_DAYS + JUL_DAYS + AUG_DAYS + SEP_DAYS + OCT_DAYS + day
    elif month == DEC:
        ordinalDate = JAN_DAYS + FEB_DAYS + MAR_DAYS + APR_DAYS + MAY_DAYS + JUN_DAYS + JUL_DAYS + AUG_DAYS + SEP_DAYS + OCT_DAYS + NOV_DAYS + day

    #calculates remaining days 
    remainingdays=fullyear-ordinalDate
    return ordinalDate, remainingdays


#determines if dates are chronological 
def datesinorder(day1,day2,month1,month2, year1, year2):
    if year1>year2:
        return False 
    elif month1<month2 and day1>day2:
        return False
    else:
        return True


#determines the amount of days between dates 
def daysbetween(year1,year2,remaining1,ordinal2):
    yearsbetween=year2-year1

    #determines how many leap years are within the years between the dates 
    #Gets full number and its remainder
    amntofLYs=yearsbetween//4
    reaminder=yearsbetween%4

    #if remainder is larger than 1, then there is actually another leap year
    #than what the amntofLYs gave us 
    if reaminder>1:
        amntofLYs+=1

    #cutting off a year since you still need to include ordinal and remaining 
    yearsbetween-=1

    #final days calculation
    finaldays=(yearsbetween*365)+amntofLYs+remaining1+ordinal2
    return finaldays



main()





