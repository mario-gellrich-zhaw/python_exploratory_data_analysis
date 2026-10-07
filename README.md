# Exploratory Data Analysis (EDA)

Python exercises and examples for a systematic introduction to exploratory data analysis (EDA) — from non-graphical statistics to interactive web applications.

---

## Repository Structure

```
data/                               # Central data folder
├── apartments_data_enriched_cleaned.csv
├── autoscout24_data_enriched_cleaned.csv
├── municipalities_kt_zh_data.xlsx
└── GEN_A4_GEMEINDEN_2019_epsg4326.json

01_introduction_to_eda/
└── introduction_to_eda.ipynb       # What is EDA, objectives, Anscombe's quartet

02_non_graphical_eda/
└── non_graphical_eda.ipynb         # Mean/median/mode, quantiles, variance, skewness,
                                    # kurtosis, contingency tables, covariance, correlation

03_graphical_eda/
└── graphical_eda.ipynb             # Line chart, box plot, histogram, QQ plot, bar chart,
                                    # pie chart, scatter plot, bubble plot, scatter matrix,
                                    # hexbin plot, correlation heatmap

04_matplotlib/
└── graphics_with_matplotlib.ipynb  # Matplotlib fundamentals and plot methods

05_seaborn/
└── seaborn_for_eda.ipynb           # Seaborn high-level API and objects interface

06_interactive_graphics/
├── flask_matplotlib_example/       # Flask + Matplotlib: histogram served as image
├── flask_apartment_data_example/   # Flask + pandas: apartment data web app
├── fastapi_example/main.py         # FastAPI: histogram and summary statistics endpoints
├── plotly_and_dash.ipynb           # Plotly Express + Dash data app
├── streamlit_example/app.py        # Streamlit interactive EDA app
└── exploring_spatial_data.ipynb    # Leaflet/Folium: interactive maps

07_automated_eda/
└── automated_eda.ipynb             # Data profiling (sweetviz),
                                    # AI-assisted EDA opportunities and pitfalls
```

---

## EDA Methods Overview

| | Non-Graphical | Graphical |
|---|---|---|
| **Univariate** | mean, median, mode, quantiles, variance, std, skewness, kurtosis | histogram, box plot, line chart, QQ plot, bar chart, pie chart |
| **Multivariate** | contingency tables, covariance matrix, correlation matrix | scatter plot, bubble plot, scatter matrix, hexbin plot, correlation heatmap |

---

## Getting Started

1. Fork this repository into your own GitHub account
2. Create a new Codespaces environment
3. Install dependencies: `pip install -r requirements.txt`
4. Open any notebook in the topic folders above

---

## Data

All datasets are stored in the `data/` folder:

| File | Description |
|---|---|
| `apartments_data_enriched_cleaned.csv` | Swiss rental apartment data |
| `autoscout24_data_enriched_cleaned.csv` | Used car listings from AutoScout24 |
| `municipalities_kt_zh_data.xlsx` | Municipality data for Canton Zurich |
| `GEN_A4_GEMEINDEN_2019_epsg4326.json` | GeoJSON boundaries for Swiss municipalities |

---

## References

- Seltman, H.J. (2018). *Experimental Design and Analysis*, Chapter 4: Exploratory Data Analysis
- Tukey, J.W. (1977). *Exploratory Data Analysis*. Addison-Wesley
- Anscombe, F.J. (1973). Graphs in statistical analysis. *The American Statistician*, 27(1), 17–21
- Matejka, J. & Fitzmaurice, G. (2017). Same stats, different graphs. *CHI 2017*
- Wilke, C.O. (2019). *Fundamentals of Data Visualization*. O'Reilly
