from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

cached_price = None
last_updated = 0
update_interval = 3*60*60 #Changes price every 3 hours


def get_new_price():
    return random.randint(80, 300)


@app.route('/flights', methods=['GET'])
def get_flights():
    global cached_price, last_updated

    origin = request.args.get('origin')
    destination = request.args.get('destination')
    date = request.args.get('date')

    now = time.time()

    # Refresh price every few hours
    if cached_price is None or (now - last_updated) > update_interval:
        cached_price = get_new_price()
        last_updated = now
        print(f"Updated price: €{cached_price}")

    return jsonify({
        "origin": origin,
        "destination": destination,
        "date": date,
        "price": cached_price
    })


if __name__ == '__main__':
    app.run(debug=True)
