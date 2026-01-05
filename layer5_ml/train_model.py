from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import numpy as np

def train_model(df):
    X = df[["energy", "failure_strain", "oxide_thickness", "stiffness"]]
    y = df["failure_risk"]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)

    preds = model.predict(X)
    score = r2_score(y, preds)

    return model, score
