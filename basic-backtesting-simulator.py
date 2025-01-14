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

# Execute TWAP strategy
def execute_twap(data, total_volume, intervals):
    # Divide total volume equally across intervals
    volume_per_interval = total_volume // intervals
    prices_during_execution = []
    traded_volumes = []
    
    # Split data into intervals and calculate average price for each
    for interval in range(intervals):
        start = interval * (len(data) // intervals)
        end = (interval + 1) * (len(data) // intervals)
        interval_data = data.iloc[start:end]
        
        avg_price = interval_data['Price'].mean()
        prices_during_execution.append(avg_price)
        traded_volumes.append(volume_per_interval)
    
    return prices_during_execution, traded_volumes

# Calculate performance metrics
def evaluate_strategy(executed_prices, traded_volumes, benchmark):
    # Weighted average price of executed trades
    avg_execution_price = np.average(executed_prices, weights=traded_volumes)
    
    # Metrics: Execution cost and slippage
    execution_cost = avg_execution_price - benchmark
    slippage = max(executed_prices) - min(executed_prices)
    
    return {
        'Execution Cost': execution_cost,
        'Slippage': slippage
    }

# Main function
if __name__ == "__main__":
    # Step 1: Create synthetic data
    market_data = generate_market_data()
    
    # Step 2: Define trading parameters
    total_volume_to_trade = 10_000
    num_intervals = 10
    benchmark_price = market_data['Price'].mean()  # Using VWAP as a benchmark

    # Step 3: Execute the TWAP strategy
    executed_prices, traded_volumes = execute_twap(
        data=market_data,
        total_volume=total_volume_to_trade,
        intervals=num_intervals
    )

    # Step 4: Evaluate strategy performance
    metrics = evaluate_strategy(
        executed_prices=executed_prices,
        traded_volumes=traded_volumes,
        benchmark=benchmark_price
    )

    # Step 5: Output results
    print("Strategy Performance Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")
