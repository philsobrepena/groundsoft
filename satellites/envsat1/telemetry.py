import requests
import random
import time
import os

class Telemetry:
    def __init__(self, satellite_id, server_url):
        self.satellite_id = satellite_id
        self.server_url = server_url

    def send_data(self):
        #simulate telemetry

        data = {
            "envsat-1": self.satellite_id,
            "temperature": random.uniform(-50,50),
            "humidity": random.uniform(0,100),
        }
        try:
            response = requests.post(self.server_url, json=data)
            print(f"Data Sent!: {data}, Response: {response.status_code}")

        except Exception as e:
            print(f"Data Send Failed: {e}")

    def run(self):
        while True:
            self.send_data()
            time.sleep(5) # every 5 seconds

if __name__ == "__main__":
    server_url = os.getenv("SERVER_URL", "http://localhost:8000/telemetry")
    telemetry = Telemetry(satellite_id="envsat1", server_url=server_url)
    telemetry.run()
