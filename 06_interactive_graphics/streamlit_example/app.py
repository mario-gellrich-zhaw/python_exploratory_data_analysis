"""
Streamlit EDA app for apartment data.

Usage:
    pip install streamlit matplotlib seaborn pandas
    streamlit run app.py
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# ── Data ──────────────────────────────────────────────────────────────────────
df = pd.read_csv(
    "../../../data/apartments_data_enriched_cleaned.csv", sep=";", encoding="utf-8"
)
NUM_COLS = ["price", "area", "rooms"]

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title("EDA Settings")
variable = st.sidebar.selectbox("Variable", NUM_COLS, index=0)
bins = st.sidebar.slider("Number of bins", min_value=10, max_value=100, value=40, step=5)
show_kde = st.sidebar.checkbox("Show KDE", value=True)
luxurious_filter = st.sidebar.multiselect(
    "Luxurious", options=sorted(df["luxurious"].unique()), default=sorted(df["luxurious"].unique())
)

# ── Filter ────────────────────────────────────────────────────────────────────
df_filtered = df[df["luxurious"].isin(luxurious_filter)]

# ── Main ──────────────────────────────────────────────────────────────────────
st.title("Apartment Data — Interactive EDA")
st.write(f"**Rows shown:** {len(df_filtered):,} / {len(df):,}")

# Histogram
st.subheader(f"Distribution of {variable.capitalize()}")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(data=df_filtered, x=variable, bins=bins, kde=show_kde, ax=ax)
ax.set_xlabel(variable.capitalize())
st.pyplot(fig)

# Summary statistics
st.subheader("Summary Statistics")
st.dataframe(df_filtered[NUM_COLS].describe().round(2))

# Scatter plot
st.subheader("Scatter Plot: Price vs. Area")
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df_filtered.sample(min(500, len(df_filtered)), random_state=42),
                x="area", y="price", hue="luxurious", alpha=0.5, ax=ax2)
st.pyplot(fig2)
