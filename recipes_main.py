"""
Copyright 2016 Leon Zucchini
Repository: https://github.com/leonzucchini/recipes

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
    - Store information to database

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
    - Stores full html files as raw text files
    - Stores log of http responses
    - Adds data neo4j database with recipe information (inshallah)

THIS IMPLEMENTATION ASSUMES A NEO4J DATABASE IS RUNNING SEPARATELY
"""

import py2neo

import initialize
import store
import retrieve

def main():
    """ Run main script. """

    # Initialize (get config, paths, resources, connect to graph db)
    default_config_file_name = "config.json"
    config = initialize.Config(default_config_file_name, verbose=False)
    graph = store.connect_to_graph()

    # Category pages

    ##  Store urls (from initial input)
    store.store_cagetory_urls(config.category_urls, verbose=False)

    #3 Retrieve data from category pages
    retrieve.retrieve_category_data(
        category_urls=config.category_urls,
        folder_path=config.data_path_category_raw,
        user_agents=config.user_agents,
        overwrite_option="Overwrite",
        verbose_get=True,
        verbose_store=False,
        short_cycle=True)

main()
