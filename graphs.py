import networkx as nx
	
G = nx.Graph()

G.add_node('C')
G.remove_node('C')
G.add_node('D')
G.add_edges_from([('A','B'), ('C','D'), ('A','C')]);


#getOrdem – retorna a ordem do grafo
print G.order() 

#getNos – retorna os nós do grafo
print G.nodes()

#getGrau(No) – retorna o grau de um grafo
print G.degree()

#getAdjacentes(No) – retorna a lista de nós adjacentes
print G.adjlist_outer_dict_factory();

print G.is_multigraph()
