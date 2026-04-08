# File: TextTranslate.py
# Student: Mia Garza
# UT EID: mkg2545
# Course Name: CS303E
# 
# Date: 4/5
# Description of Program: Decrypts genz slang for unfamiliar populations


#import os
#print(os.listdir())
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


EXPLAIN_TERM="1"
TRANSLATE="2"
EXTEND_CHANGE="3"
SHOW_MENU= "4"
EXIT="5"

ERROR="Action not recognized; please enter 1-5."
BAD_TERM="Term not defined: "

LEGAL_COMMANDS = [EXPLAIN_TERM, TRANSLATE, EXTEND_CHANGE, SHOW_MENU, EXIT]

#so could i just store it by indexing into before and after the :, 
# then grabbing that string and putting it into a dict
#ask for file name, then open it and read thru it 
#when i need to access smth, just look it up, just like you would for a list
#loop through it to get actions and apply them 
#



def ask():
    new_dict={}
    question=input("Specify file containing terms and definitions: ").lower()
    userfile=open(question, "r")
    print(userfile)
    if question:
        print("Building dictionary from: "+ question)
        for line in userfile:
            line=line.strip()
            key, value = line.split(":")
            new_dict[key.strip()] = value.strip().lower()
    actions(new_dict)



def actions(new_dict):
    #do i put this whole thing in a while True loop? 
    print()
    print("The following actions are available: \n"
            "1 - Explain a term. \n"
            "2 - Translate a message.\n"
            "3 - Extend/Change the dictionary. \n"
            "4 - Show this menu. \n"
            "5 - Exit the application \n")
    
    while True: 
        print()
        choose= input("Choose an action (1-5): ")
        if choose not in LEGAL_COMMANDS:
            print("Action not recognized; please enter 1-5.")
            continue
        if choose is EXPLAIN_TERM:
            #print("EXPLAIN_TERM")
            var=input("     Please enter a term to explain: ")
            if var not in new_dict:
                print("Term not defined:", var)
                print()
                continue
            elif var in new_dict:
                print()
                print(var, ": ", new_dict[var], sep="")

                

        if choose is TRANSLATE:
            print("TRANSLATE")
        if choose is EXTEND_CHANGE:
            print("EXTEND_CHANGE")
        if choose is SHOW_MENU:
            print("SHOW_MENU")
        if choose is EXIT:
            print("EXIT")





#def get_it():

    

print()
print("Welcome to the Text Translator application. ")
ask()
print()