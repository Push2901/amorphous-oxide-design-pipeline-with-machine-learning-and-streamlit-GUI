import numpy as np

def build_spring_network(G, positions):
    springs = []

    for i, j, data in G.edges(data=True):
        length0 = data["distance"]
        springs.append({
            "i": i,
            "j": j,
            "l0": length0,
            "k": 1.0  # uniform spring constant
        })

    return springs
