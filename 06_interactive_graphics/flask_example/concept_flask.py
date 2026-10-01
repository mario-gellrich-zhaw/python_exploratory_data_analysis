from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set global Matplotlib style for dark background
plt.style.use('dark_background')

# Initialize Flask app
app = Flask(__name__)

# Load the apartment data from CSV
@app.route('/')
def index():
    # Load the CSV file (update the path if needed)
    df = pd.read_csv('../../../data/apartments_data_enriched_cleaned.csv')

    # Calculate KPIs and round them
    mean_price = round(df['price'].mean(), 2)
    mean_area = round(df['area'].mean(), 2)

    # Plot histogram of prices (dark theme is applied globally)
    plt.figure(figsize=(10,6))
    
    # Plot the histogram with skyblue bars and white edges
    color = (102/255, 204/255, 0/255)
    plt.hist(df['price'], bins=20, color=color, edgecolor='white')
    
    # Set title and labels with greenyellow color
    plt.title('Price Distribution of Apartments', color='greenyellow')
    plt.xlabel('Price (CHF)', color='greenyellow')
    plt.ylabel('Number of Apartments', color='greenyellow')

    # Customize grid, tick parameters
    plt.grid(color='gray', linestyle='--')
    plt.tick_params(colors='greenyellow')  # Change the tick color

    # Save histogram to the static folder
    histogram_path = os.path.join('static', 'price_histogram.png')
    plt.savefig(histogram_path, bbox_inches='tight', transparent=True)
    plt.close()

    # Convert dataframe to a list of dictionaries
    apartments = df.to_dict(orient='records')

    # Render the index.html template and pass KPI data and histogram
    return render_template('index.html', apartments=apartments, 
                           mean_price=mean_price, 
                           mean_area=mean_area, 
                           histogram_path=histogram_path)

if __name__ == '__main__':
    # Ensure the 'static' directory exists for storing the histogram image
    if not os.path.exists('static'):
        os.makedirs('static')

    # Run the Flask app
    app.run(debug=True, host='0.0.0.0')
