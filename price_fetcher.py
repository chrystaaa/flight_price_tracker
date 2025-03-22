import requests

def fetch_flight_price(origin, destination, date):
    url = "http://127.0.0.1:5000/flights"
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
