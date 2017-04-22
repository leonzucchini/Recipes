"""
Retrieve, parse, and store information from chefkoch.de.

Data sources
- Category pages
    Accessed using hard-coded urls.
    Contain links and basic recipe information, including urls for recipe pages.
- Recipe pages
    Accesssed using urls from category pages.
    Contain detailed recipe information.

Modules
- Initialize
    - Import preferences and resources
    - Initialize storage (neo4j)
- Prepare data source (for each data source)
    - Get urls
    - Get parsing structure
- Process data source (for each data source, loop over urls)
    - Open url
    - Parse information
    - Add information to database

Arguments:
    - Resources (string)
        Location of category urls and user agents
        Default: "resources/" at same level as this script
    - Modules (json)
        Which modules to run on which data sources
        Default: none
    - Storage (string)
        Location of neo4j database
        Default: "03_Data/" at one folder level above this script

Returns:
    - neo4j database with recipe information (inshallah)
"""

import os
import json

def main():
    """ Run main script. """

    # Initialize

    ## Get configuration
    DEFAULT_CONFIG_FILE_NAME = "config.json"
    this_folder_path = os.path.dirname(os.path.abspath(__file__))
    
    config_path = os.path.join(this_folder_path, DEFAULT_CONFIG_FILE_NAME)
    with open(config_path, "r") as f:
        config = json.load(f)

    ## Set output data path
    data_path = os.path.join(os.path.dirname(this_folder_path), config["paths"]["data"])

    ## Get resources: Category urls and user agents
    category_urls_path = os.path.join(this_folder_path,
                                      config["paths"]["resources"]["category_urls"])
    with open(category_urls_path, "r") as f:
        category_urls = json.load(f) # dictionary

    user_agents_path = os.path.join(this_folder_path, config["paths"]["resources"]["user_agents"])
    with open(user_agents_path, "r") as f:
        user_agents = f.readlines() # list of strings

main()
