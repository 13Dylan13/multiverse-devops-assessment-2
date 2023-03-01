def getfile(filename):
    import csv
    data = []  
    with open(filename) as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            data.append(row)
    return data

def removeblanks(data): 
    #need to update to work in the array
    import numpy as np
    rowcount=len(data)
    n = 0
    todelete=[]
    deletecount=0
    #find blank rows
    while n < rowcount:
        if np.all(data[n]==['', '', '', '', '', '']):
            todelete.append(n)
        n=n+1
    #delete blank rows - work backwards to avoid impacting loc
    #deleterows(data,todelete)
    deletecount=len(todelete)
    n=0
    while n < deletecount:
        data = np.delete(data, todelete[-1], 0) 
        todelete= todelete[:-1] #remove deleted item from the to delete list
        n=n+1
    return data    

    

def caps(data): 
    import numpy as np
    rowcount=len(data)
    n = 0
    while n < rowcount:
        data[n] = np.char.capitalize(data[n])
        n = n+1
    return data


def removeduplicates(data):
    #The test data is sorted by user id... this assumes this is true for all input data
    #may look to change for future release
    import numpy as np
    rowcount = len(data)
    n=0
    todelete = []
    while n < rowcount-1:
        if np.all(data[n][0]==data[n+1,0]):
            todelete.append(n+1)
        n=n+1
    #deleterows(data,todelete)
    deletecount=len(todelete)
    n=0
    while n < deletecount:
        data = np.delete(data, todelete[-1], 0) 
        todelete= todelete[:-1] #remove deleted item from the to delete list
        n=n+1
    return data    

def question3validation(data):
    #max anser is 10
    import numpy as np
    rowcount = len(data)
    n=1 #ignore the titles
    todelete = []
    while n < rowcount-1:
        if np.all(int(data[n][5]) > 10):
            todelete.append(n)
        n=n+1
        #deleterows(data,todelete)
    deletecount=len(todelete)
    n=0
    while n < deletecount:
        data = np.delete(data, todelete[-1], 0) 
        todelete= todelete[:-1] #remove deleted item from the to delete list
        n=n+1
    return data    