"""
Parse information from recipe pages for storage to database
"""

import re
import json
from pyld import jsonld
from bs4 import BeautifulSoup as bs

def parse_recipe_info(text, verbose=True):
    """ Grab html code from a file and parse for information - return dict of dicts. """

    # Open file and parse with BS4
    soup = bs(text.decode("utf-8"), "lxml")

    # Title
    title = soup.title.string.replace(" (Rezept mit Bild)", "").replace(" | Chefkoch.de", "")

    # Info
    info = str(soup.find("script", type="application/ld+json"))
    
    # jsonld.compact(info, "http://schema.org")
    # info_json = json.loads(info)
    # print json.dumps(info_json, indent=4, sort_keys=True)
