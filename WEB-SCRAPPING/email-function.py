import smtplib,ssl
from email.message import EmailMessage
import mimetypes
from pathlib import Path

SENDER = "youremail@gmail.com"
PASSWORD = "your_app_password"
RECEIVER = "receiver@gmail.com"

# function with emage

def send_email_f(file_path):
    msg = EmailMessage()
    msg["Subject"] = "Attachment from Python"
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg.set_content("Please find the attachment")

    with open(file_path, "rb") as f:
        file_data = f.read()

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        maintype, subtype = mime_type.split("/")
    else:
        maintype, subtype = "application", "octet-stream"

    msg.add_attachment(
        file_data,
        maintype=maintype,
        subtype=subtype,
        filename=Path(file_path).name
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(SENDER, PASSWORD)
        server.send_message(msg)

send_email_f("image.png")

# funciton without attachment

def send_email():

    msg = EmailMessage()
    msg["Subject"] = "Hello from Python"
    msg["From"] = SENDER
    msg["To"] = RECEIVER
    msg.set_content("This email was sent using Python 🐍")

    with smtplib.SMTP("smtp.gmail.com", 587,) as server:
        server.starttls()
        server.login(SENDER, PASSWORD)
        server.send_message(msg)


def send_email_ssl(message):
    host = 'smtp.gmail.com'
    port = 465

    sender_email = "sender_gmail_id"
    sender_password = "sender_password"

    recevier_gamil = "receiver_gmail.id"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recevier_gamil, message)