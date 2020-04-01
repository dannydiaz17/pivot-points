import requests
import json
from sym import *

def fetch():
    url = 'https://www.cmegroup.com/CmeWS/mvc/Quotes/Future/146/G?pageSize\
    =50&_=1580536038065'
    page = requests.get(url).text
    data = json.loads(page)

# Nested Dictionaries
    # qudict as in Quotes Dict
    # dict_num, each number is a different contract of the same symbol
    global dict_0
    global dict_1
    global dict_2
    global dict_3
    global dict_4

    qudict = data["quotes"]
    dict_0 = qudict[0]
    dict_1 = qudict[1]
    dict_2 = qudict[2]
    dict_3 = qudict[3]
    dict_4 = qudict[4]

    global hi
    global lo
    global ps

def getInfo(list):

    global vol

    hi = float(list['high'])
    lo = float(list['low'])
    ps = float(list['priorSettle'])

    volc = list['volume']               # volc = volume with comma
    vol = int(volc.replace(",", ""))

def addtoList(list):
    i = 0
    for i in range(4):
        symbol(list)
        i = i + 1
        print("Done")
fetch()
getInfo()
addtoList()
