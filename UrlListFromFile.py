import os

class UrlList:
    """Import URLs from a text file (complete, each in a new line), return as list."""

    def __init__(self, filename):
        # Get directory of current file 
        # NOTE THIS IS GOING TO BREAK IF I MOVE IT => REALLY WANT THE DIRECTORY OF THE *ENCLOSING* FILE
        self.filename = os.path.relpath(filename)
        self.rootDir = os.path.dirname(os.path.realpath(__file__))
        self.urls = [] 

        # Get path of file with URLs
        """ Assumes the URLs are in plain text with the full file, each in a new line"""
        self.path = os.path.join(self.rootDir, self.filename)
        
        # Read URLs to list
        with open(filename, "r") as f:
            self.urls = f.readlines()
