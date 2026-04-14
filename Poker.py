# Description of Program: play poker with this program

from Hand import *





while True:
    n=int(input("How many hands should I deal? "))
    if n<=0:
        print(" Positive number required. Try again! ")
        continue
    else:
        d=Deck()
        d.shuffle()
        print()
        break


for i in range(1, n+1):
    if len(d)<5:
        print("Dealing a new deck.")
        d=Deck()
        d.shuffle()
    h=Hand(d, True)
    print("Hand drawn ("+ str(i)+ "):")
    evaluateHand(h)
    print()
    
