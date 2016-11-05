# import sys, requests
# from py2neo import *
import os
# import datetime
# import time
# import json

import GetInput
# import GetResponse
# import SetupFolder
# import WriteObject
# import ReportProgress

def setup(input_folder_name):

    # Pick up preferences from preference file
    ui = GetInput.UserInput()
    ui.getFileNames(input_folder_name)

    # prefs = GetInput.InputFile(input_folder_name)
    print ui.filenames
    # setup.set_cwd() # Set working dir as specified in prefs file
    # setup.create_dirpaths() # Create directories for output and pass warnings if they exist

    # # Pick up URLs from a local file
    # with open(setup.paths['category_links'], "r") as f:
    #     url_dict = json.load(f)
    # url_keys = url_dict.keys()

    # # Prepare folder for saving
    # print setup.prefs['_linkFiles']
    # output_file = WriteObject()
    # output_file.check_folder(debug = True)

# id = 0
# timer = ProgressReport()

# for url_key in url_keys:
    
#     url = url_dict[url_key]
#     timer.report()

#     # Use GetResponse to get response from server using URL
#     html_response = GetResponse().tryRequest(url)
#     if html_response.get_error:
#         print "HTML Error"
#         print html_response.response
#     else:
#         html_text = html_response.response

#         # Store html text in local file
#         id += 1
        
#         file_name = prefs["link_output_file_prefix"] + "_" + str(id) + "_" + \
#                     url_key + "_" + str(date.today()) + ".txt"
    
#         output_file.write_file(html_text, file_name)

def main():
    filepath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/recipes/_input/"
    setup(filepath)

if __name__ == '__main__':
    main()