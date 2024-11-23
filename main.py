from emails.email_utils import EmailSender

if __name__ == "__main__":
    # Example usage
    recipient = "tylertravisrhs@gmail.com"
    subject = "Daily Update"
    body = "Here's your daily email with the latest information!"
    
    email = EmailSender()

    #email.send_email(recipient, subject, body)
    email.daily_email(recipient)