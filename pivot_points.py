
import json
import requests


def fetch():
    url = 'https://www.cmegroup.com/CmeWS/mvc/Quotes/Future/146/G?pageSize\
    =50&_=1580536038065'
    page = requests.get(url).text
    data = json.loads(page)

# Nested Dictionaries
    # qudict as in Quotes Dict
    # fdict as in Final Dict
    qudict = data["quotes"]
    fdict = qudict[0]

    for i in range(5):
        SYMBOL(qudict[i])
        print()

    global hi
    global lo
    global ps
    global vl


    hi = float(fdict['high'])
    lo = float(fdict['low'])
    ps = float(fdict['priorSettle'])


    # I'm leaving this line in for future debugging
    # pretty = json.dumps(data,indent=4, separators=(',', ':'))


def arth():
    # Pivot math
    h = hi
    l = lo
    c = ps

    global p
    global r1
    global r2
    global r3
    global s1
    global s2
    global s3

    p = (h + l + c)/3
    r1 = (2 * p) - l
    r2 = p + h - l
    r3 = h + 2 * (p - l)
    s1 = (2 * p) - h
    s2 = p - h + l
    s3 = l - 2 * (h - p)


def writer():

    reading = open("pivo.ts", 'r+').read().splitlines()

    reading[16] = "R3 = %.2f;" % (r3)
    reading[17] = "R2 = %.2f;" % (r2)
    reading[18] = "R1 = %.2f;" % (r1)
    reading[19] = "PP = %.2f;" % (p)
    reading[20] = "S1 = %.2f;" % (s1)
    reading[21] = "S2 = %.2f;" % (s2)
    reading[22] = "S3 = %.2f;" % (s3)

    with open("pivotsSTUDY.ts", 'w+') as writing:
        writing.write("\n".join(reading))
        writing.close()


def printInfo(symbl):
    print("Symbol: " + symbl + "\n")
    print("R3:" + "{:.2f}".format(r3) + "\n")
    print("R2:" + "{:.2f}".format(r2) + "\n")
    print("R1:" + "{:.2f}".format(r1) + "\n")
    print("PIVOT:" + "{:.2f}".format(p) + "\n")
    print("S1:" + "{:.2f}".format(s1) + "\n")
    print("S2:" + "{:.2f}".format(s2) + "\n")
    print("S3:" + "{:.2f}".format(s3) + "\n")


#from parse import *


List = []

class SYMBOL:
    def __init__(self, list):
        self.symbol = list['code']
        symbol = self.symbol

        if list['high'] != '-' or list['low'] != '-' or list['priorSettle'] != '-':
            sw = 1
        else:
            sw = 2

        def dashCase():
            self.hi = list['high']
            self.lo = list['low']
            self.ps = list['priorSettle']

        def othrCase():
            self.hi = float(list['high'])
            self.lo = float(list['low'])
            self.ps = float(list['priorSettle'])

        switch = {1 : dashCase,
                  2 : othrCase,
        }

        switch[sw]()
        volc = list['volume']
        self.vl = volc.replace(",", "")

        List.append(symbol)

    def update(self):
        # self.Mnth() = ?
        pass

fetch()

print(List)
# Symbol List
