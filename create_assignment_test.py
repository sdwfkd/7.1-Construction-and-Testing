import pytest
import System

#Tests if the program can handle creating an assignment
def test_create_assignment(grading_system):
    assignment_name = 'assignment15'
    due_date = '04/01/20'
    course = 'cloud_computing'
    grading_system.usr.create_assignment(assignment_name, due_date, course)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
