#ifndef ENERGY_MODEL_H
#define ENERGY_MODEL_H

typedef struct {
    double x, y, z;
    char element;
} Atom;

double compute_pair_energy(Atom a, Atom b);
double compute_total_energy(Atom* atoms, int n_atoms);

#endif
