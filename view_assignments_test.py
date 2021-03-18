import pytest
import System

#Tests if the program can handle viewing a course the student isnt in
def test_grade_change(grading_system):
    course = 'cloud_computing'
    grading_system.usr.view_assignments(course)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
