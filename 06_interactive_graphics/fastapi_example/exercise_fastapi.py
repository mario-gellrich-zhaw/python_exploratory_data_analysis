"""
Exercise: FastAPI — Swiss EV Charging Stations
==============================================
Build a FastAPI app that serves EDA results for the EV charging stations dataset.

Run with:
    uvicorn exercise_fastapi:app --reload
Then open http://127.0.0.1:8000/docs for the interactive Swagger UI.

Tasks
-----
1. Load the EV dataset (../../../data/ev_charging_stations.csv).
2. GET /histogram  — return a PNG histogram for a selected variable
   (power_kw | amperage | voltage) and number of bins (5-100).
3. GET /summary    — return JSON summary statistics (mean, median, std, min, max)
   for a selected variable.
4. GET /top-cities — return the top N cities by station count as JSON
   (query param: n, default 10, range 1-30).
5. GET /power-types — return the count of stations per power_type as JSON.
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
# YOUR CODE HERE

app = FastAPI(title='EV Charging Stations EDA API')


# Task 2: histogram endpoint
@app.get('/histogram', response_class=Response,
         responses={200: {'content': {'image/png': {}}}})
def histogram(
    variable: Literal['power_kw', 'amperage', 'voltage'] = Query(default='power_kw'),
    bins: int = Query(default=30, ge=5, le=100),
):
    # YOUR CODE HERE
    pass


# Task 3: summary statistics endpoint
@app.get('/summary')
def summary(
    variable: Literal['power_kw', 'amperage', 'voltage'] = Query(default='power_kw'),
):
    # YOUR CODE HERE
    pass


# Task 4: top cities endpoint
@app.get('/top-cities')
def top_cities(n: int = Query(default=10, ge=1, le=30)):
    # YOUR CODE HERE
    pass


# Task 5: power types endpoint
@app.get('/power-types')
def power_types():
    # YOUR CODE HERE
    pass
