import os
import sys
import re
from bs4 import BeautifulSoup as bs

from GetInput import UserInput
from GetResponse import HTMLResponse

def get_category_framework(category_dict):
    """Cycle through dictionary of link categories and retrieve html files.
    Return list of tuples (NOT dictionary)."""
    url_parts = []
    for k, v in category_dict.items():
        test = re.match(r"(.*chefkoch.de/rs/s)\d+(.*)", v)
        url_parts.append((test.group(1), test.group(2)))
    return url_parts

def crawl_urls(cat_list):
    """Crawl through URLs in framework (list of tuples)
    Loop over values of varying parts of URLs and
    save texts to local folder.

    Argument: category framework as defined in
    get_category_framework.
    """

    for url_tuple in cat_list:
        # Cycle through cateogry patterns
        url_list = []
        url_increment = 0
        url_error_count = 0

        while True:
            # Cycle through increments in URL pages
            url_increment += 30
            url = url_tuple[0] + str(url_increment) + url_tuple[1]

            if url_error_count > 5 or url_increment > 500:
                break

            html_response = HTMLResponse(url)
            if check_url_error(html_response):
                pass
                # if page not known add one to the increment, break after 5
                url_error_count += 1
                break
            else:
                html_response = HTMLResponse(url)
                url_list.append(url)

        return url_list

def check_url_error(html_response):
    """Check the response from a get request is valid.
    Check also that chefkoch knows the page using their
    'Page not known' text.
    Return tuple with HTML error and page not found
    """
    url_error = 0
    not_found_text = "Zu deiner Suchanfrage konnten " \
                     + "keine Rezepte gefunden werden."
    not_found = re.match(not_found_text, html_response.response)
    if not_found or html_response.get_error:
         url_error = 1
    return url_error