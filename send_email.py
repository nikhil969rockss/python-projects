import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "<Your app password>"
sender_email= "<your email id>"
receiver_email= "<receiver email id>"

def send_email(image_file):
    email_message = EmailMessage()
    email_message["Subject"] = "A new person is detected"
    email_message.set_content("check the person's photo")

    with open(image_file, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image",
                                 subtype=imghdr.what(None, content))

    gmail  = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender_email, PASSWORD)
    gmail.sendmail(sender_email, receiver_email, email_message.as_string())
    gmail.quit()


if __name__ = '__main__':
    send_email("images/20.png")

# This i can't test because Gmail has banned the email id which was 2 step
# verified, because it detects that it was created by a computer program.