import os
import sys

def write_text(input_text, file_path, option="Exit"):
    """ Write text to disk checking options if it exists """

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
                f.write(input_text)

    else:

        if option == "Exit":
            print "Write file error: This file already exists.\n %s \nExiting..." %(file_path)
            sys.exit(1)

        elif option == "Append":
            with open(file_path, 'a') as f:
                f.write(input_text)

        elif option == "Overwrite":
            with open(file_path, 'w') as f:
                f.write(input_text)
