import pytest
import System

#Tests if the program can handle submitting a fake assignment
def test_grade_change(grading_system):
    assignment_name = 'assignment42'
    current_date = '04/01/20'
    course = 'cloud_computing'
    grading_system.usr.submit_assignment(course,assignment_name,'Blah Blah Blah',current_date)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
