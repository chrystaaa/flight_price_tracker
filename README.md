Flight Price Tracker

This is a simple Python script that checks flight prices for a specific route and sends an email notification when the price drops below a set threshold. A custom Flask API is used to simulate flight data.

This project was built using:
- Flask (for creating the mock API)
- dotenv (to keep settings like email and passwords safe)
- schedule (to check prices automatically every few hours)
- smtplib (to send email alerts)
- CSV (to store flight price history)

Steps followed:
1. Created a mock API using Flask that returns a random flight price
2. Wrote a script that fetches prices from that API
3. Set up logic to compare the price to a threshold
4. Sent email notifications using SMTP if the price was low
5. Logged all prices to a CSV file for tracking

>Disclaimer:  
This project was created only for educational purposes to practice using Flask, APIs, and automation. It is not connected to any real airline website or flight data provider.

>How to Run:

1. Open your terminal (Git Bash, Command Prompt, etc.)
2. Navigate to the folder where your script is saved
3. Start the mock API by running:

python mock_api.py

4. In a new terminal window, run the tracker:

python flight_tracker.py

>Setup Required:

Files you need in the same folder:

1. flight_tracker.py → the main tracker script  
2. notifier.py → sends email when price is low  
3. mock_api.py → simulates live flight data  
4. .env → stores your settings (like email, origin, etc.)  
5. price_history.csv → automatically created to log flight prices

>Make sure you have the following installed on your computer:

1. Python 3.x  
2. Flask  
3. schedule  
4. requests  
5. python-dotenv

To install everything, run this command in your terminal:

pip install flask requests schedule python-dotenv

>Disclaimer:  
If you're using Gmail, you need to create an App Password and use that instead of your regular password.
