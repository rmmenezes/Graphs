## Welcome to Project in NetworkX PYTHON
This project is an activity carried out in the course of computer science in the field of graphs.

NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

### Install
Install the latest version of NetworkX::

    $ pip install networkx

Install with all optional dependencies::

    $ pip install networkx[all]

For additional details, please see `INSTALL.rst`.

### Simple example

Find the shortest path between two nodes in an undirected graph::

    >>> import networkx as nx
    >>> G = nx.Graph()
    >>> G.add_edge('A', 'B', weight=4)
    >>> G.add_edge('B', 'D', weight=2)
    >>> G.add_edge('A', 'C', weight=3)
    >>> G.add_edge('C', 'D', weight=4)
    >>> nx.shortest_path(G, 'A', 'D', weight='weight')
    ['A', 'B', 'D']

### Support or Contact

[contact support Networkx](https://networkx.github.io/)

[Profile GitHub rmmenezes](https://github.com/rmmenezes)

[Profile GitHub rmmenezes](https://github.com/jonfel)
