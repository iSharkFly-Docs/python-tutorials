# -*- coding: utf-8 -*-

# Python Send Email by SMTP
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/t/python/13398

import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server_address = input("请输入 SMTP 邮件服务器地址和端口：\n")
smtp_server_user_name = input("请输入 SMTP 邮件服务器的登录用户名：\n")
smtp_server_user_passwd = getpass.getpass()

email_address_from = input("发送的邮件地址 [FROM]:\n")
email_address_to = input("接收的邮件地址 [TO]:\n")

subject = input("请输入你的邮件主题\n")
body_text = input("请输入你希望发送的内容（所有内容将会显示为一行）)\n\n")

body_html = """\
    <html>
    <head></head>
    <body>
    <h1>使用 Python 发送的电子邮件！</h1>
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
    """发送邮件的方法，可以使用这个方法发送纯文本或者 HTML 的邮件。

    例如，如果你希望发送一个邮件给你的自己，你可以使用：
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
