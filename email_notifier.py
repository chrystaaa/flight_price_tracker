import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")
TO_EMAIL=os.getenv("TO_EMAIL")

# Function to send an email alert when flight price drops
def send_email_notification(origin,destination,date,price):
    subject=f"Flight Price Drop Alert: €{price} from {origin} to {destination}"
    body=f"Good news!\n\nThe flight from {origin} to {destination} on {date} is now just €{price}!\n\nGo book it!"
    
    msg=MIMEText(body)
    msg["Subject"]=subject
    msg["From"]=EMAIL
    msg["To"]=TO_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(EMAIL,PASSWORD)
            smtp.send_message(msg)
            print("Email notification sent!")
    except Exception as e:
        print("Failed to send email:",e)
