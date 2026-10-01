"""
Exercise: Flask — Swiss EV Charging Stations
============================================
Build a Flask web app that serves interactive EDA charts for the EV charging stations dataset.

Run with:
    python exercise_flask.py
Then open http://127.0.0.1:5000 in your browser.

Tasks
-----
1. Load the EV charging stations dataset (../../../data/ev_charging_stations.csv).
2. Create a route GET / that renders an HTML page showing:
   - A dropdown to select a numerical variable (power_kw, amperage, voltage).
   - A histogram of the selected variable, served as a base64-encoded PNG image.
3. Create a route GET /summary that returns a JSON response with summary statistics
   (mean, median, std, min, max) for power_kw, amperage and voltage.
4. Pass the number of bins as a query parameter ?bins=<int> (default: 30).

Hints
-----
- Use matplotlib with the Agg backend to render plots server-side.
- Encode the plot with base64 and embed it as <img src="data:image/png;base64,..."> in the template.
- Use flask.request.args.get() to read query parameters.
- Use flask.jsonify() to return JSON responses.
"""

import io
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Task 1: load the dataset
# YOUR CODE HERE


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>EV Charging Stations EDA</title></head>
<body>
  <h2>EV Charging Stations — Histogram</h2>
  <form method="GET">
    <label>Variable:
      <select name="variable">
        <option value="power_kw"  {% if variable == 'power_kw'  %}selected{% endif %}>power_kw</option>
        <option value="amperage"  {% if variable == 'amperage'  %}selected{% endif %}>amperage</option>
        <option value="voltage"   {% if variable == 'voltage'   %}selected{% endif %}>voltage</option>
      </select>
    </label>
    <label>Bins: <input type="number" name="bins" value="{{ bins }}" min="5" max="80"></label>
    <button type="submit">Update</button>
  </form>
  <br>
  <img src="data:image/png;base64,{{ image }}" style="max-width:800px;">
</body>
</html>
"""


@app.route('/')
def index():
    # Task 2 + 4: YOUR CODE HERE
    pass


@app.route('/summary')
def summary():
    # Task 3: YOUR CODE HERE
    pass


if __name__ == '__main__':
    app.run(debug=True)
