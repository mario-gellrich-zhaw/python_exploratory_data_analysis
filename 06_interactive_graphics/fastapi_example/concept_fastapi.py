"""
FastAPI example: serve a histogram as a PNG image.

Usage:
    pip install fastapi uvicorn matplotlib pandas
    uvicorn concept_fastapi:app --reload --host 0.0.0.0 --port 8000

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

plt.switch_backend("Agg")  # non-interactive backend for server-side rendering

# Load apartment data
df = pd.read_csv("../../data/apartments_data_enriched_cleaned.csv")

app = FastAPI(title="Apartment Data EDA API")

NUMERIC_COLS = ["price", "area", "rooms"]


@app.get(
    "/histogram",
    response_class=Response,
    responses={200: {"content": {"image/png": {}}}},
    summary="Return a histogram for a selected variable",
)
def histogram(
    variable: Literal["price", "area", "rooms"] = Query(
        default="price", description="Variable to plot"
    ),
    bins: int = Query(default=40, ge=5, le=150, description="Number of histogram bins"),
):
    """Return a PNG histogram for the selected apartment variable."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df[variable].dropna(), bins=bins, color="steelblue", edgecolor="white")
    ax.set_xlabel(variable.capitalize())
    ax.set_ylabel("Frequency")
    ax.set_title(f"Distribution of {variable.capitalize()}")
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=100)
    plt.close(fig)
    buf.seek(0)
    return Response(content=buf.read(), media_type="image/png")


@app.get("/summary", summary="Return summary statistics as JSON")
def summary(variable: Literal["price", "area", "rooms"] = Query(default="price")):
    """Return descriptive statistics for the selected variable."""
    stats = df[variable].describe().round(2).to_dict()
    return {"variable": variable, "statistics": stats}
