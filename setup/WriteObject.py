import os
import sys
import re
import shutil

class WriteObject(object):
    def __init__(self, inputtext, filepath):
        """Write file to disk, exiting if it already exists."""

        self.inputtext = inputtext
        self.filepath = filepath

        if os.path.exists(self.filepath):
            print "WriteObject error: This file already exists. Exiting..."
            sys.exit(1)
        else:
            with open(self.filepath, 'w') as f:
                f.write(self.inputtext)
