import sys
from app import getfile, caps, removeblanks, removeduplicates, question3validation

filename='results.csv'
cleanedfile='cleanedresults.csv'

#clean the data
data = getfile(filename)
#print('original length', len(data))
data = removeblanks(data)
#print('no blanks', len(data))
data = caps(data)
#print('caps', len(data))
data = removeduplicates(data)
#print(len(data))
data = question3validation(data)
#print('q3', len(data))

print (data)
#validate the data
#process the data





