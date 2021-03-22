# -*- coding: utf-8 -*-

# Python Send Email by SMTP
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/t/python/13398

import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server_address = input("Please Enter SMTP Server address with port:\n")
smtp_server_user_name = input("Please Enter SMTP Server User Name:\n")
smtp_server_user_passwd = getpass.getpass()

email_address_from = input("Email Address [FROM]:\n")
email_address_to = input("Email Address [TO]:\n")

subject = input("What is your email subject?\n")
body_text = input("What message did you want to email? (currently this is only one line)\n\n")

body_html = """\
    <html>
    <head></head>
    <body>
    <h1>Using Python Sending Test Email!</h1>
    <p>
    """

body_html += body_text

body_html += """</p>
    </body>
    </html>
    """


def send_mail(to_addr, subject="Test email",
              body_text="Test message",
              body_html="Test message",
              from_addr=email_address_from,
              email_user=smtp_server_user_name,
              email_passwd=smtp_server_user_passwd,
              smtpserver="smtp.mailgun.org:587"):
    """A function to send email, in MIME multi-part (plain-text and HTML).

    For example: to send to myself:
    send_mail(to_addr, subject, body_text=body_text, body_html=body_html)
    """

    # Construct the message header
    message = MIMEMultipart('alternative')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = subject

    # Append the body text
    message.attach(MIMEText(body_text, 'plain'))
    message.attach(MIMEText(body_html, 'html'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(email_user, email_passwd)
    sending_response = server.sendmail(from_addr, to_addr, message.as_string())
    print(sending_response)
    server.quit()


send_mail(email_address_to, subject, body_text, body_html, email_address_from, smtp_server_user_name,
          smtp_server_user_passwd,
          smtp_server_address)
