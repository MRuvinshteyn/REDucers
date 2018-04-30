from functools import reduce
#import re

manny = open("pg61.txt","rU")
manny = manny.read()
manny = manny.split("\n")
manny = " ".join(manny)
manny = manny.split(" ")
#manny = re.split(" ",manny)
#print manny
print reduce((lambda x, y: x + y), [1 if x.lower() == "bourgeoisie" else 0 for x in manny])

print reduce((lambda x, y: max(x,y)), manny)


#print manny
