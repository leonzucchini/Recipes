""" Get configuration parameters from config files. """
import os
import sys
import json

def get_config(file_path, print_config=False):
    """ Retrieve user input in json format. """

    # Check path exists
    if not os.path.exists(file_path):
        print 'Error with configuration: Configuration file does not exist:\n%s' %(file_path)
        sys.exit(1)
    else:
        pass

    # Retrieve configuration from json file, return dict
    with open(file_path, "r") as f:
        config = json.load(f)

    # Print nicely as json
    if print_config:
        print json.dumps(config, indent=4, sort_keys=True)

    return config
