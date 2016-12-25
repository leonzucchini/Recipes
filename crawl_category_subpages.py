# Copyright 2016 Leon Zucchini
#
# This file is part of the "recipes" project
# Repository: https://github.com/leonzucchini/recipes

import os
import re
from datetime import datetime as dt

from tools import (
    get_input,
    get_response,
    make_folders,
    remove_pyc,
    write_text
)

def crawl_categories(category_dict, folder_path,
                log_name, log_option="Exit", files_option="Exit",
                verbose=False, short_cycle=False):
    """
    Get syntax framework for URLs of recipe category sub-pages (containing links to recipes).
    Crawl through recipe category sub-pages (loop over varying parts of URLs). 
    Get HTML, check for errors, and store results.    
    """

    log_list = []
    log_path = os.path.join(folder_path, log_name)

    # Get syntax framework
    url_tuples = []
    for k, v in category_dict.items():
        test = re.match(r"(.*chefkoch.de/rs/s)\d+(.*)", v)
        url_tuples.append((test.group(1), test.group(2)))

    for url_tuple in url_tuples: 

        # Cycle through URL sub-pages
        SUBPAGE_NO = 0
        URL_ERROR_COUNT = 0

        while True:
            # Cycle through increments in URL pages

            # Set break points
            break_now = URL_ERROR_COUNT > 5 # Break after 5 bad responses
            if short_cycle:
                break_now = URL_ERROR_COUNT > 5 or SUBPAGE_NO > 100 # Use shorter cycle for testing
            if break_now:
                break

            else:
                # Get response
                cat_url = "".join([url_tuple[0], str(SUBPAGE_NO), url_tuple[1]])
                html_response = get_response.HTMLresponse(cat_url)

                # Check for html get errors
                not_found = re.match("Zu deiner Suchanfrage konnten keine Rezepte gefunden werden.", html_response.text)
                if not_found or html_response.error:

                    # Add to error count and log
                    URL_ERROR_COUNT += 1
                    log_list.append(html_response.error_message)
                    if verbose:
                        print html_response.error_message

                else:
                    # If no error write text to file
                    get_message = " ".join(["Got category sub-page:", cat_url])
                    log_list.append(get_message)
                    file_name = ".".join(["_".join([url_tuple[1][:-5].replace("/",""), str(SUBPAGE_NO)]), "txt"])
                    file_path = os.path.join(folder_path, file_name)
                    write_text.write_text(html_response.text, file_path, files_option)

                    if verbose:
                        print get_message

                # Increment of 30 due to specific syntax of chefkoch.de category sub-pages
                SUBPAGE_NO += 30 

    # Write log to file
    write_text.write_text("\n".join(log_list), log_path, log_option)

def main():
    """ Crawl through the chefkoch.de recipe category sub-pages and store HTML to files.
        Note:
            Recipes in chefkoch.de are sorted into categories (e.g. baking).
            Each category has many sub-pages containing links to 30 recipes.
            This file crawles through and stores the sub-pages so I can parse for the links later. 
    """

    # Define path to configs 
    config_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/config/config.json"
    
    # Get configs and set up paths
    config = get_input.get_input(config_path, print_config=False)
    output_path = os.path.join(config['_home'], config['_linkFiles'])
    make_folders.make_output_folder(output_path, debug=False) 

    # Parse cateogry urls and store pages to local files
    categories_path = os.path.join(config['_home'], config['category_links'])
    categories_links = get_input.get_input(categories_path, print_config=False)
    crawl_categories(
        categories_links, output_path,
        log_name = "_category_log.txt", log_option="Append",
        files_option="Exit", verbose=True, short_cycle=False
        )

    # Clear up pyc files
    remove_pyc.remove_pyc(config['_home'])
    print "All done!"

main()
