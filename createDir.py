import os
import sys
import shutil
import re

def create_dir(dirpath, debug = False):
        """Create subdirectory, checking for 
        Construct subdirectory and input file paths and return all as dictionary.
        Skip if debug = True.
        """

        if debug:
            print "FolderSetup warning: Not creating directory because debug = True"
            pass
        
        else:
            # If destination folder does not exist then create it
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)
            
            # Otherwise give a choice to replace (overwrite), use, or exit
            else:
                confirm_prompt = "The following folder exists:" + "\n" + \
                    str(dirpath) + "\n" + \
                    "Would you like to add to it ('a'), overwrite ('o'),  or exit ('e'): "
                confirm = raw_input(confirm_prompt)

                # Prompt for correctly formatted input (y/n)
                while not re.search(r'[aeo]', confirm):
                    confirm_prompt = "Please confirm what you want to do." + "\n" + \
                        "Would you like to add to it ('a'), overwrite ('o'),  or exit ('e'):"
                    confirm = raw_input(confirm_prompt)
                
                # If exit
                if confirm == "e":
                    print "OK exiting..."
                    sys.exit(1)
                
                # Else if overwrite
                elif confirm == "o":
                    shutil.rmtree(dirpath)
                    os.mkdir(dirpath)
                
                # Else if add
                elif confirm == "a":
                    pass