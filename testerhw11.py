
"""
midterms= {'Susie': 'dropped', 'Frank': 87, 'Charles': 79}

user=input("Which one??? ")

#if user==user[key]:
#    print(key)

print(midterms[user])
    
for key in midterms:    
    print(key, ":", midterms[key])
"""


PUNC=["!", ",", "?", ".", ":"]
newstr=""

ques=input("give a string: ")
for i in ques:
    if i in PUNC:
        newstr=newstr+" "+i+" "
        #print(True)
    else:
        newstr=newstr+i
print(newstr)
newstr=newstr.split()
print(newstr)

