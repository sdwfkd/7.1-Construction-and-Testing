import pytest
import System

#Tests if the program can drop a fake student from a class
def test_drop_student(grading_system):
    name = 'NotPresent'
    course = 'cloud_computing'
    grading_system.usr.drop_student(name, course)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
