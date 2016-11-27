"""
"""
import os
import re
from bs4 import BeautifulSoup as bs
import py2neo as pn 

def parse_info(file_path):
    """ Grab html code from a file and parse for information - return dict of dicts. """

    with open(file_path, "r") as f:
        soup = bs(f.read().decode("utf-8"), "lxml")

    category = re.match(r"g\d+(\w+)_.*", os.path.basename(file_path)).group(1)
    recipes = {}

    search_hits = soup.find_all("li", class_="search-list-item")
    # hit = search_hits[0]

    for hit in search_hits:
    # Parse results in search hit for basic information

        # Recipe ID
        id = hit['id'].replace('recipe-','')
        recipes[id] = {}

        # URL, title, subtitle
        recipes[id]["url"] = "".join(["www.chefkoch.de", hit.a['href']])
        recipes[id]["title"] = hit.a.find("div", class_="search-list-item-title").get_text()
        recipes[id]["subtitle"] = hit.a.find("p", class_="search-list-item-subtitle").get_text().strip()

        # Votes (number and average)
        votes_raw = hit.a.find("span", class_="search-list-item-uservotes-stars")["title"]
        recipes[id]["votes_n"] = re.match(r"(\d*)\s.*?(\d+\.\d+)", votes_raw).group(1)
        recipes[id]["votes_avg"] = re.match(r"(\d*)\s.*?(\d+\.\d+)", votes_raw).group(1,2)

        # Other info
        recipes[id]["difficulty"] = hit.a.find("span", class_="search-list-item-difficulty").get_text()
        recipes[id]["preptime"] = hit.a.find("span", class_="search-list-item-preptime").get_text()
        recipes[id]["activationdate"] = hit.a.find("span", class_="search-list-item-activationdate").get_text()

    return recipes

def neo_dict(dictionary):
    """ Write content of dictionary to graph database as attributes (node = dict name). """
    pass


def main():
    folder_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/03_Data/textFiles/"
    graph = pn.Graph()

    # Get file names from folder  
    file_paths = []
    [file_paths.append(os.path.join(folder_path, fn)) for fn in os.listdir(folder_path)]
    file_paths.pop(0) # Remove log file from list

    # Parse information from files
    fp = file_paths[0]
    page_hits = parse_info(fp)
    print page_hits.items()[0]

main()