#include <math.h>
#include "energy_model.h"

/* Equilibrium distances (Å, abstracted) */
double r0(char a, char b) {
    if ((a=='S' && b=='O') || (a=='O' && b=='S')) return 1.6;
    if ((a=='O' && b=='H') || (a=='H' && b=='O')) return 1.0;
    return 2.5;
}

/* Force constants */
double k(char a, char b) {
    if ((a=='S' && b=='O') || (a=='O' && b=='S')) return 10.0;
    if ((a=='O' && b=='H') || (a=='H' && b=='O')) return 5.0;
    return 1.0;
}

double distance(Atom a, Atom b) {
    return sqrt(
        (a.x-b.x)*(a.x-b.x) +
        (a.y-b.y)*(a.y-b.y) +
        (a.z-b.z)*(a.z-b.z)
    );
}

/* Harmonic bond energy */
double compute_pair_energy(Atom a, Atom b) {
    double r = distance(a, b);
    double dr = r - r0(a.element, b.element);
    return 0.5 * k(a.element, b.element) * dr * dr;
}

/* Total system energy */
double compute_total_energy(Atom* atoms, int n_atoms) {
    double E = 0.0;
    for (int i = 0; i < n_atoms; i++) {
        for (int j = i + 1; j < n_atoms; j++) {
            E += compute_pair_energy(atoms[i], atoms[j]);
        }
    }
    return E;
}
