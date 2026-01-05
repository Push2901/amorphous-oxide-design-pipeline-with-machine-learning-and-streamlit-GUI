import pandas as pd
import os

def load_thickness_data():
    return pd.read_csv(r"C:\Users\DELL\Desktop\Material Swiss nom\Project 3\amorphous_oxide_model\layer4_thickness_java\outputs\thickness_results.csv"
    )

def load_design_rules():
    with open(r"C:\Users\DELL\Desktop\Material Swiss nom\Project 3\amorphous_oxide_model\layer5_ml\outputs\design_rules.txt") as f:
        return f.read()



def assert_exists(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Required file not found: {path}")