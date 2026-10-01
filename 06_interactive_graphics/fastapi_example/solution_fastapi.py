"""
Solution: FastAPI — Swiss EV Charging Stations
==============================================
Run with:
    uvicorn solution_fastapi:app --reload --host 0.0.0.0 --port 8000

Local:      http://127.0.0.1:8000/docs
Codespaces: https://<your-codespace-name>-8000.app.github.dev/docs
            (use --host 0.0.0.0 so Codespaces port forwarding can reach the server)
"""

import io
from typing import Literal

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, Query
from fastapi.responses import Response

plt.switch_backend('Agg')  # non-interactive backend for server-side rendering

# Task 1: load dataset
df = pd.read_csv('../../data/ev_charging_stations.csv')
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
    """Return a PNG histogram for the selected EV variable."""
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
    """Return mean, median, std, min and max for the selected variable."""
    stats = df[variable].agg(['mean', 'median', 'std', 'min', 'max']).round(2)
    return {'variable': variable, 'statistics': stats.to_dict()}


# Task 4: top cities endpoint
@app.get('/top-cities', summary='Return top N cities by station count')
def top_cities(n: int = Query(default=10, ge=1, le=30)):
    """Return the top N cities ranked by number of charging stations."""
    result = df['city'].value_counts().head(n)
    return {'top_cities': result.to_dict()}


# Task 5: power types endpoint
@app.get('/power-types', summary='Return station count per power type')
def power_types():
    """Return the count of charging stations per power type."""
    result = df['power_type'].value_counts()
    return {'power_types': result.to_dict()}
