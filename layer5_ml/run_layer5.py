import os
from layer5_ml.features import build_feature_table
from layer5_ml.train_model import train_model
from layer5_ml.interpret import extract_rules

os.makedirs("layer5_ml/outputs", exist_ok=True)

df = build_feature_table()
df.to_csv("layer5_ml/outputs/feature_table.csv", index=False)

model, score = train_model(df)

with open("layer5_ml/outputs/model_metrics.txt", "w") as f:
    f.write(f"R2 score: {score:.3f}\n")

rules = extract_rules(model, df)

with open("layer5_ml/outputs/design_rules.txt", "w") as f:
    f.write(rules)

print("Layer 5 complete. Design rules extracted.")
