# Fixtures are used as setup and tear down methods for testcases - conftest file to generalize fixture and make it available to all test cases.
# Fixture is not only to run prequsites and it will also help us to load the data.
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("I will execute steps in fixture demo method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixture demo method")
