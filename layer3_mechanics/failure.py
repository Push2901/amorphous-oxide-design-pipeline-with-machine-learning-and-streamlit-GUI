import numpy as np

def evaluate_damage(springs, positions, strain_threshold=0.2):
    broken = 0

    for s in springs:
        i, j = s["i"], s["j"]
        l0 = s["l0"]

        l = np.linalg.norm(positions[i] - positions[j])
        if (l - l0) / l0 > strain_threshold:
            broken += 1
    if len(springs) == 0:
        raise RuntimeError("No springs found — bond network is empty.")

    damage_fraction = broken / len(springs)
    return damage_fraction
