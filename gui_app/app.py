import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from utils import load_thickness_data, load_design_rules

st.set_page_config(
    page_title="Amorphous Oxide Design Explorer",
    layout="wide"
)

st.title("Amorphous Oxide Interlayer Design Explorer")

# ---- Load data
df = load_thickness_data()
rules = load_design_rules()

# ---- Sidebar inputs
st.sidebar.header("Design Parameters")

thickness = st.sidebar.slider(
    "Oxide Thickness (nm)",
    float(df["oxide_thickness"].min()),
    float(df["oxide_thickness"].max()),
    5.0,
    step=0.5
)

# ---- Interpolate failure risk
risk = np.interp(
    thickness,
    df["oxide_thickness"],
    df["failure_risk"]
)

# ---- Plot
fig, ax = plt.subplots()

ax.plot(
    df["oxide_thickness"],
    df["failure_risk"],
    label="Failure Risk Curve"
)

ax.scatter(
    thickness,
    risk,
    color="red",
    label=f"Selected thickness = {thickness} nm"
)

ax.set_xlabel("Oxide Thickness (nm)")
ax.set_ylabel("Failure Risk")
ax.legend()

st.pyplot(fig)

# ---- Results panel
col1, col2 = st.columns(2)

with col1:
    st.subheader("Predicted Outcome")
    st.metric("Failure Risk", f"{risk:.3f}")

with col2:
    st.subheader("Design Rules (ML)")
    st.text(rules)

