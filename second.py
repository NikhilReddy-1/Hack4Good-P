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
    if act >= 15 :
        print("Your area is in Red Zone!")
        
    #print(y)
    #print("",type(y))
    
        
    
    
    
    
    

if __name__ == '__main__':
    main()