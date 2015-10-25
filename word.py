import sys
import re

##########################################################################
# Function    : filterWordsBasedOnLength
# Parameters  : jumbledWord(String) and dictionary reference word(String)
# Returns     : String
# Description : This function matches the two given string for 
#               their length and returns the word if the lenghts are same.
##########################################################################

def filterWordsBasedOnLength(jumbledWord,word):
    if len(jumbledWord) == len(word):
        return word



# Function    : computeValuForEachWord
# Parameters  : filteredWord(String) and jumbledWord(String)
# Returns     : boolean
# Description : This computes the unicode value of each sting to filter out
#               the words and then if the value matches it then checks
#  	whether the characters match if they do it return true else
#		false

   
def computeValuForEachWord(filteredWord,jumbledWord):
    filteredWordValue = 0
    jumbledWordValue = 0
    for character in filteredWord:
        filteredWordValue += ord(character)

    for char in jumbledWord:
        jumbledWordValue += ord(char)
    filteredWord = list(filteredWord)
    if filteredWordValue == jumbledWordValue:
        for w in jumbledWord:
            if w not in filteredWord:
                return False
	    else:
                del filteredWord[filteredWord.index(w)] #For filtering out cases where value becomes same due to multi occurence of same char
        return True
    else:
        return False



# Function    : process()
# Parameters  : 
# Returns     : String
# Description : This is the main process initializer for the code that 
#               invokes all other functions for computations


def process():

    try:
        inputFile = open("dictionary.txt","r")
    except Exception, e:
        print "Exception while reading the dictionary file . Following are the details of the exception :\n\r"+ str(e)
	sys.exit(0)
    #words = inputFile.read().strip().split("\r\n") #This would be faster but cannot use as it input file format could vary.
    fileContents = words = inputFile.read().strip() #Striping whitespaces
    words = re.split("[\s\n\r]+",fileContents) #Splitting the file into word tokes based on either spaces/new line/carriage return

    if len(sys.argv) < 2: #check for whether input specified or not
        print "No jumbled word specified.Please enter a jumbled word."
	sys.exit(0)
    else:
	jumbledWord = sys.argv[1] 
	filteredWords = [filterWordsBasedOnLength(jumbledWord,word) for word in words]
	filteredWords = filter(None,filteredWords)
        for dictionaryWord in filteredWords:
            if computeValuForEachWord(dictionaryWord,jumbledWord):
                print dictionaryWord
        

process()

