
from Deck import *

def isLegalCardList( l ):
    """ Check that list l contains 5 legal card specifiers, 
        all distinct. You can assume that it's a list. """
    # You'll need to fill this in

    if len(l)!=5:
        return False
    
    if len(l)!=len(set(l)):
        return False
    
    for i in l:
        if not isLegalCardSpecifier(i):
            return False
    return True
          

class Hand:

    def __init__(self, source, fromDeck = True):
        """ A hand is simply a list of 5 cards, dealt from the deck
            or given as a list of five card specifiers.  If fromDeck
            is True, expect to deal from a deck passed as source. 
            If False, expect source to be a list of five Card specifiers.
            Create the hand from the specified cards.
        """



        if fromDeck:
            if ( len(source) < 5 ):
                print ( "Not enough cards left!" )
                return None
            self.__cards = []
            for i in range(5):
                card = source.deal()              # deal next card
                self.__cards.append(card)         # append it to the hand
        elif not isLegalCardList( source ):
            print("Illegal card list provided.")
        else:
            # fill in this code, to generate a hand from
            # a list of Card specifiers.  You can assume that
            # source is a list,

            #MG- create list self.__cards=[]
            #go thru each item in source
            #turn it into a card
            #add it to my list
            self.__cards=[]
            for i in source:
                card=Card(i)
                self.__cards.append(card)


    def __str__(self):
        """ Generates the print image of the Hand. """
        emptystr=""
        for i in self.__cards:
            card=str(i)
            emptystr=emptystr+card+"\n"
        return emptystr

    def getCard( self, i ):
        """ Get the ith card from the hand, where 
            i in [0..4]. Return None if i is not
            legal. """
        if 0<=i<=4:
            value=self.__cards[i]
        else:
            value=None
        return value
            
################################################################################
#                                                                              #
#                                Evaluate Hand                                 #
#                                                                              #
################################################################################

def processHand(hand):
    """ Given a poker hand, create and return two lists which
        record the ranks and suits in the hand. """
    myRanks = [0] * 13    
    mySuits = [0] * 4     

    for i in range(5):
        card=hand.getCard(i)

        rank= card.getRank()
        suit= card.getSuit()

        rankindex=CARDRANKS.index(rank)
        suitindex=CARDSUITS.index(suit)

        myRanks[rankindex]+=1
        mySuits[suitindex]+=1
    
    return myRanks, mySuits
    #pass


# You'll need to define all of the auxiliary functions called by
# evaluateHand.  Notice that these auxiliary functions don't all
# need both myRanks and mySuits, but I decided to pass them both
# just to make the interface more uniform.  You can change that 
# if you want to.

def hasPair( myRanks, mySuits ):
    for i in myRanks:
        if i==2:
            return True
    return False
    

def hasTwoPair(myRanks, mySuits):
    count=0
    for i in myRanks:
        if i==2:
            count+=1
    if count==2:
        return True
    return False

def hasThreeOfAKind( myRanks, mySuits ):
    for i in myRanks:
        if i==3:
            return True
    return False

"""
#FIX THIS ONE!!!!!!!!
def hasStraight( myRanks, mySuits ):
    for [i] in myRanks:
        count=0

        if myRanks[i]==1: 
            count+=1                
        if myRanks[i+1]==1:
            count+=1
        if myRanks[i+2]==1:
            count+=1
        if myRanks[i+3]==1:
            count+=1
        if myRanks[i+4]==1:
            count+=1

        if count==5:
            return True
    return False
"""


#good to go 
def hasStraight( myRanks, mySuits ):
    for i in range(len(myRanks)-4):
        count=0

        if myRanks[i]==1: 
            count+=1                
        if myRanks[i+1]==1:
            count+=1
        if myRanks[i+2]==1:
            count+=1
        if myRanks[i+3]==1:
            count+=1
        if myRanks[i+4]==1:
            count+=1

        if count==5:
            return True
        
    count2=0
    if myRanks[12]==1: 
        count2+=1                
    if myRanks[0]==1:
        count2+=1
    if myRanks[1]==1:
        count2+=1
    if myRanks[2]==1:
        count2+=1
    if myRanks[3]==1:
        count2+=1
    if count2==5:
        return True
    
    return False 


        
def hasFlush( myRanks, mySuits ):
    for i in mySuits:
        if i==5:
            return True
    return False


def hasFullHouse( myRanks, mySuits ):
    value1=False
    value2=False

    for i in myRanks:
        if i==2:
            value1=True
        if i==3:
            value2=True
    return value1 and value2


def hasFourOfAKind( myRanks, mySuits ):
    for i in myRanks:
        if i==4:
            return True
    return False



#FIX THIS ONE TOO!!!!!!!
def hasStraightFlush( myRanks, mySuits ):
    return hasStraight(myRanks, mySuits) and hasFlush(myRanks, mySuits)



def hasRoyalFlush( myRanks, mySuits ):
    count=0
    for i in myRanks[8: ]:
        if i==1:
            count+=1

    return(count==5 and hasFlush(myRanks, mySuits))


# Add other recognizers here; evaluateHand tells you which ones you
# need.  I suggest doing them in "reverse order" so you define the 
# lowest hands first. Hopefully, you'll see why as you code them!

def evaluateHand( hand ):
    myRanks, mySuits = processHand( hand )
    print( hand )

    if hasRoyalFlush( myRanks, mySuits ):
        print( "Royal Flush" )

    elif hasStraightFlush( myRanks, mySuits ):
        print( "Straight Flush" )

    elif hasFourOfAKind( myRanks, mySuits ):
        print( "Four of a kind" )

    elif hasFullHouse( myRanks, mySuits ):
        print( "Full House" )

    elif hasFlush( myRanks, mySuits ):
        print( "Flush" )

    elif hasStraight( myRanks, mySuits ):
        print( "Straight" )

    elif hasThreeOfAKind( myRanks, mySuits ):
        print( "Three of a kind" )

    elif hasTwoPair( myRanks, mySuits ):
        print( "Two pair" )

    elif hasPair( myRanks, mySuits ):
        print("Pair")
    else:
        print( "Nothing" )

# This is some test code.  You can modify this or write your
# own.  You certainly should test additional hands. You can run 
# this in interactive mode with:
# 
# from Hand import *
# TestCode()
#
# You can also run this in batch mode by uncommenting the call to:
# TestCode()
#
# and running:
# 
# python3 Hand.py              # or whatever the python command is
#                              # is on your system. 


"""
def TestCode():
    print("\nGenerating and printing deck")
    d = Deck()
    #print(d)
    print("\nShuffling deck and printing deck")
    d.shuffle()
    #print(d)

    print("\nGenerating hand from deck")
    h = Hand(d, True)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["as", "ad", "ah", "ac", "2d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["AS", "2S", "3C", "4H", "5D"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    cardSpec = ["2s", "9S", "tc", "AH", "4d"]
    h = Hand(cardSpec, False)
    evaluateHand( h )

    print("\nGenerating hand from list")
    h6 = Hand(d, True)              # back to dealing from the deck d
    evaluateHand( h6 )

TestCode()
"""
