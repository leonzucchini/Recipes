import os

def set_cwd(homefolderpath, debug = False):
        """ Set CWD. Skip if debug = True."""
        if debug:
            print "FolderSetup warning: Not setting cwd because debug = True"
            pass
        else:
            os.chdir(os.path.abspath(homefolderpath))