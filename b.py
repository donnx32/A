import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_node(7)

g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)

nx.draw(g)

plt.show()