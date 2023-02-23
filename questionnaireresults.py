import sys
from app import getfile, caps, dataclean

filename='results.csv'
data = getfile(filename)
data = caps(data)
data = dataclean(filename)
print (data)





