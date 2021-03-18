import pytest
import System

#Tests if the program can handle a correct password
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.check_password(username,password)
