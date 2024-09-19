import pdb
import sys

try:
    1 / 0  # Division by zero causes an error
except:
    _, _, tb = sys.exc_info()  # Get the traceback object
    pdb.post_mortem(tb)  # Start pdb in post-mortem mode
