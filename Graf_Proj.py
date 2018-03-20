import networkx as nx

G = nx.Graph()

G.add_node('C')
#G.remove_node('C')
G.add_node('D')
G.add_edges_from([('A','B'), ('C','D'), ('A','C')]);
print G.is_multigraph()
print G.order()
print G.nodes()
print G.degree()
print G.adjlist_outer_dict_factory();
