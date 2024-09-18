# Function to test
import unittest


def add(a, b):
    return a+b


# Creating a test case
class TestMathOperations(unittest.TestCase):
    # Runs before every test method
    def setUp(self):
        print("Setup before test")

    # Test method (must start with "test_")
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    # Runs after every test method
    def tearDown(self):
        print("Cleanup after test")


# Running the tests
if __name__ == '__main__':
    unittest.main()


