import pytest
import Staff

#Tests if the program can handle a grade change
def test_grade_change(grading_system):
    username = 'akend3'
    course = 'comp_sci'
    assignment =  'assignment1'
    grade = 91
    grading_system.usr.change_grade(username,course,assignment,grade)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
