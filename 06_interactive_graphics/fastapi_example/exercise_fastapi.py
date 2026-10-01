"""
Exercise: FastAPI — Swiss EV Charging Stations
==============================================
Build a FastAPI app that serves EDA results for the EV charging stations dataset.

Run with:
    uvicorn exercise_fastapi:app --reload --host 0.0.0.0 --port 8000

Local:      http://127.0.0.1:8000/docs
Codespaces: https://<your-codespace-name>-8000.app.github.dev/docs
            (use --host 0.0.0.0 so Codespaces port forwarding can reach the server)

Tasks
-----
1. Load the EV dataset (../../data/ev_charging_stations.csv).
2. GET /histogram  — return a PNG histogram for a selected variable
   (power_kw | amperage | voltage) and number of bins (5-100).
3. GET /summary    — return JSON summary statistics (mean, median, std, min, max)
   for a selected variable.
4. GET /top-cities — return the top N cities by station count as JSON
   (query param: n, default 10, range 1-30).
5. GET /power-types — return the count of stations per power_type as JSON.
"""

# pylint: disable=unused-import,unused-argument
import io
from typing import Literal

import matplotlib.pyplot as plt
import pandas as pd
from fastapi import FastAPI, Query
from fastapi.responses import Response

plt.switch_backend('Agg')  # non-interactive backend for server-side rendering

# Task 1: load dataset
# YOUR CODE HERE

app = FastAPI(title='EV Charging Stations EDA API')


# Task 2: histogram endpoint
@app.get('/histogram', response_class=Response,
         responses={200: {'content': {'image/png': {}}}})
def histogram(
    variable: Literal['power_kw', 'amperage', 'voltage'] = Query(default='power_kw'),
    bins: int = Query(default=30, ge=5, le=100),
):
    """Return a PNG histogram for the selected EV variable."""
    # YOUR CODE HERE


# Task 3: summary statistics endpoint
@app.get('/summary')
def summary(
    variable: Literal['power_kw', 'amperage', 'voltage'] = Query(default='power_kw'),
):
    """Return mean, median, std, min and max for the selected variable."""
    # YOUR CODE HERE


# Task 4: top cities endpoint
@app.get('/top-cities')
def top_cities(n: int = Query(default=10, ge=1, le=30)):
    """Return the top N cities ranked by number of charging stations."""
    # YOUR CODE HERE


# Task 5: power types endpoint
@app.get('/power-types')
def power_types():
    """Return the count of charging stations per power type."""
    # YOUR CODE HERE
