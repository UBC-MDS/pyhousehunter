from pyhousehunter import emailer
import pandas as pd
from pytest import raises

# Toy data for tests
toy_data = pd.read_csv('tests/toy.csv')
empty_data =  pd.DataFrame()

# Tests on input
def test_invalid_email_type():
    """
    Test to confirm that ValueError is raised when wrong email address is provided.
    """
    with raises(TypeError):
       emailer.send_email(123, toy_data)

def test_invalid_email_value():
    """
    Test to confirm that ValueError is raised when wrong email address is provided.
    """
    with raises(ValueError):
       emailer.send_email("ela.com", toy_data)
       emailer.send_email("ela", toy_data)

def test_invalid_subject_type():
    """
    Test to confirm that TypeError is raised when wrong type if provided for subject.
    """
    with raises(TypeError):
       emailer.send_email("elabandari@gmail.com", 123)

def test_invalid_dataframe():
    """
    Test to confirm that TypeError is raised when dataframe is the wrong object type.
    """
    with raises(TypeError):
       emailer.send_email("elabandari@gmail.com", 123)

def test_dataframe_empty():
    """
    Test to confirm that ValueError is raised when dataframe is empty.
    """
    with raises(ValueError):
        emailer.send_email("elabandari@gmail.com", empty_data)

# Tests on output
def test_email_sent_return_none():
    """
    Test to confirm that email has been sent and function returns None.
    """
    assert emailer.send_email("elabandari@gmail.com", toy_data) == None

