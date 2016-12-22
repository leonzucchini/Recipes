"""
Crawl through recipe pages and parse data to database
"""

import os
import requests
import grequests
import pandas as pd
from tools import (
    get_user_agent
)

def main():

    # Get links for supporting files
    link_list_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/03_Data/link_data.csv"
    user_agents_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/config/user_agents.txt"

    # Page link from page link database
    links = pd.read_csv(link_list_path)[['url']].values.tolist()
    links = [item for sublist in links for item in sublist] # Flatten list of lists
    num_links = len(links)

    iter = 5
    i = 0
    these_links = links[i:(i+iter)]
    # print these_links
    # Select user-agents from list (downloaded)
    user_agent_list = get_user_agent.user_agent_list(user_agents_path)
    uas = get_user_agent.select_user_agents(user_agent_list, iter)

    # Open several pages at once using grequests
    # Parse information from page
    # Store to database
    # Store information on progress

    # Open page using user-agent (IP masking?)
    rs = (grequests.get(u) for u in these_links)
    grm = grequests.map(rs)
    print grm
    # response = requests.get(these_links[0])
    # headers = "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4")
    # print response


main()