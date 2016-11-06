import os
import json
import re
import sys
import shutil

class FolderSetup(object):
    """ Use preferences file to set up folders and check for existing output.
    """

    def __init__(self, debug = False):
        """ Read preferences to json. 
        Checks path to file preferences exists (else exit).
        Returns: json object with paths and other preferences.
        """
        self.debug = debug
        pass

    def set_cwd(self, homefolderpath):
        """ Set CWD using path from preferences file and pop "_home" from json.
        Skip if debug = True.
        """
        if self.debug:
            print "FolderSetup warning: Not setting cwd because debug = True"
            pass
        else:
            self.home = os.path.abspath(homefolderpath)
            os.chdir(self.home)
            return self.home
