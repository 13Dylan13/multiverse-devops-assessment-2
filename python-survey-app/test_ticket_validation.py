#Ticket 1 and 3
def test_check_that_the_file_loads():
    #ARRANGE
    from app import getfile
    filename='../terraform-iac/results.csv'
    expected_titles = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    nulls = 0
    n = 0
    #ACT
    data = getfile(filename)
    rowcount = len(data)
    while n < rowcount:
        if data[n] == ['', '', '', '', '', '']:
            nulls=nulls+1
        n=n+1
    #ASSERT
    assert data[0] == expected_titles
    assert nulls == 0

#Ticket 2 
def test_duplicate_entries_removed():
    from app import getfile,removeduplicates
    #ARRANGE
    filename='../terraform-iac/results.csv'
    import numpy as np
    duplicatesfound = 0
    #ACT
    data = getfile(filename)
    data = removeduplicates(data)
    rowcount = len(data)
    n=0
    while n < rowcount-1:
        if np.all(data[n][0]==data[n+1][0]):
            duplicatesfound = duplicatesfound+1
        n=n+1
    n=0
    #ASSERT
    assert duplicatesfound == 0
    
#Ticket 4
def test_confirm_capitalisation_applied():
    import numpy as np
    from app import getfile, caps
    filename='../terraform-iac/results.csv'
    expected_titles = ['User_id','First_name','Last_name','Answer_1','Answer_2','Answer_3']
    #ACT
    data = getfile(filename)
    data = caps(data)
    #ASSERT
    assert np.all(data[0] == expected_titles)
    

#Ticket 5
def test_answer_3_validation():
    #ARRANGE
    from app import getfile, question3validation
    import numpy as np
    filename='../terraform-iac/results.csv'
    #ACT
    data = getfile(filename)
    data = question3validation(data)
    invalidanswers = 0
    rowcount = len(data)
    n=1 #ignore the titles
    while n < rowcount-1:
        if np.all(int(data[n][5]) > 10):
            invalidanswers = invalidanswers+1
        n=n+1
    #ASSERT
    assert invalidanswers == 0

#Ticket 6
def test_output_file_creation():
    #ARRANGE
    from app import getfile, output_results
    import numpy as np
    filename='../terraform-iac/results.csv'
    cleanedFilename='clean_results.csv'
    expected_titles = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    #ACT
    data = getfile(filename)
    output_results(data)
    cleaneddata = getfile(cleanedFilename)
    cleanedrowcount = len(cleaneddata)
    initialrowcount = len(data)
    #ASSERT
    assert len(cleaneddata) == len(data)
    assert np.all(cleaneddata[0] == expected_titles)
    assert cleanedrowcount == initialrowcount
    #could add a time creation check
    

#Ticket 7
def test_display_clean_results():
    #ARRANGE
    from app import getfile, caps,removeduplicates,question3validation, formatForPrinting
    filename='../terraform-iac/results.csv'
    #ACT
    data = getfile(filename)
    data = caps(data)
    data = removeduplicates(data)
    data = question3validation(data)
    #ASSERT
    formatForPrinting(data)
    
