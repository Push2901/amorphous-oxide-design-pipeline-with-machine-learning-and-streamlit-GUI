import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
from layer1_network.topology import build_topology



# Assign ideal bond lengths

from layer1_network.generator import generate_atoms
from layer1_network.bonding import build_bond_graph
from layer1_network.hydrogen import add_hydrogen
from layer1_network.analysis import atom_counts, radial_distribution

os.makedirs("outputs/structures", exist_ok=True)
os.makedirs("outputs/figures", exist_ok=True)

# --- Generate structure
positions, species = generate_atoms(n_si=150, disorder=0.4)
G = build_topology(species)
for i, j in G.edges():
    G.edges[i, j]["distance"] = 1.6
positions, species, G = add_hydrogen(G, positions, species, h_fraction=0.2)

# --- Save structure
np.save("outputs/structures/positions.npy", positions)
np.save("outputs/structures/species.npy", np.array(species))

# --- Analysis
coord = atom_counts(G)
print("Atom counts:", coord)

r, g = radial_distribution(positions)

# --- Save RDF plot
plt.figure()
plt.plot(r, g)
plt.xlabel("r")
plt.ylabel("g(r)")
plt.title("Radial Distribution Function (a-SiOxHy)")
plt.savefig("outputs/figures/rdf.png", dpi=300)
plt.close()

print("Layer 1 complete. Outputs saved.")

# ---- Export atoms for C code
with open("layer2_energy/atoms.txt", "w") as f:
    f.write(f"{len(positions)}\n")
    for pos, sp in zip(positions, species):
        f.write(f"{sp[0]} {pos[0]} {pos[1]} {pos[2]}\n")


with open("outputs/structures/bond_graph.pkl", "wb") as f:
    pickle.dump(G, f)

print("Bond graph saved.")
print("Number of bonds:", G.number_of_edges())

