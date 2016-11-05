import os
import json
import re
import sys
import shutil

class FolderSetup(object):
    """ Use preferences file to set up folders and check for existing output.
    """

    def __init__(self, prefs_abs_filepath, debug = False):
        """ Read preferences to json. 

        Checks path to file preferences exists (else exit).
        
        Returns: json object with paths and other preferences.
        """
        self.pref_filepath = prefs_abs_filepath
        self.debug = debug

        if os.path.exists(self.pref_filepath):
            with open(self.pref_filepath, "r") as f:
                self.prefs = json.load(f)
        else:
            print 'FolderSetup error: Preferences file does not exist'
            sys.exit(1)

    def print_prefs(self):
        """ Print preference json file
        """
        print json.dumps(self.prefs, indent=4, sort_keys=True)

    def set_cwd(self):
        """ Set CWD using path from preferences file and pop "_home" from json.
        Skip if debug = True.

        """
        if self.debug:
            print "FolderSetup warning: Not setting cwd because debug = True"
            pass
        else:
            self.home = os.path.abspath(self.prefs['_home'])
            self.prefs.pop('_home') # this is helpful with create_dir() below
            os.chdir(self.home)
            return self.home
    
    def create_dirpaths(self):
        """Parse preferences file for subdirectories.
        Construct subdirectory and input file paths and return all as dictionary.
        """
        self.paths = {}
        for k, v in self.prefs.items():
            self.paths[k] = os.path.join(self.home, self.prefs[k])