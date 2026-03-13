import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()
email_password = os.getenv("EMAIL_PASSWORD")
email_id = os.getenv('SENDER_EMAIL')


def send_email(message):

    host ="smtp.gmail.com"
    port = 465

    sender_email = email_id
    password = email_password

    receiver_email = "ns9013604867@gmail.com"
    context =  ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message)


# HTML email support

# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
#
# def send_email(message):
#     email = MIMEMultipart()
#     email["From"] = "YOUR_EMAIL"
#     email["To"] = "RECEIVER_EMAIL"
#     email["Subject"] = "Today's top technology news"
#
#     email.attach(MIMEText(message, "html"))
#   with smtplib.SMTP_SSL(host, port, context=context) as server:
#         server.login(sender_email, email_password)
#         server.sendmail(
#             from_addr=sender_email,
#             to_addrs=receiver_email,
#             msg=email.as_string()
#         )
#     # smtp code yahan hoga