

import os


def main():
    filename=input("Enter a filename: ")
    print()
    if not os.path.exists(filename):
        print("File not found"+ filename)
        print()
        return
    else:
        fullcount, uniquecount, newdict=createDictionary(filename)


    mostfreq=mostFrequentWords(newdict,10)
    longwords=longestWords(newdict,10)
    shortwords=shortestWords(newdict,10)


    print("Text analysis of file: ", filename)
    print("  Total word count:  ", fullcount)
    print("  Unique word count: ", uniquecount)
    print("  10 most frequent words: \n  ", mostfreq)
    print("  10 longest words: \n  ", longwords)
    print("  10 shortest words: \n  ", shortwords)

def cleanLine( s ):
    """Given a string s, remove designated punctuation and convert others:
    non-ascii single quotes to ascii equivalents; underscore and dash
    to space."""

    # Create a translation table that maps any character in string
    # toRemove to a None.  Also translates the non-ascii single quote
    # to an ascii single quote and underscore/dash to blank.

    toTranslate = "\u2018\u2019\u2010\u2014\u2012-"
    translateTo = "''    "
    toRemove = ".,;:?$()[]\u201C\u201D\u00A3"
    translationTable = str.maketrans(toTranslate, translateTo, toRemove)
    
    # Use the translate() method to apply the mapping to string s
    translatedText = s.translate(translationTable)

    #print("Translated Text:", translatedText)
    return translatedText




# We won't put these common words in the dictionary:
wordsToExclude = ['a', 'about', 'after', 'all', 'also', 'am', 'an', 'and',
                  'any', 'are', 'as', 'at', 'back', 'be', 'because',
                  'but', 'by', 'can', 'come', 'could', 'day', 'do',
                  'even', 'first', 'for', 'from', 'get', 'give', 'go',
                  'good', 'had', 'have', 'he', 'her', 'him', 'his',
                  'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its',
                  'just', 'know', 'like', 'look', 'make', 'man', 'me',
                  'men', 'most', 'my', 'new', 'no', 'not', 'now',
                  'of', 'on', 'one', 'only', 'or', 'other', 'our',
                  'out', 'over', 'people', 'said', 'say', 'see',
                  'she', 'so', 'some', 'take', 'than', 'that', 'the',
                  'their', 'them', 'then', 'there', 'these', 'they',
                  'think', 'this', 'time', 'to', 'two', 'up', 'us',
                  'use', 'want', 'was', 'way', 'we', 'well', 'went',
                  'were', 'what', 'when', 'which', 'who', 'will',
                  'with', 'work', 'would', 'year', 'you', 'your']



def createDictionary( filename ):
    """Create a dictionary associating each word in a text file with the
    number of times the word occurs.  Also count the total number of
    words and the number of unique words in the text.  Certain very
    common words are not included in the dictionary, but are counted.
    Return a triple: (wordCount, uniqueWordCount, dictionary)."""
    fullcount=0
    uniquecount=0
    newdict={}
    seenalr=set()

    userfile=open(filename, "r")

    for line in userfile:
        newlines=cleanLine(line)    
        newlines=newlines.split()

        for word in newlines:
            word=word.lower()

            if word.isdigit():
                continue
            fullcount+=1

            if word in newdict:
                newdict[word]+=1
            elif word in wordsToExclude:
                if word not in seenalr:
                    seenalr.add(word)
                    uniquecount+=1
            else:
                newdict[word]=1
                uniquecount+=1

    userfile.close()
    #print(fullcount, uniquecount, newdict)
    return fullcount, uniquecount, newdict




def sortByFrequency( newdict ):
    """Return a list of pairs of (count, word)
    sorted by count in descending order. I.e., 
    the most frequent word should be first in the
    list."""
    topten=[]

    for word in newdict:
        count=newdict[word]
        #topten.append((newdict[word], word))
        topten.append((count,word))

    topten.sort(reverse=True)
    #print(topten)
    return topten



# Think about how to use the function sortByFrequency
# for this one.
def mostFrequentWords( newdict, k ):
    """Return a list of the k most frequently occurring 
    words."""
    newsorts=sortByFrequency(newdict)
    most=[]
    
    for word in range(k):
        #fix this
        frq=newsorts[word][1]
        most.append(frq)
    
    #print(most)
    return most



def sortByWordLength( newdict ):
    """Return a list of pairs of (length, word)
    sorted by length in descending order. I.e.,
    the longest word should be first in the list."""
    length_lst=[]

    for word in newdict:
        length=len(word)
        length_lst.append((length,word))

    length_lst.sort(reverse=True)

    #print(length_lst)
    return length_lst



# Think about how to use the function sortByWordLength
# for this one.
def longestWords( newdict, k ):
    """Return a list of the k longest words in the
    text."""
    wordlen=sortByWordLength(newdict)
    longs=[]

    for word in range(k):
        value=wordlen[word][1]
        longs.append(value)

    return longs



# Think about how to use the function sortByWordLength
# for this one.
def shortestWords( newdict, k ):
    """Return a list of the k shortest words in the
    text."""
    wordlen=sortByWordLength(newdict)
    short=[]

    for word in range(-1,-k-1,-1):
        value=wordlen[word][1]
        short.append(value)

    #print(longs)
    return short



#newdict[userfile.lower()]
main()
