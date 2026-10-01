"""
Exercise: Streamlit — Swiss EV Charging Stations
=================================================
Build an interactive EDA web app for the EV charging stations dataset.

Run with:
    streamlit run exercise_streamlit.py

Local:      http://127.0.0.1:8501
Codespaces: https://<your-codespace-name>-8501.app.github.dev
            (Streamlit binds to 0.0.0.0 automatically — no extra flags needed)

Tasks
-----
1. Load the dataset and display its shape and a preview (st.dataframe).
2. Sidebar: add a multiselect widget to filter by power_type.
3. Sidebar: add a slider to set the number of histogram bins (range 5-80).
4. Show a histogram of power_kw using the selected number of bins.
5. Show a bar chart of the top N cities (let the user choose N via a slider, range 5-20).
6. Show a scatter plot of voltage vs. amperage coloured by power_type.
7. Show summary statistics (st.dataframe) for the filtered dataset.
"""

# pylint: disable=unused-import
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set_theme(style='whitegrid')

# ── Data ──────────────────────────────────────────────────────────────────────
# Task 1: load ../../data/ev_charging_stations.csv
# YOUR CODE HERE


# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title('EDA Settings')

# Task 2: multiselect for power_type
# YOUR CODE HERE

# Task 3: slider for bins
# YOUR CODE HERE

# Task 5: slider for top-N cities
# YOUR CODE HERE

# ── Filter ────────────────────────────────────────────────────────────────────
# YOUR CODE HERE: filter df by selected power types


# ── Main ──────────────────────────────────────────────────────────────────────
st.title('Swiss EV Charging Stations — Interactive EDA')

# Task 1: shape + preview
# YOUR CODE HERE

# Task 4: histogram of power_kw
st.subheader('Distribution of Charging Power (kW)')
# YOUR CODE HERE

# Task 5: top-N cities bar chart
st.subheader('Top Cities by Station Count')
# YOUR CODE HERE

# Task 6: scatter plot voltage vs. amperage
st.subheader('Voltage vs. Amperage by Power Type')
# YOUR CODE HERE

# Task 7: summary statistics
st.subheader('Summary Statistics (filtered dataset)')
# YOUR CODE HERE
