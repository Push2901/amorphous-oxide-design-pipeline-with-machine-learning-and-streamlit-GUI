import numpy as np
import matplotlib.pyplot as plt
import csv
import os

from layer1_network.bonding import build_bond_graph
from layer3_mechanics.springs import build_spring_network
from layer3_mechanics.loading import apply_strain
from layer3_mechanics.failure import evaluate_damage

import pickle


# ---- Resolve project root explicitly
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STRUCT_DIR = os.path.join(PROJECT_ROOT, "outputs", "structures")

# ---- Load data
positions = np.load(os.path.join(STRUCT_DIR, "positions.npy"))
species = np.load(os.path.join(STRUCT_DIR, "species.npy"), allow_pickle=True)

with open(os.path.join(STRUCT_DIR, "bond_graph.pkl"), "rb") as f:
    G = pickle.load(f)

print("Loaded graph with edges:", G.number_of_edges())

# --- Load Layer 1 structure
# positions = np.load("outputs/structures/positions.npy")
# species = np.load("outputs/structures/species.npy", allow_pickle=True)

# G = build_bond_graph(positions, species)
springs = build_spring_network(G, positions)

os.makedirs("layer3_mechanics/outputs", exist_ok=True)

strains = np.linspace(0, 0.5, 50)
damage = []

for eps in strains:
    strained_pos = apply_strain(positions, eps)
    d = evaluate_damage(springs, strained_pos)
    damage.append(d)

# --- Save CSV
with open("layer3_mechanics/outputs/stress_strain.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["strain", "damage_fraction"])
    for e, d in zip(strains, damage):
        writer.writerow([e, d])

# --- Plot
plt.plot(strains, damage)
plt.xlabel("Strain")
plt.ylabel("Damage fraction")
plt.title("Failure evolution in amorphous network")
plt.savefig("layer3_mechanics/outputs/failure_plot.png", dpi=300)
plt.close()

print("Layer 3 complete. Mechanical failure simulated.")
