import urllib.request
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

    urlData = "https://api.covid19india.org/data.json"
    jsonData = getResponse(urlData)

    for i in jsonData["cases_time_series"]:
        print(f'patients: {i["totalconfirmed"]}')
        plt.plot([i["totalconfirmed"]])
        plt.ylabel("some numbers")
        plt.show()




if __name__ == '__main__':
    main()
