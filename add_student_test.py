import pytest
import System

#Tests if the program can add a student
def test_grade_change(grading_system):
    name = 'yted91'
    course = 'databases'
    grading_system.usr.create_assignment(name, course)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
