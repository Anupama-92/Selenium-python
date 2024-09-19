import ipdb


def add(a, b):
    ipdb.set_trace()  # Enhanced pdb debugger
    return a + b


result = add(5, 3)

import pudb

def add(a, b):
    pudb.set_trace()  # Full-screen terminal debugger
    return a + b

