
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
        
    pass  

class Hand:

    def __init__(self, source, fromDeck = True):
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


#FIX THIS ONE!!!!!!!!
def hasStraight( myRanks, mySuits ):
    for i in myRanks:
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
        
def hasFlush( myRanks, mySuits ):
    for i in mySuits:
        if i==5:
            return True
    return False


def hasFullHouse( myRanks, mySuits ):
    for i in myRanks:
        if i==2:
            value1=True
        else:
            value1=False
    for i in myRanks:
        if i==3:
            value2=True
        else:
            value2=False
    return value1 and value2


def hasFourOfAKind( myRanks, mySuits ):
    for i in myRanks:
        if i==4:
            return True
    return False



#FIX THIS ONE TOO!!!!!!!
def hasStraightFlush( myRanks, mySuits ):
    for i in myRanks:
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
            value1=True
        else:
            value1=False

    for i in mySuits:
        if i==5:
            value2=True 
        else:
            value2=False

    return value1 and value2


def hasRoyalFlush( myRanks, mySuits ):
    count=0
    for i in myRanks[8: ]:
        if i==1:
            count+=1

    value2=False
    for i in mySuits:
        if i==5:
            value2=True

    return(count==5 and value2)


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



def TestCode():
    print("\nGenerating and printing deck")
    d = Deck()
    print(d)
    print("\nShuffling deck and printing deck")
    d.shuffle()
    print(d)

    print("\nGenerating hand fro3m deck")
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

# TestCode()

