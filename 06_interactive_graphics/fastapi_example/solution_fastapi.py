"""
Solution: FastAPI — Swiss EV Charging Stations
==============================================
Run with:
    uvicorn solution_fastapi:app --reload
Then open http://127.0.0.1:8000/docs for the interactive Swagger UI.
"""

import io
from typing import Literal

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, Query
from fastapi.responses import Response

# Task 1: load dataset
df = pd.read_csv('../../../data/ev_charging_stations.csv')
NUM_COLS = ['power_kw', 'amperage', 'voltage']

app = FastAPI(title='EV Charging Stations EDA API')


# Task 2: histogram endpoint
@app.get(
    '/histogram',
    response_class=Response,
    responses={200: {'content': {'image/png': {}}}},
    summary='Return a PNG histogram for the selected variable',
)
def histogram(
    variable: Literal['power_kw', 'amperage', 'voltage'] = Query(default='power_kw'),
    bins: int = Query(default=30, ge=5, le=100),
):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df[variable].dropna(), bins=bins, color='steelblue', edgecolor='white')
    ax.set_xlabel(variable)
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {variable}')
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100)
    plt.close(fig)
    buf.seek(0)
    return Response(content=buf.read(), media_type='image/png')


# Task 3: summary statistics endpoint
@app.get('/summary', summary='Return summary statistics for the selected variable')
def summary(
    variable: Literal['power_kw', 'amperage', 'voltage'] = Query(default='power_kw'),
):
    stats = df[variable].agg(['mean', 'median', 'std', 'min', 'max']).round(2)
    return {'variable': variable, 'statistics': stats.to_dict()}


# Task 4: top cities endpoint
@app.get('/top-cities', summary='Return top N cities by station count')
def top_cities(n: int = Query(default=10, ge=1, le=30)):
    result = df['city'].value_counts().head(n)
    return {'top_cities': result.to_dict()}


# Task 5: power types endpoint
@app.get('/power-types', summary='Return station count per power type')
def power_types():
    result = df['power_type'].value_counts()
    return {'power_types': result.to_dict()}
