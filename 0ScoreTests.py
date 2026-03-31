# Assignment: HW10
# File: ScoreTests.py
# Student: Mia Garza
# UT EID: mkg2545
# Course Name: CS303E
# 
# Date: 3/28/25
# Description of Program: grades a (wide and changing) variety of tests and validates inputs



STUDENT = ['Kevin', 'Joe', 'Nick', 'Michael', 'Randy', 'Jermaine', 'Tito', 'Marlon', 'Jackie', 
           'Jimmy', 'Merrill', 'Alan', 'Jay', 'Wayne', 'Virl', 'Donnie', 'Phil', 'Don', 'Dick', 'Tom' ]

CORRECT =  ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'D']

ANSWERS = [['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'D'],
           ['A', 'C', 'C', 'B', 'A', 'A', 'A', 'A', 'C', 'C', 'C', 'B', 'B', 'A', 'C', 'D', 'C', 'A', 'A', 'D'], 
           ['B', 'C', 'B', 'B', 'A', 'A', 'B', None, 'C', 'A', 'C', 'B', 'D', 'A', 'D', 'C', 'A', 'D', 'A', 'D'], 
           ['A', None, 'C', None, None, 'A', 'D', 'A', 'C', 'C', 'A', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', None], 
           ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'C', 'C', 'B', 'C', 'B', 'D', 'A', 'C', 'A', 'C', 'C', 'A', 'D'], 
           ['B', 'D', 'B', 'B', None, 'A', 'D', 'B', 'C', 'C', 'C', 'B', 'A', 'A', 'C', 'D', 'C', None, 'A', 'D'], 
           ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'A', 'B', 'D', 'D', 'C', 'A', 'A', 'D'], 
           ['A', 'D', 'D', 'B', 'A', 'B', 'D', 'A', 'D', 'D', 'C', 'A', 'A', 'A', 'C', 'C', 'C', 'A', 'C', None], 
           ['D', 'C', None, 'B', 'D', 'A', 'D', None, 'D', None, 'C', 'D', 'A', 'A', 'D', 'A', None, 'A', 'A'], 
           ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'D'], 
           ['B', 'C', 'C', 'D', 'A', 'A', 'D', 'A', 'C', 'A', 'C', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'D'], 
           ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'A', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'D'], 
           ['D', 'D', 'B', 'C', 'A', 'A', 'A', 'A', 'D', 'C', 'C', 'D', 'A', 'B', 'C', 'B', 'B', 'A', 'D', 'C'], 
           ['A', 'C', 'C', 'B', 'A', 'A', 'D', None, 'D', 'C', 'C', None, 'A', 'C', 'C', 'D', 'C', 'A', 'A'], 
           ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'A', 'A', 'C', 'D', 'C', 'A', 'A', 'D'], 
           ['A', 'C', 'C', 'B', 'B', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'A', 'D', 'C', 'D', 'D', 'D', 'A', 'B'], 
           ['A', 'C', 'C', 'B', 'D', 'A', 'A', None, 'C', None, 'C', 'D', 'D', 'C', 'C', 'D', 'C', None, 'A', 'A'], 
           ['A', 'D', 'C', 'D', 'C', 'C', 'D', 'A', 'C', 'C', 'C', 'C', 'A', 'A', 'C', None, 'D', 'A', 'A', 'D'], 
           ['A', 'C', 'C', 'B', 'A', 'A', 'D', 'A', 'C', 'C', 'C', 'B', None, 'A', 'C', 'D', 'C', 'A', 'A', 'D'], 
           ['A', 'A', 'D', 'B', None, 'A', 'D', 'A', 'C', None, 'C', 'A', 'A', 'A', 'C', 'A', None, 'A', 'B', 'D']]


#constants
correct=0     
ERROR="Bad format in answer list."
scores_total=0
minus=0


#intial formatting and header
print()
print("Student".ljust(10) + "Grade".rjust(9))
print("-"*20)


for x in range(len(STUDENT)):
    #Validates length of student given exam against the real length  
    if len(CORRECT)!=len(ANSWERS[x]):
        print(str(STUDENT[x].ljust(10))+" : "+ERROR)
        minus+=1
        continue
#Grades the exams 
    for i in range(len(CORRECT)):
        if ANSWERS[x][i] not in ['A','B','C','D']:
            continue
        if CORRECT[i]==ANSWERS[x][i]:
            correct+=1
#determines the actual score by calculating it 
    correct=(correct/len(CORRECT))*100
    print(str(STUDENT[x].ljust(10))+ " : " + format(correct, "7.2f"))
    scores_total+=correct 
    correct=0

#provides the average score 
scores_total=scores_total/(len(ANSWERS)-minus)
print("-"*20)
print("Average".ljust(10)+ " : " + format(scores_total, "7.2f"))
print()



