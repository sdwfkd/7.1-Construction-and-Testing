import pytest
import System

#Tests if the program can add a student to a class
def test_add_student(grading_system):
    name = 'yted91'
    course = 'databases'
    grading_system.usr.add_student(name, course)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
