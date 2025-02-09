import numpy as np
import random

def predict_health_risk(data):
    """
    Simulated AI model predicting astronaut health risks.
    Input: Dictionary containing health data (heart rate, oxygen levels, etc.).
    Output: Health risk status.
    """
    heart_rate = data.get("heart_rate", 70)
    oxygen_level = data.get("oxygen_level", 98)

    risk_score = (220 - heart_rate) * (oxygen_level / 100)
    
    if risk_score < 50:
        return "High Risk - Immediate Attention Required"
    elif risk_score < 100:
        return "Medium Risk - Monitor Closely"
    else:
        return "Low Risk - All Normal"

if __name__ == "__main__":
    sample_data = {"heart_rate": 85, "oxygen_level": 95}
    print(predict_health_risk(sample_data))
