"""
Retrieve data from chefkoch pages and store to disk (raw text format).
"""

import os
import sys
import re
import requests
import grequests
import random
from datetime import datetime as dt

def retrieve_category_data(category_urls, folder_path, user_agents,
                           overwrite_option="Exit", short_cycle=True,
                           verbose_get=True, verbose_store=False):
    """
    Crawl through recipe category pages.
    Get HTML, check for errors, store results.
    """

    log = []
    log_path = os.path.join(folder_path, "_retrieve_log.txt")

    # Get urls
    url_tuples = []
    for k, v in category_urls.items():
        test = re.match(r"(.*chefkoch.de/rs/s)\d+(.*)", v)
        url_tuples.append((test.group(1), test.group(2)))

    # Cycle through categories
    for url_tuple in url_tuples:

        # Cycle through URL sub-pages
        SUBPAGE_NO = 0
        SUBPAGE_INCREMENT = 30
        URL_ERROR_COUNT = 0


        # Cycle through increments in URL pages
        while True:

            # Set break points
            if not short_cycle:
                # Full cycle: Break after 5 bad responses
                break_now = URL_ERROR_COUNT > 5
            else:
                # Short cycle for testing: Break after 5 bad responses and max 100 sub-pages
                break_now = URL_ERROR_COUNT > 5 or SUBPAGE_NO > 100
            if break_now:
                break

            # HTTP get request
            subpage_url = "".join([url_tuple[0], str(SUBPAGE_NO), url_tuple[1]])
            user_agent = select_user_agent(user_agents)
            http_response = HTTPresponse(subpage_url, user_agent)

            # Check for get errors
            not_found = re.match(
                "Zu deiner Suchanfrage konnten keine Rezepte gefunden werden.",
                http_response.text)
                # This is chefkoch's 404 response
            if not_found or http_response.error:

                # Log error and add to error count
                log.append(http_response.error_message)
                URL_ERROR_COUNT += 1
                if verbose_get:
                    print http_response.error_message

            else:
                # If no error write text to file
                get_message = " ".join(["Got category sub-page:", subpage_url])
                log.append(get_message)
                file_name = ".".join(
                    ["_".join([url_tuple[1][:-5].replace("/", ""),
                               str(SUBPAGE_NO)]), "txt"])
                file_path = os.path.join(folder_path, file_name)
                store_text(http_response.text, file_path, overwrite_option, verbose=verbose_store)

                if verbose_get:
                    print get_message

            # Increment of 30 due to specific syntax of chefkoch.de category sub-pages
            SUBPAGE_NO += SUBPAGE_INCREMENT

    # Write log to file
    store_text("\n".join(log), log_path, overwrite_option, verbose=verbose_store)


# def retrieve_page_data():

#     """
#     Crawl through recipe pages and parse data to database.
#     """

#     # Get links for supporting files
#     url_list_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/03_Data/link_data.csv"
#     user_agents_path = "/Users/Leon/Documents/02_Research_Learning/Research/Recipes/02_Code/config/user_agents.txt"

#     # Get page url from database
#     # url_list = pd.read_csv(url_list_path)[['url']].values.tolist()
#     # url_list = [item for sublist in url_list for item in sublist] # Flatten list of lists
#     # num_urls = len(url_list)

#     # Select user-agents from list (downloaded)
#     # user_agent_list = get_user_agent.user_agent_list(user_agents_path)

#     ### THIS IS WHERE THE LOOP OVER URLS GOES
#     # Select url and user-agent
#     # url = url_list[2051]
#     # user_agent = get_user_agent.select_user_agent(user_agent_list)
#     url = "http://www.chefkoch.de/rezepte/1651531272966946/Schaschlik-wie-im-Kaukasus-grillen.html"
#     user_agent = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16'}

#     # Open page using randomly selected user-agent
#     response = get_response.HTMLresponse(url, user_agent=user_agent)
#     text = response.text
#     # Note161223: Checked grequests, but not sure how to handle multiple headers with identical keys in dict.
#     parse_recipe_pages.parse_recipe_info(text)


# class HTTPresponse(object):
#     """ Response from trying to get an HTML page, returning error and text. """

#     def __init__(self, url, user_agent):
#         """ Try to get response from URL """

#         self.error = 0
#         self.error_message = ""
#         self.text = ""

#         # Try to get HTML response
#         try:
#             r = requests.get(url, headers=user_agent)
#             r.raise_for_status()
#             self.text = r.text.encode('utf-8')

#         # If error, return error message and flag
#         except requests.exceptions.RequestException as err:
#             self.error = 1
#             self.response = str(err)
#             self.error_message = "".join(["Get error: ", url])


def select_user_agent(agent_list):
    """Select random user agent from pre-loaded list of agents. """

    agent_id = random.randint(0, len(agent_list)-1)
    agent = {"user-agent": agent_list[agent_id].replace("\n", "").replace("\"", "")}
    return agent


def store_text(input_text, file_path, option="Exit", verbose=False):
    """ Write text to disk, checking options if it exists. """

    if not os.path.exists(file_path):
        # If file does not exist create it
        with open(file_path, 'w') as f:
                f.write(input_text)

    else:
        # If file does exist, behave depending on options
        if verbose:
            print "This file already exists: %s" %(file_path)
        if option == "Exit":
            if verbose:
                print "Option 'Exit' selected in 'store_text', so exiting now."
            sys.exit(1)

        elif option == "Append":
            if verbose:
                print "Option 'Append' selected in 'store_text', so appending new text to file."
            with open(file_path, 'a') as f:
                f.write(input_text)

        elif option == "Overwrite":
            if verbose:
                print "Option 'Overwrite' selected in 'store_text', so overwriting file."
            with open(file_path, 'w') as f:
                f.write(input_text)
