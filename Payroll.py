# File: Payroll.py
# Student: Mia Garza
# UT EID: mkg2545
# Course Name: CS303E
# 
# Date: 1/21/26
# Description of Program:




#Using input statement to get the user's name, how much they worked, pay rate, and tax rates 

print()

name=input("Enter employee's name: ")
hours_worked=float(input("Enter number of hours worked in a week: "))
pay_rate=float(input("Enter hourly pay rate: "))
fed_tax=float(input("Enter federal tax withholding rate: "))
state_tax=float(input("Enter state tax withholding rate: "))

print()


#calculating gross pay, witholding amounts, total deduction, and net pay
#variables with CALC at the end are the final calculations of pay/deductions   

gross_pay= hours_worked*pay_rate

fed_taxCALC= fed_tax*gross_pay
state_taxCALC= state_tax*gross_pay

total_ded=fed_taxCALC+state_taxCALC            
net_pay=gross_pay-total_ded



#printed out employee payroll

print("Employee Name:", name) 
print("Hours Worked:", hours_worked)
print("Pay Rate: $", format(pay_rate, ".2f"), sep="")
print("Gross Pay: $", format(gross_pay, ".2f"), sep="")

#Deduction Amounts 
print("Deductions: \n  Federal Withholding (", fed_tax*100, "%): $", format(fed_taxCALC, ".2f"), sep = "")
print("  State Withholding (", state_tax*100, "%): $", format(state_taxCALC, ".2f"), sep = "")
print("  Total Deduction: $", format(total_ded, ".2f"), sep = "")

#Final Net Pay for the employee
print("Net Pay: $", format(net_pay, ".2f"), sep = "")

print()




      

      
