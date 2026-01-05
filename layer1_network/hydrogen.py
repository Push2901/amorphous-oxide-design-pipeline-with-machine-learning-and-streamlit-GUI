import numpy as np

def add_hydrogen(
    G,
    positions,
    species,
    h_fraction=0.15,
    seed=0
):
    np.random.seed(seed)

    new_positions = positions.tolist()
    new_species = species.copy()

    oxygen_nodes = [
        n for n, d in G.nodes(data=True)
        if d["element"] == "O" and G.degree(n) == 1
    ]

    n_h = int(len(oxygen_nodes) * h_fraction)

    for o in np.random.choice(oxygen_nodes, size=n_h, replace=False):
        direction = np.random.randn(3)
        direction /= np.linalg.norm(direction)

        h_pos = positions[o] + direction * 1.0
        idx = len(new_positions)

        new_positions.append(h_pos)
        new_species.append("H")

        G.add_node(idx, element="H", pos=h_pos)
        G.add_edge(o, idx, distance=1.0)

    return np.array(new_positions), new_species, G
