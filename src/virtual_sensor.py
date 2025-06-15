import random

def generate_sensor_data():
    return {
        'N': random.randint(0, 140),
        'P': random.randint(5, 145),
        'K': random.randint(5, 205),
        'temperature': round(random.uniform(20, 40), 2),
        'humidity': round(random.uniform(30, 90), 2),
        'ph': round(random.uniform(4.5, 8.5), 2),
        'rainfall': round(random.uniform(50, 200), 2)
    }
