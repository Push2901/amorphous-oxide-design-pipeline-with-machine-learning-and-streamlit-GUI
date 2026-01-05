import numpy as np
import pandas as pd

def build_feature_table():
    # ---- Layer 2: Energy
    with open("layer2_energy/outputs/energy_results.txt") as f:
        energy = float(f.read().split()[-1])

    # ---- Layer 3: Mechanical damage
    mech = pd.read_csv("layer3_mechanics/outputs/stress_strain.csv")
    failure_strain = mech.loc[mech["damage_fraction"] > 0.3, "strain"].min()

    # ---- Layer 4: Thickness sweep
    thick = pd.read_csv("layer4_thickness_java/outputs/thickness_results.csv")

    rows = []
    for _, r in thick.iterrows():
        rows.append({
            "energy": energy,
            "failure_strain": failure_strain,
            "oxide_thickness": r["oxide_thickness"],
            "stiffness": r["stiffness"],
            "failure_risk": r["failure_risk"]
        })

    return pd.DataFrame(rows)
