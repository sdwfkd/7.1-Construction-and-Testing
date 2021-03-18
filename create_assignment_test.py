import pytest
import System

#Tests if the program can handle a grade change
def test_grade_change(grading_system):
    assignment_name = 'assignment15'
    due_date = '04/01/20'
    course = 'cloud_computing'
    grading_system.usr.create_assignment(assignment_name, due_date, course)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
