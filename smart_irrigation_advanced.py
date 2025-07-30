import random
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="smart_irrigation_advanced_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class SmartIrrigationSystem:
    def __init__(self, threshold=40):
        self.threshold = threshold
        self.battery_level = 100  # Simulated battery %
        self.weather_condition = "Sunny"
        print(f"🚀 System Ready | Threshold: {self.threshold}%, Battery: {self.battery_level}%")
        logging.info("System initialized with moisture threshold: %d%%", self.threshold)

    def read_soil_moisture(self):
        return random.randint(20, 80)

    def predict_moisture(self, current):
        return max(current - random.randint(2, 6), 0)

    def read_battery_level(self):
        self.battery_level = max(self.battery_level - random.randint(1, 3), 10)
        return self.battery_level

    def simulate_weather(self):
        self.weather_condition = random.choice(["Sunny", "Cloudy", "Rainy"])
        return self.weather_condition

    def activate_pump(self):
        print("✅ Pump Activated - Irrigating Crops")
        logging.info("Pump Activated")

    def deactivate_pump(self):
        print("❌ Pump Deactivated - Moisture Sufficient")
        logging.info("Pump Deactivated")

    def alert_low_moisture(self, moisture):
        if moisture < 25:
            print("🚨 ALERT: Critically low soil moisture!")
            logging.warning("Critical low moisture alert triggered at %d%%", moisture)

    def alert_low_battery(self, battery):
        if battery < 20:
            print("🔋 WARNING: Battery Low! Please recharge.")
            logging.warning("Battery low at %d%%", battery)

    def control_irrigation(self):
        moisture_now = self.read_soil_moisture()
        predicted = self.predict_moisture(moisture_now)
        battery = self.read_battery_level()
        weather = self.simulate_weather()

        print(f"\n📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📊 Soil Moisture: {moisture_now}% | 🔮 Predicted: {predicted}%")
        print(f"☀️ Weather: {weather} | 🔋 Battery: {battery}%")

        self.alert_low_moisture(moisture_now)
        self.alert_low_battery(battery)

        if predicted < self.threshold and weather != "Rainy":
            self.activate_pump()
        else:
            self.deactivate_pump()

        logging.info("Moisture: %d%%, Predicted: %d%%, Battery: %d%%, Weather: %s",
                     moisture_now, predicted, battery, weather)

# Main Execution
if __name__ == "__main__":
    system = SmartIrrigationSystem(threshold=40)

    for cycle in range(1, 6):
        print(f"\n🔄 Cycle {cycle}")
        system.control_irrigation()
        time.sleep(2)

    print("\n📘 System Run Complete. Check 'smart_irrigation_advanced_log.txt' for logs.")
