import os
import sys
import shutil
import re

def make_output_folder(folder_path, debug=False):
        """ Make folder for output, checking for previous results """

        # Skip if debug (avoids replace prompt)
        if debug:
            print "FolderSetup warning: Not creating directory because debug = True"
            pass

        else:
            # If destination folder does not exist then create it
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            else:
                # Otherwise give a choice to replace (overwrite), use, or exit
                confirm_prompt = "The following folder exists:" + "\n" + \
                    str(folder_path) + "\n" + \
                    "Would you like to add to it ('a'), overwrite ('o'),  or exit ('e'): "
                confirm = raw_input(confirm_prompt)

                # Prompt for correctly formatted input (y/n)
                while not re.search(r'[aeo]', confirm):
                    confirm_prompt = "Please confirm what you want to do." + "\n" + \
                        "Would you like to add to it ('a'), overwrite ('o'),  or exit ('e'):"
                    confirm = raw_input(confirm_prompt)
                
                # If exit
                if confirm == "e":
                    print "OK exiting."
                    sys.exit(1)
                
                # Else if overwrite
                elif confirm == "o":

                    # Make folder path
                    shutil.rmtree(folder_path)
                    os.mkdir(folder_path)

                    print "Created output folder: %s" %(folder_path)

                # Else if add
                elif confirm == "a":
                    print "OK adding to folder"

        return None