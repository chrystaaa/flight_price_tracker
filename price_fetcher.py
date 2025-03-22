import os
from dotenv import load_dotenv
import requests

load_dotenv()

def fetch_flight_price(origin, destination, date):
    # Get the API URL from the environment variable
    url = os.getenv("API_URL")
    
    if not url:
        print("Error: API URL not found in environment variables.")
        return None

    params = {
        "origin": origin,
        "destination": destination,
        "date": date
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        data = response.json()
        price = data.get("price")
        print(f"Price from {origin} to {destination} on {date}: €{price}")
        return price
    except Exception as e:
        print(f"Error fetching from custom API: {e}")
        return None
