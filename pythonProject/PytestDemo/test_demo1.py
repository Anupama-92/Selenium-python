# Any pytest file should start with test_
# pytest method name should start with test
# Any should be wrapped in method only
# v stands for verbos, which will show the more information - pytest -v
# --s is a flag which will help you to print all console logs in output - pytest -v -s
# py.test -k CreditCard -v -s to run multiple methods from different tests
# -k stands for method name execution, -s logs in output, -v stands for more info metadata
# We can run specific file with py.test <filename>
# We can mark (tag) tests @pytest.mark.smoke and then run with -m
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


def test_CreditCard():
    print("Hello Good morning")

