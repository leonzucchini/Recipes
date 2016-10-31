import sys, os, requests
from py2neo import *

from GetResponse import *
from UrlListFromFile import *

# Define main()
def main():
  """
  Download and store text from URL to specified directory. 
  Several dependencies that have yet to be written.
  Could also call prefs.py instead of passing arguments via the command
  line.
  """

  # Pick up URLs from a local file
  url_list = UrlList("LinkFiles/category_links.txt")
  print url_list.urls

  # Use GetResponse to get response from server using URL
  url = "http://www.chefkoch.de/rs/s0g47/Suessspeisen-Backen-Rezepte.html"
  a = GetResponse().tryRequest(url)





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

# Boilerplate to call main()
if __name__ == '__main__':
  main()