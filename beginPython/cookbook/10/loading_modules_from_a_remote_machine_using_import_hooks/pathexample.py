# Example of path-path import hook

# Enable for debugging
if False:
    import logging
    logging.basicConfig(level=logging.DEBUG)

from . import urlimport
urlimport.install_path_hook()

import sys
sys.path.append('http://localhost:15000')

from .testcode import fib
from .testcode import spam
from .testcode.grok import blah
print(blah.__file__)

