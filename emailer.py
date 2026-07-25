# emailer.py
# Sends the final report as an email to the configured email address. 

import smtplib
import os
from dotenv import load_dotenv
import email
from email.message import EmailMessage

def send_email(subject, message):
    load_dotenv()
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    target_email_addr = os.getenv("TARGET_EMAIL_ADDRESS")
    target_server = os.getenv("TARGET_EMAIL_SERVER")
    target_port = os.getenv("TARGET_EMAIL_PORT")
    server = smtplib.SMTP_SSL(target_server, 465) # set in configuration correct target SMTP server
    server.login(username, password) # Gather username and password from configuration

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = username
    msg["To"] = target_email_addr
    msg.set_content(message)

    try: 
        with smtplib.SMTP(target_server, target_port) as server:
            server.starttls()  # Upgrade connection to secure TLS encrypted
            server.login(username, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    return