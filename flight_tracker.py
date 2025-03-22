from price_fetcher import fetch_flight_price
from notifier import send_email_notification
import schedule
import time
import csv
import os
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# User Settings from .env
origin = os.getenv("ORIGIN", "LCA")  # Default to LCA if not set
destination = os.getenv("DESTINATION", "SKG")  # Default to SKG if not set
date = os.getenv("DATE", "2025-04-01")  # Default to 2025-04-01 if not set
price_threshold = float(os.getenv("PRICE_THRESHOLD", 160))  # Default to 160 if not set

print(f"Tracking flight from {origin} to {destination} on {date} with a price threshold of €{price_threshold}")


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
