def getfile(filename):
    import csv
    data = []
    with open(filename) as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=",")
          for row in csv_reader:
            if row == ['', '', '', '', '', '']:
                continue
            else:
                data.append(row)
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
        if np.all(data[n][0]==data[n+1][0]):
            todelete.append(n+1)
        n=n+1
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
    deletecount=len(todelete)
    n=0
    while n < deletecount:
        data = np.delete(data, todelete[-1], 0) 
        todelete= todelete[:-1] #remove deleted item from the to delete list
        n=n+1
    return data    

def output_results(data):
    import csv
    with open('clean_results.csv','w+', newline='') as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(data)

def formatForPrinting(data):
    from tabulate import tabulate
    print(tabulate(data, headers="firstrow"))
    


def check_for_blanks(data): 
    #created for testing only
    nulls = 0
    rowcount = len(data)
    n = 0
    while n < rowcount:
        if data[n] == ['', '', '', '', '', '']:
            nulls=nulls+1
        n=n+1
    return nulls

def checkforduplicates(data):
    #created for testing only
    #The test data is sorted by user id... this assumes this is true for all input data
    import numpy as np
    rowcount = len(data)
    duplicatesfound = 0
    n=0
    while n < rowcount-1:
        if np.all(data[n][0]==data[n+1][0]):
            duplicatesfound = duplicatesfound+1
        n=n+1
    n=0
    return duplicatesfound    

def checkforinvalidQ3answers(data):
    #created for testing only
    import numpy as np
    invalidanswers = 0
    rowcount = len(data)
    n=1 #ignore the titles
    while n < rowcount-1:
        if np.all(int(data[n][5]) > 10):
            invalidanswers = invalidanswers+1
        n=n+1
    return invalidanswers