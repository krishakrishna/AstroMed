import random

def get_sensor_data():
    """
    Simulated sensor data for astronaut vitals (heart rate, oxygen levels, body temp).
    """
    return {
        "heart_rate": random.randint(60, 120),  # Normal HR range
        "oxygen_level": random.randint(90, 100),  # Normal O2 saturation
        "body_temp": round(random.uniform(36.5, 37.5), 1)  # Normal human temp
    }

if __name__ == "__main__":
    print(get_sensor_data())
