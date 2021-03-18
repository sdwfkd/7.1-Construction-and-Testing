import pytest
import System

#Tests if the program can handle checking grades for a course that doesnt exist
def test_grade_change(grading_system):
    course = 'Fake_Class'
    grading_system.usr.check_grades(course)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
