def getfile(filename):
    import csv
    data = []
    
    with open(filename) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            data.append(row)
    return data

def dataclean(filename): #this needs to run on the user id
    import pandas as pd
    import numpy as np
    cleaneddata = pd.read_csv(filename)
    cleaneddata = cleaneddata.dropna(how='all') #drop blank rows
    cleaneddata.drop_duplicates(subset=['user_id'], keep='first', inplace=True) #drop duplicates
    cleaneddata.to_csv(r'cleanedresults.csv', index = False, header=True)
    return cleaneddata
    

def caps(data): 
    import numpy as np
    data = np.char.capitalize(data)
    return data