import numpy as np
from scipy.spatial.distance import pdist

# def coordination_numbers(G):
#     stats = {}
#     for _, d in G.nodes(data=True):
#         el = d["element"]
#         stats.setdefault(el, 0)
#         stats[el] += 1
#     return stats

def atom_counts(G):
    counts = {}
    for _, d in G.nodes(data=True):
        el = d["element"]
        counts.setdefault(el, 0)
        counts[el] += 1
    return counts


def radial_distribution(positions, bins=100):
    dists = pdist(positions)
    hist, edges = np.histogram(dists, bins=bins, density=True)
    r = 0.5 * (edges[:-1] + edges[1:])
    return r, hist
