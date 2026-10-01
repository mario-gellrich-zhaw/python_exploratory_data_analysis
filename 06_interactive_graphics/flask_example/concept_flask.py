"""
Concept: Flask — Apartment Data EDA
====================================
Run with:
    python concept_flask.py

Local:      http://127.0.0.1:5000
Codespaces: https://<your-codespace-name>-5000.app.github.dev
            (Flask binds to 0.0.0.0 via app.run(host='0.0.0.0'))
"""

import os

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template

# Set global Matplotlib style for dark background
plt.style.use('dark_background')

# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def index():
    """Render the main dashboard with KPIs and a price histogram."""
    df = pd.read_csv('../../data/apartments_data_enriched_cleaned.csv')

    mean_price = round(df['price'].mean(), 2)
    mean_area = round(df['area'].mean(), 2)

    plt.figure(figsize=(10, 6))
    color = (102 / 255, 204 / 255, 0 / 255)
    plt.hist(df['price'], bins=20, color=color, edgecolor='white')
    plt.title('Price Distribution of Apartments', color='greenyellow')
    plt.xlabel('Price (CHF)', color='greenyellow')
    plt.ylabel('Number of Apartments', color='greenyellow')
    plt.grid(color='gray', linestyle='--')
    plt.tick_params(colors='greenyellow')

    histogram_path = os.path.join('static', 'price_histogram.png')
    plt.savefig(histogram_path, bbox_inches='tight', transparent=True)
    plt.close()

    apartments = df.to_dict(orient='records')
    return render_template(
        'index.html',
        apartments=apartments,
        mean_price=mean_price,
        mean_area=mean_area,
        histogram_path=histogram_path,
    )


if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, host='0.0.0.0')
