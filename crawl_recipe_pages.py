"""
Crawl through recipe pages and parse data to database.
"""

import os
import requests
import grequests
import pandas as pd
import parse_recipe_pages
from tools import (
    get_user_agent,
    get_response
)

def main():

    # Get links for supporting files
    url_list_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/03_Data/link_data.csv"
    user_agents_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/config/user_agents.txt"

    # Get page url from database
    # url_list = pd.read_csv(url_list_path)[['url']].values.tolist()
    # url_list = [item for sublist in url_list for item in sublist] # Flatten list of lists
    # num_urls = len(url_list)

    # Select user-agents from list (downloaded)
    # user_agent_list = get_user_agent.user_agent_list(user_agents_path)

    ### THIS IS WHERE THE LOOP OVER URLS GOES
    # Select url and user-agent
    # url = url_list[2051]
    # user_agent = get_user_agent.select_user_agent(user_agent_list)
    url = "http://www.chefkoch.de/rezepte/1651531272966946/Schaschlik-wie-im-Kaukasus-grillen.html"
    user_agent = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16'}

    # Open page using randomly selected user-agent
    response = get_response.HTMLresponse(url, user_agent=user_agent)
    text = response.text
    # Note161223: Checked grequests, but not sure how to handle multiple headers with identical keys in dict.
    parse_recipe_pages.parse_recipe_info(text)

main()