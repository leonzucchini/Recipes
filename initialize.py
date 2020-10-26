"""Intitialize script by getting configuration, setting paths, and getting resources. """

import os
import json
import sys
import shutil

class Config(object):
    """ Configuration for the script. """

    def __init__(self, config_file_name, verbose=True):

        ## Get configuration
        this_folder_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(this_folder_path, config_file_name)
        with open(config_path, "r") as f:
            self.config = json.load(f)

        ## Set output data paths and make folders for raw input
        self.data_path_category_raw = os.path.join(os.path.dirname(this_folder_path),
                                                   self.config["paths"]["data_raw"]["category"])
        self.data_path_page_raw = os.path.join(os.path.dirname(this_folder_path),
                                               self.config["paths"]["data_raw"]["page"])

        make_folder(self.data_path_category_raw, overwrite_option="Append", verbose=verbose)
        make_folder(self.data_path_page_raw, overwrite_option="Append", verbose=verbose)

        ## Set output data paths and make folders for parsed input
        self.data_path_category_parsed = os.path.join(os.path.dirname(this_folder_path),
                                                   self.config["paths"]["data_parsed"]["category"])
        self.data_path_page_parsed = os.path.join(os.path.dirname(this_folder_path),
                                               self.config["paths"]["data_parsed"]["page"])

        make_folder(self.data_path_category_parsed, overwrite_option="Append", verbose=verbose)
        make_folder(self.data_path_page_parsed, overwrite_option="Append", verbose=verbose)

        ## Get resource: Category urls
        category_urls_path = os.path.join(this_folder_path,
                                          self.config["paths"]["resources"]["category_urls"])
        with open(category_urls_path, "r") as f:
            self.category_urls = json.load(f) # dictionary

        ## Get resource: Category urls
        user_agents_path = os.path.join(this_folder_path,
                                        self.config["paths"]["resources"]["user_agents"])
        with open(user_agents_path, "r") as f:
            self.user_agents = f.readlines() # list of strings


def make_folder(folder_path, overwrite_option="Exit", verbose=True):
    """ Make a folder, checking whether it already exists. """

    # If folder does not exist then create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # If it exists then exit, remove and overwrite, or append (=do nothing)
    else:
        if verbose:
            print "The following folder exists: %s" %(folder_path)
        if overwrite_option == "Exit":
            if verbose:
                print "Option 'Exit' set in make_folder, so exiting now."
            sys.exit(1)
        if overwrite_option == "Overwrite":
            if verbose:
                print "Option 'Overwrite' set in make_folder, so overwriting."
            shutil.rmtree(folder_path)
            os.mkdir(folder_path)
        if overwrite_option == "Append":
            if verbose:
                print "Option 'Append' set in make_folder, so doing nothing with the folder."
            pass

    return None
