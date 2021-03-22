# -*- coding: utf-8 -*-

# Python Email Sending Test
# Author - HoneyMoose(huyuchengus@gmail.com)
# Link Article - https://www.ossez.com/t/python/13398

import requests


# MAILGUN API SEND MESSAGE
def mailgun_api_send_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7955c7c533744fb28e650b72192eac87.mailgun.org",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "OSSEZ <huyuchengus@gmail.com>",
              "to": ["huyuchengus@gmail.com"],
              "subject": "Hello MailGun API",
              "text": "Testing Sending mail by Mailgun API!"})


if __name__ == "__main__":
    for i in range(3):
        print(mailgun_api_send_message().text)
