#The REDucers [Jawadul Kadir and Michael Ruvinshteyn]
#SoftDev2 pd07
#K18 -- Reductio ad Absurdum
#2018 - 04 - 30

from functools import reduce

#set up list of all words - strip all punctuation and split by spaces
mani = open("pg61.txt","rU")
manny = " ".join(mani.read().split("\n")) #create a string of all words without newlines
#get rid of all punctuation (optional if you can make wordCount avoid them)
manny = "".join(manny.split(";"))
manny = "".join(manny.split(","))
manny = "".join(manny.split(":"))
manny = "".join(manny.split("."))
manny = manny.split(" ") #make the string into a list
manny = [x for x in manny if len(x) > 0] #get rid of all empty strings (optional)
manny = [x.lower() for x in manny] #lowercase every word to shorten the set
mani.close()

#count the amount of occurrences of the given word
def wordCount(word, l):
    return reduce((lambda x, y: x + y), [1 if x.lower() == word.lower() else 0 for x in l])

#returns the sum of the frequencies of every word within the given list
def groupCount(group, l):
    return reduce((lambda x,y: x + y), [wordCount(x,l) for x in group])   

#return the most common word in the document
#   groups all words in the set of all words (no dupes) with their frequencies
#   reduces the list by continuing with the word that has the larger frequency
def mostCommonWord(l):
    def matchFreq(word):
        return [word, wordCount(word, l)]
    freqs = map(matchFreq, set(l))
    return reduce((lambda x,y:x if x[1] > y[1] else y), freqs)[0].lower()

#test cases
print 'wordCount("bourgeoisie", manny): ' + str(wordCount("bourgeoisie", manny))
print 'wordCount("a", manny): ' + str(wordCount("a", manny))
print 'groupCount(["bourgeoisie","a"], manny): ' + str(groupCount(["bourgeoisie","a"], manny))
print 'wordCount("the", manny): ' + str(wordCount("the", manny))
print 'mostCommonWord(manny): ' + str(mostCommonWord(manny))