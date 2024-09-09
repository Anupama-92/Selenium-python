# Sceanrio - we have to place in conftest only when we think that particular fixtures is shared by multiple files.
import pytest


@pytest.fixture(scope='class')
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Anupama", "Saranu", "anupama.saranu@cognine.com"]

# I have to run test case in multiple browser
# Request is one of the instance will belongs to fixtures


@pytest.fixture(params=[("Chrome","Anupama","Saranu"), ("Firefox","Anupama"), "IE"])
def crossBrowser(request):
    return request.param
