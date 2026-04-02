# Description of Program: Finds the maximum, minimum, and average of inputed grades
# along with the amount of passing/failing grades, and the total amount given. 


#Constants that set a baseline for the calculations 
AVRG_OF_GRADES=0
TOTAL_OF_GRADES=0
NUM_OF_GRADES= 0
NUM_OF_FAILING=0


#first user input that establishes the first value, the min, and the max. Also checks if grades entered
grades=float(input("Enter a grade or -1 to finish: "))
if grades==-1:
    print()
    print("  No grades entered.") 
    print()
MIN_GRADE=grades
MAX_GRADE=grades



#while loop that caluclates min, max, average, passing/failing and iterates each time new grade is given 
while grades!=-1:
    #uses constants to calculate and iterate over each given grade 
    NUM_OF_GRADES+=1
    TOTAL_OF_GRADES+=grades
    AVRG_OF_GRADES= (TOTAL_OF_GRADES)/NUM_OF_GRADES
    #checks if grades are passing, determines min and max
    if grades<70:
        NUM_OF_FAILING+=1
    if grades<MIN_GRADE:
        MIN_GRADE=grades
    if grades>MAX_GRADE:
        MAX_GRADE=grades
    passingamnt=NUM_OF_GRADES-NUM_OF_FAILING
    #prompts the user the quesiton again if while condititon true 
    grades=float(input("Enter a grade or -1 to finish: "))
    #once user breaks out of program, grade stats are printed 
    if grades==-1:
        print()
        print("  Number of grades:", format(NUM_OF_GRADES, ">9.0f"))
        print("  Number failing:", format(NUM_OF_FAILING, ">11.0f"))
        print("  Number passing:", format(passingamnt, ">11.0f"))
        print("  Minimum grade:", format(MIN_GRADE,">12.2f"))
        print("  Maximum grade:", format(MAX_GRADE,">12.2f"))
        print("  Average grade:", format(AVRG_OF_GRADES, ">12.2f"))
        print()
        break

