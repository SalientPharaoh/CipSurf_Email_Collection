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
        msg['Subject'] = 'You\'re in! Get ready to be the first to know about our new product.'
        body = f"Hi! {name},\n\n Thank You! Stay healthy and Enjoy!\n\n"

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, mailto, msg.as_string())
