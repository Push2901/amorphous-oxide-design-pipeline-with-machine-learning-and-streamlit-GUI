import numpy as np

def extract_rules(model, df):
    importances = model.feature_importances_
    features = df.columns[:-1]

    ranked = sorted(
        zip(features, importances),
        key=lambda x: x[1],
        reverse=True
    )

    best = df.loc[df["failure_risk"].idxmin()]

    rules = []
    rules.append("Feature importance ranking:")
    for f, w in ranked:
        rules.append(f"  {f}: {w:.3f}")

    rules.append("\nOptimal design point:")
    for k, v in best.items():
        rules.append(f"  {k}: {v}")

    return "\n".join(rules)
