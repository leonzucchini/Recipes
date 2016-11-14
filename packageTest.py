import os
from datetime import datetime as dt
# from py2neo import *

from setup import GetInput

def main():
    
    # Define main paths (can be moved to config file later)
    inputfolderpath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes" +\
                    "/02_Code/recipes/_input/"

    # Get setup
    user_input = GetInput.UserInput()
    user_input.getFilePaths(inputfolderpath)

    print user_input.filenames

if __name__ == '__main__':
    main()
