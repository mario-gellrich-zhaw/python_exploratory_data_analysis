"""
Solution: Flask — Swiss EV Charging Stations
============================================
Run with:
    python solution_flask.py

Local:      http://127.0.0.1:5000
Codespaces: https://<your-codespace-name>-5000.app.github.dev
            (Flask binds to 0.0.0.0 by default via app.run(host='0.0.0.0'))
"""

import base64
import io

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, jsonify, render_template_string, request

plt.switch_backend('Agg')  # non-interactive backend for server-side rendering

app = Flask(__name__)

df = pd.read_csv('../../data/ev_charging_stations.csv')
NUM_COLS = ['power_kw', 'amperage', 'voltage']

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
  <p><a href="/summary">View summary statistics (JSON)</a></p>
</body>
</html>
"""


def make_histogram(variable: str, bins: int) -> str:
    """Render histogram and return as base64-encoded PNG string."""
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
    return base64.b64encode(buf.read()).decode('utf-8')


@app.route('/')
def index():
    """Render histogram page with variable selector and bin slider."""
    variable = request.args.get('variable', 'power_kw')
    if variable not in NUM_COLS:
        variable = 'power_kw'
    bins = max(5, min(80, request.args.get('bins', default=30, type=int)))
    image = make_histogram(variable, bins)
    return render_template_string(HTML_TEMPLATE, variable=variable, bins=bins, image=image)


@app.route('/summary')
def summary():
    """Return JSON summary statistics for all numeric columns."""
    stats = df[NUM_COLS].agg(['mean', 'median', 'std', 'min', 'max']).round(2)
    return jsonify(stats.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
