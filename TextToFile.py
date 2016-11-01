import os, sys, re, shutil

class TextFile:
    """Save string to .txt file in a specified location under a specified name."""
    def __init__(self, input_text, dstfolder, file_name):
        self.input_text = input_text
        self.dstfolder = dstfolder
        self.file_name = file_name

    def writeToFile(self):
        # Add cwd to folder path and check whether folder already exists
        self.dstfolder = os.path.join(os.getcwd(), self.dstfolder)
        print str(self.dstfolder)        
        # If destination folder does not exist then create it
        if not os.path.exists(self.dstfolder):
            os.mkdir(self.dstfolder)
        
        # Otherwise give a choice to replace (overwrite), use, or exit
        else:
            confirm_prompt = "The following folder exists:" + "\n" + \
                str(self.dstfolder) + "\n" + \
                "Would you like to add to it ('a'), overwrite ('o'),  or exit ('e'): "
            confirm = raw_input(confirm_prompt)

            # Prompt for correctly formatted input (y/n)
            while not re.search(r'^[aeo]$', confirm):
                confirm_prompt = "Please confirm what you want to do." + "\n" + \
                    "Would you like to add to it ('a'), overwrite ('o'),  or exit ('e'): "
                confirm = raw_input(confirm_prompt)
            
            # If exit
            if confirm == "e":
                print "OK exiting so you can fix the paths."
                sys.exit(1)
            
            # Else if overwrite
            elif confirm == "o":
                shutil.rmtree(self.dstfolder)
                os.mkdir(self.dstfolder)
            
            # Else if add
            elif confirm == "a":
                pass

        # Construct destination file path and check whether it already exists
        self.dstpath = os.path.join(self.dstfolder, self.file_name)
        if os.path.exists(self.dstpath):
            print "Something is wrong: This file already exists. Exiting so you can fix stuff."
            sys.exit(1)
        
        # Write to disk
        else:
            with open(self.dstpath, 'w') as f:
                f.write(self.input_text)
