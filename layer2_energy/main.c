#include <stdio.h>
#include <stdlib.h>
#include "energy_model.h"

#include <direct.h>


int main() {
    char cwd[1024];
    getcwd(cwd, sizeof(cwd));
    printf("CWD: %s\n", cwd);
    // FILE *fp = fopen("atoms.txt", "r");
    FILE *fp = fopen("atoms.txt", "r");

    if (!fp) {
        printf("Could not open atoms.txt\n");
        return 1;
    }

    int n;
    fscanf(fp, "%d", &n);

    Atom *atoms = malloc(sizeof(Atom) * n);

    for (int i = 0; i < n; i++) {
        fscanf(fp, " %c %lf %lf %lf",
               &atoms[i].element,
               &atoms[i].x,
               &atoms[i].y,
               &atoms[i].z);
    }

    fclose(fp);

    double E = compute_total_energy(atoms, n);

    FILE *out = fopen("outputs/energy_results.txt", "w");

    fprintf(out, "Total energy: %.6f\n", E);
    fclose(out);

    printf("Total energy computed: %.6f\n", E);

    free(atoms);
    return 0;
}
