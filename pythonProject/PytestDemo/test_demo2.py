# Any pytest file should start with test_
# pytest method name should start with test
# Any should be wrapped in method only
# v stands for verbos, which will show the more information - pytest -v
# --s is a flag which will help you to print all console logs in output - pytest -v -s
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings doesnot match"


def test_addCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition is not match"




