def getfile(filename):
    import csv
    data = []
    
    with open(filename) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            data.append(row)
 
    return data

def deduplicate(data):
    deduped_data = list(dict.fromkeys(data))
    return deduped_data

def caps(data):
    import numpy as np
    data = np.char.capitalize(data)
    return data