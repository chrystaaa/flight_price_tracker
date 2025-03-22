from price_fetcher import fetch_flight_price
from notifier import send_email_notification
import schedule
import time
import csv
import os
from datetime import datetime

# Users Settings
origin = "JFK"
destination = "LHR"
date = "2025-04-01"
price_threshold = 160  # in Euros

# Create CSV with header if it doesn't exist
if not os.path.exists("price_history.csv"):
    with open("price_history.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "origin", "destination", "date", "price"])

# Main Function
def check_price():
    print("🔎 Checking flight prices...")
    price = fetch_flight_price(origin, destination, date)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if price is not None:
        print(f"Fetched price: €{price}")

        # Save to CSV
        with open("price_history.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now, origin, destination, date, price])

        if price <= price_threshold:
            send_email_notification(origin, destination, date, price)
        else:
            print(f"Price €{price} is above your threshold of €{price_threshold}.")
    else:
        print("Could not fetch price.")

# Scedule
print("🔍 Starting flight price tracker...")
check_price()
schedule.every(6).hours.do(check_price)

while True:
    schedule.run_pending()
    time.sleep(1)
