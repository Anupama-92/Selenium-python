# Package in python is a folder that contains various modules as files.
# __init__.py helps the Python interpreter recognize the folder as a package.
# It also specifies the resources to be imported from the modules.
# If the __init__.py is empty this means that all the functions of the modules will be imported.
# We can also specify the functions from each module to be made available.

# from .Mod1 import package
# from .Mod2 import sum

# Import Modules from a Package-import package_name.module_name
from mypackage import Mod1
from mypackage import Mod2

Mod1.package()
res = Mod2.sum(1, 2)
print(res)
