# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
#py.test is command for execute all testcases in command prompt
# py.test -v(verbos- provide more info)
# py.test -v -s(It will print all console logs in the output)
# In pytest, every method is treated as one test case.
# py.test -k CreditCard -v-s
# Method name should make sense
# -k stands for method names execution, -s logs in output -v stands for more information
# Can run specific file with py.test <filename>
# Can mark (tag) tests @pytest.mark.smoke an then run with -m
# Can skip the test with @pytest.mark.skip
# datadriven and Parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"




