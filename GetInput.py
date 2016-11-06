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
                self.patherror = \
                    'GetInput error: Input path does not exist \n%s' %(path)
                print self.patherror
                sys.exit(1)
            else:
                pass
            return self

        def getDict(self, filepath):
            """Retrieve user input from preference / other files.
            Assumes input files are json format.
            Attribute defined: Dictionary of input
            """
            self.filepath = filepath
            self.path_exists(self.filepath)

            with open(filepath, "r") as f:
                self.json = json.load(f)
            return self

            ### This would actually be nicer to do differently
            ### because it currently only has one attribute slot
            ### for input (but don't want to waste time fiddling)
            ### around with setattr() now.


        def getFilePaths(self, folderpath):
            """Retrieve files containing user input from folder.
            Attribute defined: List of input file paths based on folder path.
            """
            # Get list of filenames from folder
            self.folderpath = folderpath

            self.path_exists(self.folderpath)
            self.filenames = os.listdir(folderpath)
            
            # Construct file paths
            self.filepaths = []
            for name in self.filenames:
                self.filepaths.append(
                  os.path.join(self.folderpath, name)  
                )
            return self

        def print_prefs(self, attr):
            """ Print json file nicely for a given json attribute."""
            attr = getattr(self, attr)
            print json.dumps(attr, indent=4, sort_keys=True)