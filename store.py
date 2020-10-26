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
        neo4jUrl = os.environ.get(r'NEO4J_URL', r'localhost:7474/db/data/')

    authenticate(neo4jUrl, r"neo4j", r"password")
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

def store_category_info(graph, category_parsing_result):
    """Store the result of parsing a category page to the database. 
    Argument: Dictionary of dictionaries (results for a page containing many recipes).
    Returns: Adds to database, no return
    """

    create_recipes = ""
    create_relationships = ""
    # Loop over outer dictionary (list of recipes)
    for recipe_id, recipe_dict in category_parsing_result.items():

        # Cypher query: Create (unique) recipes
        create_recipes += """
            CREATE UNIQUE (r%s: Recipe {
                id: "%s",
                title: "%s",
                subtitle: "%s",
                url: "%s",
                votes_avg: %s,
                votes_n: %s,
                activationdate: %s,
                preptime: "%s"
            }
            """ %(
                recipe_id,
                recipe_id,
                recipe_dict["title"],
                recipe_dict["subtitle"],
                recipe_dict["url"],
                recipe_dict["votes_avg"],
                recipe_dict["votes_n"],
                recipe_dict["activationdate"],
                recipe_dict["preptime"]
            )
        # Cypher query: Create (unique) relationships
        # create_relationships += """
        #         MATCH (r: Recipe {id: %s})
        #         CREATE UNIQUE (r)--[:CATEGORIZED_AS]-->(%s),
        #                       (r)--[:HAS_DIFFICULTY]-->(%s)
        #     """ %(
        #         recipe_id,
        #         recipe_dict["category"],
        #         recipe_dict["difficulty"]
        #     )

        # Run and commit transaction
        # tx = graph.begin()
        # tx.run(create_recipes)
        # # tx.run(create_relationships)
        # tx.commit()

        print create_recipes
        # print create_relationships
        # print recipe_dict.keys()
    return None
