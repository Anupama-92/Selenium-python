# Fixtures are used in testing frameworks like pytest to set up a pre-defined state before running test functions.
# Selenium framework we use fixtures for opening up a browser or setting up a database instances or creating some configuraton properties, environment variables.
# Basic Fixture:
import pytest


@pytest.fixture
def setup():
    # Setup code before test
    print("\nSetup before test")
    yield
    # Teardown code after test
    print("\nTeardown after test")


def test_example(setup):
    print("Test function")
    assert True

# Using Fixture to Provide Data:


@pytest.fixture
def data():
    return {'name': 'John', 'age': 30}


def test_data(data):
    assert data['name'] == 'John'
    assert data['age'] == 30

# Fixture with Setup and Teardown:


@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup before module")
    yield
    print("\nTeardown after module")


@pytest.fixture
def setup_function():
    print("\nSetup before function")
    yield
    print("\nTeardown after function")


def test_example1(setup_module, setup_function):
    print("Test function 1")
    assert True


def test_example2(setup_module, setup_function):
    print("Test function 2")
    assert True


# Fixture for Temporary Files:
import tempfile

@pytest.fixture
def temp_file():
    # Setup - create a temporary file
    temp_file = tempfile.NamedTemporaryFile()
    yield temp_file.name
    # Teardown - close and delete the temporary file
    temp_file.close()

# Fixture for Database Connection

import sqlite3

@pytest.fixture(scope="module")
def db_connection():
    # Setup - connect to a test database
    conn = sqlite3.connect(':memory:')
    yield conn
    # Teardown - close the database connection
    conn.close()

def test_query_data(db_connection):
    # Test function that requires a database connection
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
    db_connection.commit()

    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    assert len(results) == 2

# Fixture for Temporary Files:


import tempfile


@pytest.fixture
def temp_file1():
    # Setup - create a temporary file
    temp_file = tempfile.NamedTemporaryFile()
    yield temp_file.name
    # Teardown - close and delete the temporary file
    temp_file.close()


def test_write_to_temp_file(temp_file):
    # Test function that writes data to a temporary file
    with open(temp_file, 'w') as f:
        f.write('Hello, World!')

    with open(temp_file, 'r') as f:
        content = f.read()

    assert content == 'Hello, World!'


# Fixture for Selenium WebDriver:

from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    # Setup - create a WebDriver instance (assuming Chrome)
    driver = webdriver.Chrome()
    yield driver
    # Teardown - close the WebDriver instance
    driver.quit()


def test_search(browser):
    # Test function that uses a WebDriver to perform a search
    browser.get("https://www.example.com")
    search_input = browser.find_element_by_name("q")
    search_input.send_keys("pytest")
    search_input.submit()
    assert "pytest" in browser.title


from unittest.mock import Mock


class Calculator:
    def add(self, a, b):
        return a + b


@pytest.fixture
def calculator():
    return Calculator()


def test_calculator_add(calculator):
    calculator.add = Mock(return_value=5)
    result = calculator.add(2, 3)
    assert result == 5
    calculator.add.assert_called_once_with(2, 3)



