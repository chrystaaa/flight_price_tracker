Flight Price Tracker Project
Overview
This project is a flight price tracker that allows users to track and get notified when the price of a specific flight drops below a certain threshold. The tracker monitors flight prices using an API, and when the price reaches a pre-defined target, it sends a notification to the user.

Key Features:
Flight Price Tracking: Track prices for specific flight routes.
Notifications: Receive email notifications when the price drops below a certain threshold.
Custom API: Used a custom Flask API to simulate flight data.
Steps Followed:
1. Set Up a Flask Web Application:
Created a Flask application to simulate a flight price API.
Implemented price tracking logic that updates every 3 hours.
2. Simulated API for Testing:
Created a simulated API using Python's random module to generate random flight prices between €80 and €300.
This was done to quickly test the tracking logic without needing to integrate a real API.
3. Price Tracking Logic:
Implemented a price comparison feature that checks if the flight price has dropped below the user's set threshold.
Prerequisites
Make sure you have the following installed:

Python 3.x
Flask
requests (if connecting to any real API in the future)