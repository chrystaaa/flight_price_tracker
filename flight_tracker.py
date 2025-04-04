from price_fetcher import fetch_flight_price
from notifier import send_email_notification
from dotenv import load_dotenv
import schedule
import time
import csv
import os
from datetime import datetime

# Load environment variables from .env
load_dotenv()

# Get values from .env or use defaults
origin=os.getenv("ORIGIN","LCA")
destination=os.getenv("DESTINATION","SKG")
date=os.getenv("DATE","2025-04-01")
price_threshold=float(os.getenv("PRICE_THRESHOLD",160))

print("Tracking flight from",origin,"to",destination,"on",date,"with alert if price is below €"+str(price_threshold))

# Create CSV file if it doesn't exist
if not os.path.exists("price_history.csv"):
    with open("price_history.csv","w",newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["timestamp","origin","destination","date","price"])

# Main function to check the price
def check_price():
    print("Checking flight price...")
    price=fetch_flight_price(origin,destination,date)
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if price is not None:
        print("Price found: €"+str(price))

        # Save result to CSV
        with open("price_history.csv","a",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([now,origin,destination,date,price])

        # Send email if price is low enough
        if price<=price_threshold:
            send_email_notification(origin,destination,date,price)
        else:
            print("Price is above your set threshold.")
    else:
        print("Could not fetch the flight price.")

# Start tracker
print("Starting flight tracker...")
check_price()
schedule.every(6).hours.do(check_price)

# Loop forever, checking every 6 hours
while True:
    schedule.run_pending()
    time.sleep(1)
