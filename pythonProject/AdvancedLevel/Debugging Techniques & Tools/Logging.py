import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b


result = add(5, 3)
logging.info(f"Result: {result}")
