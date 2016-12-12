"""
"""
import os
import re
from bs4 import BeautifulSoup as bs
import pandas as pd
# import py2neo as pn

def parse_info(file_path):
    """ Grab html code from a file and parse for information - return dict of dicts. """

    with open(file_path, "r") as f:
        soup = bs(f.read().decode("utf-8"), "lxml")

    category = re.match(r"g\d+(\w+)_.*", os.path.basename(file_path)).group(1)
    recipes = {}

    search_hits = soup.find_all("li", class_="search-list-item")
    
    issue_counter = 1
    for hit in search_hits:
    # Parse results in search hit for basic information
        try:
            # Recipe ID
            id = hit['id'].replace('recipe-','')
            recipes[id] = {}

            # URL, title, subtitle
            recipes[id]["url"] = "".join(["www.chefkoch.de", hit.a['href']])
            recipes[id]["title"] = hit.a.find("div", class_="search-list-item-title").get_text().strip().replace("\n","")
            recipes[id]["subtitle"] = hit.a.find("p", class_="search-list-item-subtitle").get_text().strip().replace("\n","")

            # Votes (number and average)
            votes_raw = hit.a.find("span", class_="search-list-item-uservotes-stars")["title"]
            recipes[id]["votes_n"] = re.match(r"(\d*)\s.*?(\d+\.\d+)", votes_raw).group(1)
            recipes[id]["votes_avg"] = re.match(r"(\d*)\s.*?(\d+\.\d+)", votes_raw).group(2)

            # Other info
            recipes[id]["difficulty"] = hit.a.find("span", class_="search-list-item-difficulty").get_text()
            recipes[id]["preptime"] = hit.a.find("span", class_="search-list-item-preptime").get_text()
            recipes[id]["activationdate"] = hit.a.find("span", class_="search-list-item-activationdate").get_text()
        except Exception:
            print "Problem with parsing #" + str(issue_counter)
            issue_counter += 1

    return recipes

# def neo_dict(dictionary):
#     """ Write content of dictionary to graph database as attributes (node = dict name). """
#     pass

def main():
    folder_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/03_Data/textFiles/"
    out_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/03_Data/link_data.csv"

    # Get file names from folder  
    file_paths = []
    [file_paths.append(os.path.join(folder_path, fn)) for fn in os.listdir(folder_path)]
    file_paths.pop(0) # Remove log file from list

    # Parse information by looping over files
    # Store to pandas dict and write info for first analysis (w/o neo2j database)
    link_data = pd.DataFrame()
    for fp in file_paths:
        page_hits = parse_info(fp)
        for k, v in page_hits.items():
            row = pd.Series(v, name=k)
            link_data = link_data.append(row)
        
    link_data.to_csv(out_path, encoding='utf8')

main()