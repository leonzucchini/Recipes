import json
import os
import sys

class UserInput(object):
        """Retrieve user input.
        Currently assumes input files are json format.
        """

        def __init__(self):
            self.patherror = ""

        def path_exists(self, path):
            """Check a path exists"""

            if not os.path.exists(path):
                self.patherror = 'GetInput error: Input path does not exist \n%s' %(path)
                print self.patherror
                sys.exit(1)
            else:
                pass

        def getDict(self, filepath):
            """Retrieve user input from preference / other files.
            Currently assumes input files are json format.
            Returns: Dictionary of input
            """
            self.filepath = filepath
            if not self.patherror:
                with open(filepath, "r") as f:
                    self.input = json.load(f)

        def getFileNames(self, folderpath):
            """Retrieve files containing user input from folder.
            Attribute: List of input files
            """
            self.folderpath = folderpath
            if not self.patherror:
                self.filenames = os.listdir(folderpath)

        def getFilePaths(self, filepath, folderpath):
            """Construct absolute paths from folder path (input) and file paths.
            Check for errors on the way"""
            pass
