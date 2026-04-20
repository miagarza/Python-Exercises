# Assignment: Project 2
# File: AnalyzeText.py
# Student: Mia Garza
# UT EID: mkg2545
# Course Name: CS303E
# 
# Date: 4/19/26
# Description of Program: complex 

import os


def main():
    filename=input("Enter a filename: ")+ ".txt"

    if not os.path.exists():
        print("File does not exist"+ filename[:-4])
        print()
        return
    else:
        createDictionary(filename)


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
    FullCount=0
    newdict={}

    userfile=open(filename, "r")    #keep
    for line in userfile:   #keep
        newlines=cleanLine(line)    #keep
        key=newlines.split() #keep

        for word in key:    #keep
            word=word.lower()  
            #newdict[key.lower()]=value
            FullCount+=1
            if word not in wordsToExclude:
                newdict[word]=1
            else:
                newdict[word]+=1
    userfile.close()

        #newdict[userfile.lower()]


  