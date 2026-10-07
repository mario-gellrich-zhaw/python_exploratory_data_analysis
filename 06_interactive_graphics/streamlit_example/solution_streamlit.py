"""
Solution: Streamlit — Swiss EV Charging Stations
=================================================
Run with:
    streamlit run solution_streamlit.py

Local:      http://127.0.0.1:8501
Codespaces: https://<your-codespace-name>-8501.app.github.dev
            (Streamlit binds to 0.0.0.0 automatically — no extra flags needed)
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

sns.set_theme(style='whitegrid')

# ── Data ──────────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    """Load and cache the EV charging stations dataset."""
    return pd.read_csv('../../data/ev_charging_stations.csv')

df = load_data()
NUM_COLS = ['power_kw', 'amperage', 'voltage']

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title('EDA Settings')

power_types = sorted(df['power_type'].unique())
selected_types = st.sidebar.multiselect(
    'Power Type', options=power_types, default=power_types
)

bins = st.sidebar.slider('Histogram bins', min_value=5, max_value=80, value=30, step=5)

top_n = st.sidebar.slider('Top N cities', min_value=5, max_value=20, value=10)

# ── Filter ────────────────────────────────────────────────────────────────────
df_f = df[df['power_type'].isin(selected_types)]

# ── Main ──────────────────────────────────────────────────────────────────────
st.title('Swiss EV Charging Stations — Interactive EDA')

# Task 1: shape + preview
st.write(f'**Rows shown:** {len(df_f):,} / {len(df):,}')
st.dataframe(df_f.head(5))

# Task 4: histogram
st.subheader('Distribution of Charging Power (kW)')
fig, ax = plt.subplots(figsize=(8, 4))
for pt in selected_types:
    ax.hist(df_f[df_f['power_type'] == pt]['power_kw'],
            bins=bins, alpha=0.6, label=pt, edgecolor='white')
ax.set_xlabel('Power (kW)')
ax.set_ylabel('Count')
if selected_types:
    ax.legend()
st.pyplot(fig)
plt.close(fig)

# Task 5: top-N cities
st.subheader(f'Top {top_n} Cities by Station Count')
top_cities = df_f['city'].value_counts().head(top_n).sort_values()
fig2, ax2 = plt.subplots(figsize=(8, top_n * 0.4 + 1))
ax2.barh(top_cities.index, top_cities.values, color='steelblue', edgecolor='white')
ax2.set_xlabel('Number of Stations')
st.pyplot(fig2)
plt.close(fig2)

# Task 6: scatter plot
st.subheader('Voltage vs. Amperage by Power Type')
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df_f, x='voltage', y='amperage', hue='power_type', alpha=0.5, s=20, ax=ax3)
ax3.set_xlabel('Voltage (V)')
ax3.set_ylabel('Amperage (A)')
st.pyplot(fig3)
plt.close(fig3)

# Task 7: summary statistics
st.subheader('Summary Statistics (filtered dataset)')
st.dataframe(df_f[NUM_COLS].describe().round(2))
