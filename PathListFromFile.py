import os, sys, re

class PathList:
    """Import URLs from a text file (complete, each in a new line), return as list."""

    def __init__(self, filename):
        """Initiate PathList instance (source file RELATIVE to the current file)"""
        
        # Get directory of current file #DANGER
        self.filename = os.path.relpath(filename)
        self.rootDir = os.path.dirname(os.path.realpath(__file__))
        self.paths = [] 

        # Get path of file with URLs
        self.srcpath = os.path.join(self.rootDir, self.filename)
        # Assumes the paths are in plain text with the full file, each in a new line
        
        # Check if the path exists, else throw error and terminate
        if os.path.exists(self.srcpath):

            # Read URLs to list
            with open(filename, "r") as f:
                self.paths = f.readlines()
        else:
            print 'PathListFromFile error: Source file does not exist'
            sys.exit(1)

    def split_to_dict(self):
        """Split the path file into a dictionary for labled input. Assumes labels are split with ' = '."""
        self.dict = {}
        for path in self.paths: # check the path has the correct syntax for splitting (" = ")
            if re.search(r'( = )', path):
                foo, bar = path.split(' = ')
                self.dict[foo] = bar.replace("\"", "").replace("\n", "")
                del foo, bar
            else:
                err_message = 'PathListFromFile error: Syntax error in path file:\n' + str(self.srcpath) + '\n-> incorrect format for splitting to dictionary.'
                print err_message
                del err_message
                sys.exit(1)

        return self.dict
