from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import List

class EmailSender:

    def send_email(self, recipient_email, subject, body):
        """Sends an email to the specified recipient."""
        # Load email credentials from environment variables
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")

        if not sender_email or not sender_password:
            raise ValueError("Email credentials are missing in the environment variables!")

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Add the email body with HTML content
        msg.attach(MIMEText(body, 'html'))  # Changed to 'html' for proper hyperlink formatting

        try:
            # Connect to the SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def get_current_date(self):
        # Get the current date
        current_date = datetime.now()
        
        # Format the date as "Month Day" (e.g., "November 23")
        formatted_date = current_date.strftime("%B %d")
        
        return formatted_date

    def daily_email(self, recipient):
        # Get the current date
        formatted_date = self.get_current_date()

        # Craft the email body with HTML formatting and a clickable hyperlink
        body = f"""
        <html>
        <body>
            <p>Hi there,</p>

            <p>Please fill out the following form:</p>
            <a href="https://forms.gle/kWtfifjuDCn85FbP8">Egg Cracking Data Form</a>

            <p>This will help us track the egg cracking progress for today, {formatted_date}.</p>

            <p>Thank you!</p>
        </body>
        </html>
        """

        self.send_email(recipient, f"Egg Data Request ({formatted_date})", body)
