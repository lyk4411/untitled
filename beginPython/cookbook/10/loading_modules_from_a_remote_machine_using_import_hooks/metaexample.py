# metaexample.py
#
# Example of using a meta-path importer

# Enable for debugging
if False:
    import logging
    logging.basicConfig(level=logging.DEBUG)

from . import urlimport
urlimport.install_meta('http://localhost:15000')

from .testcode import fib
from .testcode import spam
from .testcode.grok import blah
print(blah.__file__)
