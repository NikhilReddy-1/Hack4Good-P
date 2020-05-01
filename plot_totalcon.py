import urllib.request
from flask import Flask, request,jsonify
import json
import matplotlib.pyplot as plt
import numpy



def getResponse(url):
    openUrl = urllib.request.urlopen(url)
    if(openUrl.getcode()==200):
        data = openUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", openUrl.getcode())
    return jsonData

def main():
    
    y_ax = []
    x_ax = []
    urlData = "https://api.covid19india.org/data.json"
    jsonData = getResponse(urlData)
    for i in jsonData["cases_time_series"]:
        t = int(i["totalconfirmed"])
        y_ax.append(t)
    for i in range(0,len(y_ax)):
        x_ax.append(i)
    plt.plot(x_ax,y_ax)
    plt.show()
    
    

if __name__ == '__main__':
    main()