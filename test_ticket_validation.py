#Ticket 1
def test_check_that_the_file_loads():
    #ARRANGE
    from app import getfile
    filename='results.csv'
    expected_rows = 26
    expected_titles = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    #ACT
    data = getfile(filename)
    #ASSERT
    assert len(data) == expected_rows
    assert data[0] == expected_titles

#Ticket 2 and 3
def test_remove_duplicated_responses_and_null_rows():
    #ARRANGE
    from app import getfile, dataclean
    filename='results.csv'
    cleanedfile='cleanedresults.csv'
    expected_rows = 20 #duplicate free, Blank free
    expected_titles = ['user_id','first_name','last_name','answer_1','answer_2','answer_3']
    #ACT
    cleaneddata = dataclean(filename)
    data = getfile(cleanedfile)
    #ASSERT
    assert len(cleaneddata) == expected_rows
    assert cleaneddata.isnull().values.any() == False #look for any null data left in the file
    assert len(data) == expected_rows+1 #Due to difference with array and dataframe
    assert data[0] == expected_titles #checking that using dataframes hasn't broken anything


#Ticket 3
def test_confirm_blank_lines_ignored():
    #covered in test_remove_duplicated_responses_and_null_rows
    pass

#Ticket 4
def test_confirm_capitalisation_applied():
    import numpy as np
    from app import getfile, caps
    filename='results.csv'
    cappeddata = []
    expected_rows = 26
    expected_titles = ['User_id','First_name','Last_name','Answer_1','Answer_2','Answer_3']
    #ACT
    data = getfile(filename)
    data = caps(data)
    #ASSERT
    assert len(data) == expected_rows
    assert np.all(data[0] == expected_titles)
    

#Ticket 5
def test_answer_3_validation():
    pass

#Ticket 6
def test_output_file_creation():
    pass

#Ticket 7
def test_display_clean_results():
    pass
