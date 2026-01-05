import networkx as nx

def build_topology(species, bond_length=1.6):
    

    G = nx.Graph()

    for i, sp in enumerate(species):
        G.add_node(i, element=sp)

    si_indices = [i for i, sp in enumerate(species) if sp == "Si"]
    o_indices  = [i for i, sp in enumerate(species) if sp == "O"]

    for o, (si1, si2) in zip(o_indices, zip(si_indices[::2], si_indices[1::2])):
        G.add_edge(o, si1, distance=bond_length)
        G.add_edge(o, si2, distance=bond_length)

    return G
