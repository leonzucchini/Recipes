from py2neo import *

authenticate("localhost:7474", "neo4j", "walter01")
graph = Graph()

alice = Node("Person", name="Alice")
graph.create(alice)

#german, speaks = graph.create({"name": "German"}, (alice, "SPEAKS", 0))
#graph.delete_all()
#print order(graph)
