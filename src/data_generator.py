import random
import time
import json

class SensorDataGenerator:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def generate_data(self):
        data = {
            'sensor_id': self.sensor_id,
            'temperature': random.uniform(20.0, 100.0),
            'humidity': random.uniform(30.0, 90.0),
            'vibration': random.uniform(0.0, 10.0),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
        }
        return json.dumps(data)

if __name__ == '__main__':
    generator = SensorDataGenerator(sensor_id='sensor_001')
    for _ in range(10):
        print(generator.generate_data())
        time.sleep(1)