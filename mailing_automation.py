import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
load_dotenv()

class sendmail():

    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.port = 587  # TLS port
        self.sender_email = os.getenv('EMAIL')
        self.password = os.getenv('PASSKEY')

    def send(self, mailto, name):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = mailto
        msg['Subject'] = 'Congrats! You\'re in!'
        
        body = f"Dear {name},\n\n I wanted to take a moment to say thank you and to let you know what to expect from us in the future.\n To ensure that you receive our future communications, please add our email address to your contacts. This will help prevent our emails from ending up in your spam folder.\n\n Thank you again for your support and we look forward to keeping you informed about all the exciting things happening at ClipSurf.\n\nBest regards,\nTeam ClipSurf\n\n"

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, mailto, msg.as_string())
