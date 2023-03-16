import sys
from app import caps, removeduplicates, question3validation, formatForPrinting, output_results, getfile

filename='../terraform-iac/results.csv'

data = getfile(filename)
data = caps(data)
data = removeduplicates(data)
data = question3validation(data)
output_results(data)
data = formatForPrinting(data)





