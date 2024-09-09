import pytest


@pytest.mark.smoke
def test_secondProgram():
    print("Hello")

# The below test will run, but reports will not be generated.
@pytest.mark.xfail
def test_firstCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])