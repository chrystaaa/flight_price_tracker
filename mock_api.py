from flask import Flask, request, jsonify
import random
import time

# Create a basic Flask app
app=Flask(__name__)

# Set up a price cache so price doesn't change too frequently
cached_price=None
last_updated=0
update_interval=3*60*60  # Price updates every 3 hours

# Function to generate a new random flight price
def get_new_price():
    return random.randint(80,300)

# API endpoint to simulate flight price data
@app.route('/flights',methods=['GET'])
def get_flights():
    global cached_price,last_updated

    origin=request.args.get('origin')
    destination=request.args.get('destination')
    date=request.args.get('date')

    now=time.time()

    # Update the cached price if it's expired
    if cached_price is None or (now-last_updated)>update_interval:
        cached_price=get_new_price()
        last_updated=now
        print("Updated mock price: €"+str(cached_price))

    return jsonify({
        "origin":origin,
        "destination":destination,
        "date":date,
        "price":cached_price
    })

# Start the mock server
if __name__=='__main__':
    app.run(debug=True)
