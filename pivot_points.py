import json
import requests


def fetch():
    url = 'https://www.cmegroup.com/CmeWS/mvc/Quotes/Future/146/G?pageSize\
    =50&_=1580536038065'
    page = requests.get(url).text
    data = json.loads(page)

    global qudict
    # Nested Dictionaries
        # qudict as in Quotes Dict
        # fdict as in Final Dict
    qudict = data["quotes"]

    ## I'm leaving this line in for future debugging
    ## pretty = json.dumps(data,indent=4, separators=(',', ':'))


def printSelection():
    print("\n")
    for i in range(5):
        temp = dict(qudict[i])
        name = temp['code']
        vol = temp['volume']
        print(str(i) + ": " + name + " Volume - " + str(vol) + "\n")


def arth(h, l, c):
    # Pivot math

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


def getInfo():

    global name
    global hi
    global lo
    global ps
    global vl

    name = temp['code']

    if temp['high'] == '-':

        hi = None

    elif temp['low'] == '-':

        lo = None

    elif temp['priorSettle'] == '-':

        ps = None

    elif temp['volume'] == '-':

        vl = None

    else:
        hi = float(temp['high'])
        lo = float(temp['low'])
        ps = float(temp['priorSettle'])

        volc = temp['volume']
        vl = int(volc.replace(",", ""))
    if hi == None or lo == None or ps == None:
        print("Can't get required variables from CME")
        quit()
    else:
        arth(hi, lo, ps)


def printInfo():
    print("\n" + name + "\n")
    print("High = " + str(hi) + "\n")
    print("Low = " + str(lo) + "\n")
    print("Prior Settle = " + str(ps) + "\n")
    print("Volume = " + str(vl) + "\n")
    printPivots()


def writeTS():

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


def printPivots():
    print("\n")
    print("R3:" + "{:.2f}".format(r3) + "\n")
    print("R2:" + "{:.2f}".format(r2) + "\n")
    print("PIVOT:" + "{:.2f}".format(p) + "\n")
    print("S1:" + "{:.2f}".format(s1) + "\n")
    print("S2:" + "{:.2f}".format(s2) + "\n")
    print("S3:" + "{:.2f}".format(s3) + "\n")

#from parse import *
def printInstr():
    print("""
    Instructions for TOS:\n
    1. Open ThinkOrSwim
    2. Go to the Charts Tab
    3. Click on Studies > Edit Studies > Import (Bottom Left)
    4. Select pivotsSTUDY.ts

    Always select Import and proceed to import
    for EACH INDIVIDUAL USE OF SCRIPT
    """)
    input("") # Let's you read before closing


def run(num):
    global temp

    temp = dict(qudict[num])
    getInfo()
    printInfo()
    writeTS()
    printInstr()


def main():
    fetch()
    printSelection()
    selSYM = int(input("Pick 0 - 4\n Enter number of selection:\n"))
    run(selSYM)


if __name__ == "__main__":
    main()
