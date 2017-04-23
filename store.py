"""
Store recipe data to neo4j database.
"""

import os
from py2neo import Graph
from py2neo import authenticate

def connect_to_graph(dbUrl=None):
    """Connect to database. """

    if dbUrl:
        neo4jUrl = dbUrl
    else:
        neo4jUrl = os.environ.get('NEO4J_URL', "http://localhost:7474/db/data/")

    authenticate(neo4jUrl, "neo4j", "password")
    graph = Graph(neo4jUrl, secure=False)

    return graph

def store_cagetory_urls(url_dictionary, verbose=True):
    """Store urls of category pages from setup resources (hard-coded). """

    # Connect to graph db
    graph = connect_to_graph()

    # Check if the database has already been populated
    # Note this assumes category urls are be the first entry
    datacheck = graph.data("MATCH (c:Category) RETURN c.name")

    if not datacheck:

        # Build cypher query
        query = ""
        for k, v in url_dictionary.items():
            query += """
            CREATE (%s: Category {name: \"%s\", url: \"%s\"})
            """ %(k, k, v)

        # Complete transaction
        tx = graph.begin()
        tx.run(query)
        tx.commit()

        if verbose:
            print "Cateogry urls added to graph."

    else:
        if verbose:
            print "Graph already contains information. Category urls not added."

    return None

def store_category_info(category_parsing_result):
    """Store the result of parsing a category page to the database. 
    Argument: Dictionary of dictionaries (results for a batch of parsing operations).
    Returns: Adds to database, no return
    """

    pass