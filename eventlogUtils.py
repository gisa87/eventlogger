# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 11:27:23 2018

@author: Saverio
"""
import re

testString = "Questo è un esempio di #tag che voglio #individuare per assegnare ad @ale cosa fare come @compito"

def parseHastags(intext):
    # create a regex to match a hashtag followed by any number of chars
    hashMatch = re.compile(r'#\w*')
    matchList = hashMatch.findall(intext)
    return(matchList)

def parseAssignations(intext):
    # create a regex to match a @ assignation
    hashMatch = re.compile(r'@\w*')
    matchList = hashMatch.findall(intext)
    return(matchList)
    
def cleantext(intext):
    # remove hastags and assignations and returns the text cleaned
    outText = []
    for character in intext:
        print(character)
        if character != '@' and character != '#':
            outText.append(character)
    return(''.join(outText))
    
def parseValidInputs(validEntryToParse, userInput):
    # the valid argument will be a letter in curve brackets
    validInputs = re.compile(r'\(\w*\)')
    toCheck = validInputs.findall(validEntryToParse)
    
    # to use the letter strip the brackets from the results
    for element in range(0,len(toCheck)):
        toCheck[element] = toCheck[element].strip('(')
        toCheck[element] = toCheck[element].strip(')')
    
    # since the user will give upper or lowercase inputs add to the list 
    # all the lower and uppercase versions of the valid inputs
    for element in range(0,len(toCheck)):
        if toCheck[element].isupper():
            if toCheck[element].lower() not in toCheck:
                toCheck.append(toCheck[element].lower())
        elif toCheck[element].islower():
            if toCheck[element].upper() not in toCheck:
                toCheck.append(toCheck[element].upper())
    
    # check if the user input is in the list of the valid values
    if userInput in toCheck:
        return(userInput)
    else:
        return(False)

hastags = parseHastags(testString)
assignations = parseAssignations(testString)
testoPulito = cleantext(testString)
