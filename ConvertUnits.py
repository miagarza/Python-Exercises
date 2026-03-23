# File: ConvertUnits.py
# Student: Mia Garza
# UT EID: mkg2545
# Course Name: CS303E
# 
# Date: 1/21/26
# Description of Program: Takes a measurement of feet and inches from the user
# and converts it into English and metric units


#Asking for user input of feet and inches
inputFeet = float( input("Enter number of feet: ") )
inputInches = float( input("Enter number of inches: ") )


#Below are mathematical conversions to calculate the measurements  

#Calculating the Enligh Units
inches= (inputFeet*12) + inputInches
feet= inches/12

yards=feet/3
miles=feet/5280


#Calculating the metric units 
meters=feet*.3048
centimeters=meters*100

millimeters=centimeters*10
kilometers=meters/1000


#print statements that give conversions

#prints out the feet and inches user inputed, with empty print statements where necessary
print()
print(inputFeet, " feet and ", inputInches, " inches equals:")
print()

#prints English Units
print("English Units\n  feet:" , format(feet, "0.4f"),
      "\n  inches:", format(inches, "0.4f"),
      "\n  yards:", format(yards, "0.4f"),
      "\n  miles:", format(miles, "0.4f"))

print()

#prints Metric Units
print("Metric Units\n  meters:" , format(meters, "0.4f"),
      "\n  centimeters:", format(centimeters, "0.4f"),
      "\n  millimeters:", format(millimeters, "0.4f"),
      "\n  kilometers:", format(kilometers, "0.4f"))

print()
