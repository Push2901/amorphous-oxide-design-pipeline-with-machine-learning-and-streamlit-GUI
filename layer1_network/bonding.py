import numpy as np
import networkx as nx
from scipy.spatial import cKDTree

CUTOFFS = {
    ("Si", "O"): 2.0,
    ("O", "H"): 1.2,
}

def build_bond_graph(positions, species):
    G = nx.Graph()
    tree = cKDTree(positions)

    for i, (pos, sp) in enumerate(zip(positions, species)):
        G.add_node(i, element=sp, pos=pos)

    for i, j in tree.query_pairs(r=2.5):
        a, b = species[i], species[j]
        key = tuple(sorted((a, b)))

        if key in CUTOFFS:
            dist = np.linalg.norm(positions[i] - positions[j])
            if dist <= CUTOFFS[key]:
                G.add_edge(i, j, distance=dist)

    return G
