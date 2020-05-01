import urllib.request
from flask import Flask, request,jsonify
import json
import matplotlib.pyplot as plt
import numpy
import os
import smtplib

global con
global rec
global act
global dec
global ip2
global ip1
global total
global red_zone



EMAIL_ID = os.environ.get('DB_USER')
EMAIL_PASS = os.environ.get('DB_PASS')



RECEIVER = input("Enter your E-mail ID:\n")

def getResponse(url):
    openUrl = urllib.request.urlopen(url)
    if(openUrl.getcode()==200):
        data = openUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", openUrl.getcode())
    return jsonData

def main():

    total = 0


    y_ax = []
    x_ax = []
    y = {}


    urlData = "https://api.covid19india.org/v2/state_district_wise.json"
    jsonData = getResponse(urlData)
    ip1 = input("Enter your state: ")
    ip2 = input("Enter your district: ")



    for i in jsonData: 
        x = i["state"]
        if x == ip1 :
            y[x] = i["districtData"]
            for t in y[x]:
                k = t["district"]
                if k == ip2 :
                    con = t["confirmed"]
                    rec = t["recovered"]
                    act = t["active"]
                    dec = t["deceased"]
                    print("Confirmed Patients : ",con)
                    print("Recovered Patients : ",rec)
                    print("Active Patients : ",act)
                    print("Deceased Patients : ",dec)


    for i in jsonData:
        x = i["state"]
        y[x] = i["districtData"]
        for t in y[x]:
            con = t["confirmed"]
            total = total + con






    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:


        smtp.login(EMAIL_ID,EMAIL_PASS)
        subject = 'COVID-19 STATS UPDATE'

        data_string1 = f'Dear user!\n' \
                      f'We hope you\'re staying safe and staying home.\n' \
                      f'Currently, more than 3 million people are affected worldwide and {total} people are affected in India.\n' \
                      f'Here are the stats for {ip2},{ip1} -\n' \
                      f'Confirmed Patients : {con}\n' \
                      f'Recovered Patients : {rec}\n' \
                      f'Active Patients : {act}\n' \
                      f'Deceased Patients : {dec}\n' \
                       f'Your area is in Red Zone!' \


        data_string = f'Dear user!\n' \
                  f'We hope you\'re staying safe and staying home.\n' \
                  f' Currently, more than 3 million people are affected worldwide and {total} people are affected in India.\n' \
                  f'Here are the stats for {ip2},{ip1} -\n' \
                  f'Confirmed Patients : {con}\n' \
                  f'Recovered Patients : {rec}\n' \
                  f'Active Patients : {act}\n' \
                  f'Deceased Patients : {dec}\n' \
                      f'Your area is not in Red Zone!' \


        if act >= 15:
            body = data_string1
        else:
            body = data_string

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ID, RECEIVER, msg)
    

    

if __name__ == '__main__':
    main()