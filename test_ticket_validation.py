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

#Ticket 2
def test_remove_duplicated_responses():
    #ARRANGE
    from app import getfile, removeduplicates, removeblanks
    filename='results.csv'
    expected_rows = 21 #duplicate free, Blank free
    #ACT
    data = getfile(filename)
    data = removeblanks(data) #added to avoid error when converting '' to an int
    data = removeduplicates(data)
    #ASSERT
    assert len(data) == expected_rows


#Ticket 3
def test_confirm_blank_lines_ignored():
    #ARRANGE
    from app import getfile, removeblanks
    filename='results.csv'
    expected_rows = 24 #Blank free
    #ACT
    data = getfile(filename)
    data = removeblanks(data)
    #ASSERT
    assert len(data) == expected_rows
    

#Ticket 4
def test_confirm_capitalisation_applied():
    import numpy as np
    from app import getfile, caps
    filename='results.csv'
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
    #ARRANGE
    from app import getfile, question3validation, removeblanks
    #import numpy as np
    filename='results.csv'
    expected_rows = 21
    #ACT
    data = getfile(filename)
    data = removeblanks(data) #added to avoid error when converting '' to an int
    data = question3validation(data)
    #ASSERT
    assert len(data) == expected_rows

#Ticket 6
def test_output_file_creation():
    pass

#Ticket 7
def test_display_clean_results():
    pass
