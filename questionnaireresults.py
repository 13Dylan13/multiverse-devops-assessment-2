import sys
from app import getfile, caps, dataclean

filename='results.csv'
cleanedfile='cleanedresults.csv'

#clean the data
#data = dataclean(filename)
data = getfile(filename)
print (data)
data = caps(data)
print (data)

#validate the data
#process the data





