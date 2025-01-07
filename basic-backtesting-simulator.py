import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic market data
def generate_market_data(points=1000):
    # Set a seed for reproducibility
    np.random.seed(42)
    
    # Create timestamps and simulate price changes
    timestamps = pd.date_range(start='2023-01-01', periods=points, freq='S')
    price_changes = np.random.normal(loc=0, scale=0.5, size=points)
    prices = 100 + np.cumsum(price_changes)  # Starting price at 100
    
    # Random trading volumes
    volumes = np.random.randint(100, 500, size=points)
    
    # Combine into a DataFrame
    return pd.DataFrame({
        'Timestamp': timestamps,
        'Price': prices,
        'Volume': volumes
    })
