import os
import smtplib

EMAIL_ADD = os.environ.get('DB_USER')
EMAIL_PASS = os.environ.get('DB_PASS')


RECEIVER = input("Enter your email ID:\n")

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADD,EMAIL_PASS)

    subject = 'COVID-19 STATS'
    body = 'These are the stats for your area'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADD,RECEIVER , msg)