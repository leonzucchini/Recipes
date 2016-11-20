""" Get links for recipes at chefkoch.de """

import os
from datetime import datetime as dt
# # from py2neo import *

from setup import GetInput, createDir, setCwd, clearUpPyc, WriteObject
from scrape import GetResponse
from parse import parse_links

def setup(inputfolderpath):
    """ Get file paths and set up folders for results """
    # Pick up preferences from preference file
    user_input = GetInput.UserInput()
    user_input.getFilePaths(inputfolderpath)
    user_input.prefs = user_input.get_dict(
        user_input.filepaths['linkscraping_preferences.json']
        ).json
    #user_input.print_prefs('prefs')

    # Set up folders for output
    user_input.folderlinkfiles = os.path.join(
        user_input.prefs['_home'], user_input.prefs['_linkFiles']
        )
    createDir.create_dir(user_input.folderlinkfiles, debug=True)

    return user_input

def get_url_text(user_input):
    """Get HTML text from predefined URLs and store to local files """

    # URLs from local file
    user_input.links = user_input.get_dict(user_input.filepaths['category_links.json']).json
    #user_input.print_prefs('links')
    url_keys = user_input.links.keys()

    # Set up error log
    error_log = os.path.join(user_input.prefs['_home'], user_input.prefs['error_log'])

    # Setup for loop

    # Loop throrugh URLs
    for url_key in url_keys:
        url = user_input.links[url_key]

        # Use GetResponse to get response from server using URL
        html_response = GetResponse.HTMLResponse(url)
        if html_response.get_error:
            # Check for errors
            with open(error_log, "w") as thisfile:
                line = [str(dt.now()), url_key, url, html_response.response]
                thisfile.write(" ; ".join(line))

                ###
                ### This currently overwrites the log file
                ###
        else:
            # Store html text in local file
            output_filename = "_".join([
                'category_html',
                url_key, str(dt.now().date()),
                ".txt"
            ])
            filepath = os.path.join(user_input.folderlinkfiles, output_filename)
            WriteObject.WriteObject(html_response.response, filepath)
            print "Writing: " + filepath

def main():
    """Execute the scripts calling parsing functions above."""

    # Define main paths (can be moved to config file later)
    homepath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/recipes/"
    inputfilepath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes" +\
                    "/02_Code/recipes/_input/"

    # Get setup
    user_input = setup(inputfilepath)
    setCwd.set_cwd(user_input.prefs['_home'])

    # Grab urls
    catpath = user_input.filepaths['category_links.json']
    categories = GetInput.UserInput().get_dict(catpath).json
    category_dict = parse_links.get_category_framework(categories)
    url_list = parse_links.crawl_urls(category_dict)
    print url_list

    # Clear up pyc files
    clearUpPyc.clear_up_pyc(homepath)

if __name__ == '__main__':
    main()
