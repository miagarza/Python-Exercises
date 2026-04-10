# Description of Program: Decrypts genz slang for unfamiliar populations


import os

EXPLAIN_TERM="1"
TRANSLATE="2"
EXTEND_CHANGE="3"
SHOW_MENU= "4"
EXIT="5"
ERROR="Action not recognized; please enter 1-5."
BAD_TERM="Term not defined: "

LEGAL_COMMANDS = [EXPLAIN_TERM, TRANSLATE, EXTEND_CHANGE, SHOW_MENU, EXIT]
PUNC=["!", ",", "?", ".", ":"]
MENU="""The following actions are available: 
1 - Explain a term.   
2 - Translate a message.
3 - Extend/Change the dictionary. 
4 - Show this menu. 
5 - Exit the application """



def ask():
    new_dict={}
    file_name=input("Specify file containing terms and definitions: ") + ".txt"

    if not os.path.exists(file_name):
        print("File does not exist: "+ file_name[:-4])
        print()
    else:
        userfile=open(file_name, "r")
        print("Building dictionary from: "+ file_name)
        for line in userfile:
            line=line.strip()
            key, value = line.split(":")
            new_dict[key.strip()] = value.strip()
        actions(new_dict)


#function to call for all the actions
def actions(new_dict):
    print()
    print(MENU)
    
    while True: 
        print()
        choose= input("Choose an action (1-5): ")

        #validates it
        if choose not in LEGAL_COMMANDS:
            print("Action not recognized; please enter 1-5.")
            continue

        #1 explains what the term means 
        if choose == EXPLAIN_TERM:
            #print("EXPLAIN_TERM")
            var=input("     Please enter a term to explain: ")
            print()
            if var not in new_dict:
                print("Term not defined:", var)
                continue
            elif var in new_dict:
                print(var, ": ", new_dict[var], sep="")

                
        #task 2, breaking up if punctuation 
        if choose == TRANSLATE:
            newstr=""
        
            var2=input("    Please enter a message to translate: ")
            for i in var2:
                if i in PUNC:
                    newstr=newstr+" "+i+" "
                else:
                    newstr=newstr+i
            newstr=newstr.split()
           

            for i in range(len(newstr)):
                if newstr[i] in new_dict:
                    newstr[i]=new_dict[newstr[i]]
            final=" ".join(newstr)
            print()
            print("Message Translation: "+ final)
            #print()


        #3 adds a new term and definition to the dict 
        if choose == EXTEND_CHANGE:
            added_term=input("  Add the following term: ").upper()
            added_def=input("   With definition: ")
            new_dict[added_term]=added_def



        #4 just show the menu
        if choose == SHOW_MENU:
            print()
            print(MENU)


        #5 EXIT evth
        if choose == EXIT:
            print()
            print("Thanks for using this app. Goodbye!")
            print()
            break



    

print()
print("Welcome to the Text Translator application. ")
print()
ask()
