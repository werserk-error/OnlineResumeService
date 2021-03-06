from email.mime.text import MIMEText
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from random import randint


def send_email(email, subject, text):
    addr_from = os.getenv("FROM")
    password = os.getenv("PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = email
    msg['Subject'] = subject

    body = text
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL(os.getenv('HOST'), os.getenv('PORT_MAIL'))
    server.login(addr_from, password)

    server.send_message(msg)
    server.quit()

    return True


def create_verification_code():
    return randint(100000, 999999)
