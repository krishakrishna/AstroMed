from models.health_risk_model import predict_health_risk
from sensors.sensor_interface import get_sensor_data
from nlp.chatbot import chatbot_response # type: ignore
from vision import analyze_fatigue
import time

def main():
    print("🚀 AstroMed AI - Space Health Monitoring System 🚀")
    
    while True:
        # Get real-time biometric data
        health_data = get_sensor_data()
        print(f"🩺 Biometric Data: {health_data}")

        # Predict health risk
        risk = predict_health_risk(health_data)
        print(f"⚠️ Health Risk Prediction: {risk}")

        # Vision analysis (Fatigue & Stress)
        fatigue_level = analyze_fatigue()
        print(f"😴 Fatigue Level: {fatigue_level}")

        # Chatbot interaction
        query = input("👩‍🚀 Ask AstroMed a question: ")
        response = chatbot_response(query)
        print(f"🤖 AstroMed: {response}")

        time.sleep(5)  # Simulate real-time monitoring delay

if __name__ == "__main__":
    main()
