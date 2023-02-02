def getfile(filename):
    import csv
    data = []
    
    with open(filename) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            data.append(row)
 
    return data