from utils.email_utils import EmailSender

if __name__ == "__main__":
    # Example usage
    recipient = "tylertravisrhs@gmail.com"    
    email = EmailSender()

    #email.send_email(recipient, subject, body)
    email.daily_email(recipient)