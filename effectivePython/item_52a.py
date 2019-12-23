
# Reproduce book environment
import random
random.seed(1234)

import logging
from pprint import pprint
from sys import stdout as STDOUT

# Write all output to a temporary directory
import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# Make sure Windows processes exit cleanly
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)

def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()

atexit.register(close_open_files)


# Example 1
import subprocess
# Enable these lines to make this example work on Windows
# import os
# os.environ['COMSPEC'] = 'powershell'

result = subprocess.Popen(
    ['echo', 'Hello from the child!'],
    stdout = subprocess.PIPE)
    # capture_output=True,
    # Enable this line to make this example work on Windows
    # shell=True,
out, err = result.communicate()
#
#
print(out.decode('utf-8'))

# Example 2
# Use this line instead to make this example work on Windows
# proc = subprocess.Popen(['sleep', '1'], shell=True)
# proc = subprocess.Popen(['sleep','1'],stdout = subprocess.PIPE,shell=True)
# while proc.poll() is None:
#     print('Working...')
#     # Some time-consuming work here
#     import time
#     time.sleep(0.1)
#
# print('Exit status', proc.poll())
