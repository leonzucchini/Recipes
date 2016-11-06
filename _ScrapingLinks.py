# import sys, requests
# from py2neo import *
import os
# import datetime
# import time
# import json

from GetInput import UserInput
from SetupFolder import FolderSetup
from createDir import create_dir
from clearUpPyc import clear_up_pyc
# import GetResponse

# import WriteObject
# import ReportProgress

def setup(input_folder_name):

    # Pick up preferences from preference file
    debug = False
    ui = UserInput()
    ui.getFilePaths(input_folder_name)
    ui.links = ui.getDict(ui.filepaths[0]).json
    ui.paths = ui.getDict(ui.filepaths[1]).json
    
    # Change cwd and set up folders for output
    setup = FolderSetup()
    setup.set_cwd(ui.paths['_home']) # Set working dir as specified in prefs file

    ui.paths['_linkFiles'] = os.path.join(ui.paths['_home'], ui.paths['_linkFiles'])
    create_dir( ui.paths['_linkFiles'], debug = True)

    clear_up_pyc(ui.paths['_home'])
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
    inputfilepath = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/recipes/_input/"
    setup(inputfilepath)

if __name__ == '__main__':
    main()