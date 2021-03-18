import pytest
import System

#Tests if the program can check a false submission time
def test_check_ontime(grading_system):
    submission_date = False
    due_date = '04/01/20'
    grading_system.usr.check_ontime(submission_date, due_date)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
