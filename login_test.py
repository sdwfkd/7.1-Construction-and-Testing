import pytest
import System

#Tests if the program can handle a correct login
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.login(username,password)
