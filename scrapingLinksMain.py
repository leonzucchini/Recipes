""" Parse HTML text from chefkoch.de.
"""

import os
from datetime import datetime as dt
# from py2neo import *

from GetInput import UserInput
from setCwd import set_cwd
from createDir import create_dir
from clearUpPyc import clear_up_pyc
from GetResponse import HTMLResponse
from WriteObject import WriteObject
# from ReportProgress import ProgressReport

def setup(inputfolderpath):
    """Pick up project preferences (file paths) from pre-defined json files.
    Set up folders for strong results of html-get requests.

    Arguments: Path to folder with preferences files
    Returns:   user_input of class UserInput
    """
    # Pick up preferences from preference file
    user_input = UserInput()
    user_input.getFilePaths(inputfolderpath)
    user_input.prefs = user_input.get_dict(
        user_input.filepaths['linkscraping_preferences.json']
        ).json
    #user_input.print_prefs('prefs')

    # Set up folders for output
    user_input.folderlinkfiles = os.path.join(
        user_input.prefs['_home'], user_input.prefs['_linkFiles']
        )
    create_dir(user_input.folderlinkfiles, debug=False)

    return user_input

def get_url_text(user_input):
    """Get HTML text from URL using the information passed in user_input object.
    Store to local files.

    Arguemnts: user_input object with at least the following attributes
        --links: Links to urls in json dictionary
        --prefs: Preferences file as dictionary ncluding file path to "error_log"
    Returns:   Nothing, writes to disk
    """

    # URLs from local file
    user_input.links = user_input.get_dict(user_input.filepaths['category_links.json']).json
    #user_input.print_prefs('links')
    url_keys = user_input.links.keys()

    # Set up error log
    error_log = os.path.join(user_input.prefs['_home'], user_input.prefs['error_log'])

    # Setup for loop
    id_number = 0
    # timer = ProgressReport()

    # Loop throrugh URLs
    for url_key in url_keys:
        url = user_input.links[url_key]
        # timer.report()

        # Use GetResponse to get response from server using URL
        html_response = HTMLResponse(url)
        if html_response.get_error:
            with open(error_log, "w") as thisfile:
                line = [str(dt.now()), url_key, url, html_response.response]
                thisfile.write(" ; ".join(line))

                ###
                ### This currently overwrites the log file
                ###
        else:
            # Store html text in local file
            id_number += 1
            output_filename = "_".join([
                'category_html',
                str(id_number), url_key, str(dt.now().date()),
                ".txt"
            ])
            filepath = os.path.join(user_input.folderlinkfiles, output_filename)
            WriteObject(html_response.response, filepath)
            print "Writing: " + filepath

def main():
    """Execute the scripts calling parsing functions above."""

    homepath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/recipes/"
    inputfilepath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes" +\
                    "/02_Code/recipes/_input/"

    user_input = setup(inputfilepath)
    set_cwd(user_input.prefs['_home'])

    get_url_text(user_input)

    clear_up_pyc(homepath)

if __name__ == '__main__':
    main()
