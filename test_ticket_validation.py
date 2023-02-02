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
    pass

#Ticket 3
def test_confirm_blank_lines_ignored():
    pass

#Ticket 4
def test_confirm_capitalisation_applied():
    pass

#Ticket 5
def test_answer_3_validation():
    pass

#Ticket 6
def test_output_file_creation():
    pass

#Ticket 7
def test_display_clean_results():
    pass
