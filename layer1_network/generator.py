import numpy as np


def generate_atoms(n_si=100, bond_length=1.6, disorder=0.1, seed=42):
    np.random.seed(seed)

    positions = []
    species = []

    # Place Si atoms on a loose grid
    grid_size = int(np.ceil(n_si ** (1/3)))
    spacing = 3.0

    si_positions = []
    for i in range(n_si):
        x = (i % grid_size) * spacing
        y = ((i // grid_size) % grid_size) * spacing
        z = (i // (grid_size**2)) * spacing
        pos = np.array([x, y, z])
        pos += disorder * np.random.randn(3)
        si_positions.append(pos)
        positions.append(pos)
        species.append("Si")

    # Place O atoms between Si neighbors
    for i in range(0, n_si - 1, 2):
        mid = 0.5 * (si_positions[i] + si_positions[i+1])
        mid += disorder * np.random.randn(3)
        positions.append(mid)
        species.append("O")

    return np.array(positions), species
