import sys
from app import getfile, caps, removeblanks, removeduplicates, question3validation, formatForPrinting, output_results

filename='results.csv'

data = getfile(filename)
data = removeblanks(data)
data = caps(data)
data = removeduplicates(data)
data = question3validation(data)
output_results(data)
data = formatForPrinting(data)





