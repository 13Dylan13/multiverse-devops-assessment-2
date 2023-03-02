#Ticket 1 and 3
def test_check_that_the_file_loads():
    #ARRANGE
    from app import getfile
    filename='results.csv'
    expected_rows = 24
    expected_titles = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    #ACT
    data = getfile(filename)
    #ASSERT
    assert len(data) == expected_rows
    assert data[0] == expected_titles

#Ticket 2 
def test_duplicate_entries_removed():
    from app import getfile,removeduplicates
    #ARRANGE
    filename='results.csv'
    expected_rows = 21 
    #ACT
    data = getfile(filename)
    data = removeduplicates(data)
    #ASSERT
    assert len(data) == expected_rows
    
#Ticket 4
def test_confirm_capitalisation_applied():
    import numpy as np
    from app import getfile, caps
    filename='results.csv'
    expected_rows = 24
    expected_titles = ['User_id','First_name','Last_name','Answer_1','Answer_2','Answer_3']
    #ACT
    data = getfile(filename)
    data = caps(data)
    #ASSERT
    assert len(data) == expected_rows
    assert np.all(data[0] == expected_titles)
    

#Ticket 5
def test_answer_3_validation():
    #ARRANGE
    from app import getfile, question3validation
    #import numpy as np
    filename='results.csv'
    expected_rows = 21
    #ACT
    data = getfile(filename)
    data = question3validation(data)
    #ASSERT
    assert len(data) == expected_rows

#Ticket 6
def test_output_file_creation():
    #ARRANGE
    from app import getfile, output_results
    import numpy as np
    filename='results.csv'
    cleanedFilename='clean_results.csv'
    expected_rows = 24
    expected_titles = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    last_row = ['20','Felicia','Wilkins','yes','b','8']
    #ACT
    data = getfile(filename)
    output_results(data)
    cleaneddata = getfile(cleanedFilename)
    #ASSERT
    assert len(cleaneddata) == expected_rows
    assert np.all(cleaneddata[0] == expected_titles)
    assert np.all(cleaneddata[23] == last_row)
    #could add a time creation check
    

#Ticket 7
def test_display_clean_results():
    #ARRANGE
    from app import getfile, caps,removeduplicates,question3validation, formatForPrinting
    filename='results.csv'
    #ACT
    data = getfile(filename)
    data = caps(data)
    data = removeduplicates(data)
    data = question3validation(data)
    #ASSERT
    formatForPrinting(data)
    
