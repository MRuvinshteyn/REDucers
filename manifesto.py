#The REDucers [Jawadul Kadir and Michael Ruvinshteyn]
#SoftDev2 pd07
#K18 -- Reductio ad Absurdum
#2018 - 04 - 30

from functools import reduce

#set up string of all words - strip all punctuation and split by spaces
manny = open("pg61.txt","rU").read()
manny = " ".join(manny.split("\n"))
manny = "".join(manny.split(";"))
manny = "".join(manny.split(","))
manny = "".join(manny.split(":"))
manny = "".join(manny.split("."))
manny = manny.split(" ")
manny = [x for x in manny if len(x) > 0]

#count the amount of occurrences of the given word
def wordCount(word):
    return reduce((lambda x, y: x + y), [1 if x.lower() == word.lower() else 0 for x in manny])

#return the most common word in the document
#   groups all words in the set of all words (no dupes) with their frequencies
#   reduces the list by continuing with the word that has the larger frequency
def mostCommonWord():
    def matchFreq(word):
        return [word, wordCount(word)]
    freqs = map(matchFreq, set(manny))
    return reduce((lambda x,y:x if x[1] > y[1] else y), freqs)[0].lower()

print wordCount("bourgeoisie")
print wordCount("a")
print wordCount("the")
print mostCommonWord()