import numpy as np

def apply_strain(positions, strain):
    strained = positions.copy()
    strained[:, 0] *= (1 + strain)  # uniaxial x-strain
    return strained
