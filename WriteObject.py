import os
import sys
import re
import shutil

class WriteObject:
    def __init__(self, folder):
        """Save string to .txt file in a specified location under a specified name.
        
        Arguments:
        --folder: Folder path where the result should be stored. Relative to cwd.
        --debug: If true then skip check whether results folder exists. 
        """
        self.dstfolder = os.path.join(os.getcwd(), folder)

    def write_file(self, input_text, file_name):
        """Write file to disk, exiting if it already exists."""

        self.input_text = input_text
        self.file_name = file_name
        self.dstpath = os.path.join(self.dstfolder, self.file_name)

        # Check whether the file already exists, exit if yes, else write file
        if os.path.exists(self.dstpath):
            print "Something is wrong: This file already exists. Exiting so you can fix stuff."
            sys.exit(1)
        else:
            with open(self.dstpath, 'w') as f:
                f.write(self.input_text.encode('utf8'))
