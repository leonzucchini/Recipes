"""
Parse stored raw html and
"""

import os
import re
import csv
# import pandas as pd
from bs4 import BeautifulSoup as bs

def parse_category_file(file_path, counter=1, verbose=True):
    """ Grab html code from a file (=category page) and parse for information. Return dict of dicts. """

    this_counter = counter
    # Open file and parse with BS4
    with open(file_path, "r") as f:
        soup = bs(f.read().decode("utf-8"), "lxml")

    # Get category
    category = re.match(r"g\d+(\w.+)_.*", os.path.basename(file_path)).group(1)
    recipes = {}

    search_hits = soup.find_all("li", class_="search-list-item")
    for hit in search_hits:
    # Parse results in search hit for basic information

        try:
            # Recipe ID
            id = hit['id'].replace('recipe-','')
            recipes[id] = {}

            # Info on category and category list page
            recipes[id]["category"] = category
            pNum, rText, sNum = re.match(r".*(g\d+)(.*)_(\d*).*\.(txt)", file_path).group(1,2,3)
            recipes[id]["category_list_page"] = "www.chefkoch.de/rs/s" + sNum + pNum + "/" + rText + ".html"

            # URL, title, subtitle
            recipes[id]["url"] = "".join(["http://www.chefkoch.de", hit.a['href']])
            recipes[id]["title"] = hit.a.find("div", class_="search-list-item-title").get_text().strip().replace("\n","")
            recipes[id]["subtitle"] = hit.a.find("p", class_="search-list-item-subtitle").get_text().strip().replace("\n","")

            # Votes (number and average)
            votes_raw = hit.a.find("span", class_="search-list-item-uservotes-stars")["title"]
            recipes[id]["votes_n"] = re.match(r"^(\d*)\s.*", votes_raw).group(1)
            recipes[id]["votes_avg"] = re.match(r".*\s(.*?)$", votes_raw).group(1)

            # Other info
            recipes[id]["difficulty"] = hit.a.find("span", class_="search-list-item-difficulty").get_text()
            recipes[id]["preptime"] = hit.a.find("span", class_="search-list-item-preptime").get_text()
            recipes[id]["activationdate"] = hit.a.find("span", class_="search-list-item-activationdate").get_text()

            if verbose:
                print file_path + " #" + str(this_counter) + " successfully parsed"

        except Exception:
            if verbose:
                print file_path + " #" + str(this_counter) + " problem with parsing"

        this_counter += 1

    return (recipes, this_counter)


def parse_category_data(input_folder_path, output_folder_path, output_file_name, verbose=False):
    """ 
    Parse an entire folder of category page files (looping over files).
    Store to local csv file in regular intervals.
    """

    # Get file names from folder  
    file_paths = []
    [file_paths.append(os.path.join(input_folder_path, fn)) for fn in os.listdir(input_folder_path)]
    file_paths.pop(0) # Remove log file from list

    # Parse information by looping over files
    COUNTER = 1
    # link_data = []
    output_file_path = os.path.join(output_folder_path, output_file_name)
    for fp in file_paths[:3]:
        (category_data, counter) = parse_category_file(fp, counter=COUNTER, verbose=verbose)

        w = csv.writer(open(output_file_path, "w"))
        for k, v in category_data.items():
            w.writerow([k, v])
        
        # for k, v in category_data.items():
        #     row = pd.Series(v, name=k)
        #     link_data = link_data.append(row)

        bigcounter = (counter-1)/30
        if bigcounter%50 == 0:
            print bigcounter
            # link_data.to_csv(out_path, encoding='utf8') # Interim storage for when I need to stop earlier

    # link_data.to_csv(out_path, encoding='utf8')

    return None
