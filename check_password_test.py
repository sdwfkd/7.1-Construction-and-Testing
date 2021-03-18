import pytest
import System

#Tests if the program can handle a correct password
def test_check_password(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.check_password(username,password)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
