# import sys, os, requests
# from py2neo import *
import os
from datetime import datetime

from GetResponse import GetResponse
from PathListFromFile import PathList
from TextToFile import TextFile

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
    url_list = PathList(category_list).paths

    # for url in url_list:
    #     # Use GetResponse to get response from server using URL
    #     html_text = GetResponse().tryRequest(url)
    #     print html_text.response[:100]

    # Store html text in local file
    fileDst = prefs["link_output_directory"]
    fileName = "output2.txt" #prefs["link_output_file_prefix"]
    text_file = TextFile("def", fileDst, fileName).writeToFile()
    # print text_file.dstfolder

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
