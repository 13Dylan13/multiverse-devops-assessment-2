import sys
from app import getfile, caps, dataclean

filename='results.csv'
cleanedfile='cleanedresults.csv'
data = getfile(filename)
data = caps(data)
data = dataclean(filename)
print (data)
nulls = data.isnull().values.any()
print (nulls)





