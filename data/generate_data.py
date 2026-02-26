import random
import pandas as pd
from datetime import datetime, timedelta

# Function to generate sample machine sensor data

def generate_sensor_data(num_samples=100):
    timestamps = [datetime.utcnow() - timedelta(minutes=i) for i in range(num_samples)][::-1]
    sensor_data = {
        'timestamp': timestamps,
        'temperature': [round(random.uniform(15.0, 30.0), 2) for _ in range(num_samples)],
        'humidity': [round(random.uniform(30.0, 70.0), 2) for _ in range(num_samples)],
        'vibration': [round(random.uniform(0.0, 5.0), 2) for _ in range(num_samples)],
    }

    return pd.DataFrame(sensor_data)

# Generate example data
if __name__ == '__main__':
    data = generate_sensor_data(100)  # Generate 100 samples
    print(data.head())  # Print the first 5 samples
    
    # Save to CSV
    data.to_csv('sensor_data.csv', index=False)
    
