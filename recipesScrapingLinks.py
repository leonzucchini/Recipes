# import sys, os, requests
# from py2neo import *
import os
from datetime import date

from GetResponse import GetResponse
from PathListFromFile import PathList
from WriteObject import *

# Define main()
def main():
    """
    Download and store text from URL to specified directory.
    Several dependencies that have yet to be written.
    Could also call prefs.py instead of passing arguments via the command
    line.
    """

    linkscraping_prefs = "linkscraping_preferences.txt" # note relative path!

    # Pick up preferences from preference file
    prefs = PathList(linkscraping_prefs).split_to_dict()

    category_list = prefs["category_list"]

    # Pick up URLs from a local file
    url_dict = PathList(category_list).split_to_dict()
    url_keys = url_dict.keys()

    # Prepare folder for saving
    output_file = WriteObject(prefs["link_output_directory"])
    output_file.check_folder()

    id = 0
    for url_key in url_keys:
        
        url = url_dict[url_key]

        # Use GetResponse to get response from server using URL
        html_response = GetResponse().tryRequest(url)
        if html_response.get_error:
            print "HTML Error"
            print html_response.response
        else:
            html_text = html_response.response

            # Store html text in local file
            id += 1
            
            file_name = prefs["link_output_file_prefix"] + "_" + str(id) + "_" + \
                        url_key + "_" + str(date.today()) + ".txt"
        
            output_file.write_file(html_text, file_name)

# Boilerplate to call main()
if __name__ == '__main__':
    main()

  # # Make a list of command line arguments ommitting the script itself
  # args = sys.argv[1:]

  # # Return usage and exit if no arguments are passed
  # if not args:
  #   print 'Usage: todir [--append append] [--inputfile inputfile]'
  #   sys.exit(1)

  # else:
  #   # Pick up target dirctory and shorten arguments
  #   todir = args[0]
  #   args = args[1:]

    #############
    ### append and inputfile not yet implemented
    ### a prompt to check on whether the download should really start would be good
    #############
