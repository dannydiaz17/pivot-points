import os, json, requests
from getpass import getuser
from platform import system


global empty


empty = False
invalid = False


#symbol = str(input("Which symbol would you like pivots for?\n"))


stocks = ["AAPL","AMD","FB","MSFT","NFLX","QQQ","RYCEY","SNAP","SPY","TSLA"]
futures = ["/NQ","/ES"]
forex = ["USD/JPY"]

watchlist = stocks + futures + forex


apikey = "NVRL5VTZOILNK0RFHAAHO0FU8TX5PPJI"

username = getuser()

system = system()

length = len(watchlist)


def Documentsdir():


    if system == "Windows":
        return "C:\\Users\\" + username + "\\Documents\\"

    elif system == "Linux":
        return "/home/" + username + "/Documents/"

    elif system == "Darwin":
        return "/Users/" + username + "/Documents/"

    else:
        print("BSD?!")



def flist(watchlist):

    flist = str(watchlist)
    flist = flist.replace("'",'')
    flist = flist.replace('[','')
    flist = flist.replace(']','')
    flist = flist.replace('/','%2F')
    flist = flist.replace(',','%2C')
    flist = flist.replace(' ','')

    return flist


def calculatePivots(data):
    # Pivot math

    h = data[0]
    l = data[1]
    c = data[2]


    p = (h + l + c)/3
    r1 = (2 * p) - l
    r2 = p + h - l
    r3 = h + 2 * (p - l)
    s1 = (2 * p) - h
    s2 = p - h + l
    s3 = l - 2 * (h - p)

    return r3,r2,r1,p,s1,s2,s3


def get_todays_data():

    global data

    url = "https://api.tdameritrade.com/v1/marketdata/quotes?apikey=" + apikey + "&symbol=" + flist(watchlist)
    page = requests.get(url).text
    data = dict(json.loads(page))


def getOHLC(product):

    global symbol
    global asset
    global op
    global cl
    global hi
    global lo

    try:

        info = dict(data[product])

        if info['assetMainType'] == "FUTURE":

             symbol = info['futureActiveSymbol']
             asset = info['assetMainType']
             op = float(info['openPriceInDouble'])
             cl = float(info['futureSettlementPrice'])
             hi = float(info['highPriceInDouble'])
             lo = float(info['lowPriceInDouble'])


        elif info['assetMainType'] == "EQUITY":

             symbol = info['symbol']
             asset = info['assetMainType']
             op = float(info['openPrice'])
             cl = float(info['lastPrice'])
             hi = float(info['highPrice'])
             lo = float(info['lowPrice'])


        elif info['assetMainType'] == "FOREX":

             symbol = info['symbol']
             asset = info['assetMainType']
             op = float(info['openPriceInDouble'])
             cl = float(info['closePriceInDouble'])
             hi = float(info['highPriceInDouble'])
             lo = float(info['lowPriceInDouble'])

        else:

             print("Unsupported Product")

        return hi,lo,cl

    except:

        print("Error")


def printInfo():
    print("\n " + symbol + "\n")
    print("____________________________________________\n\n")
    print(" Open         :     " + str(op) + "\n")
    print(" High         :     " + str(hi) + "\n")
    print(" Low          :     " + str(lo) + "\n")
    print(" Close        :     " + str(cl) + "\n")
    printPivots()


def writeTS():

    reading = open("pivo.ts", 'r+').read().splitlines()

    reading[22] = "R3 = %.2f;" % (r3)
    reading[23] = "R2 = %.2f;" % (r2)
    reading[24] = "R1 = %.2f;" % (r1)
    reading[25] = "PP = %.2f;" % (p)
    reading[26] = "S1 = %.2f;" % (s1)
    reading[27] = "S2 = %.2f;" % (s2)
    reading[28] = "S3 = %.2f;" % (s3)
    reading[29] = "\n"
    reading[30] = "OP = %s;" % (op)
    reading[31] = "HI = %s;" % (hi)
    reading[32] = "LO = %s;" % (lo)
    reading[33] = "CL = %s;" % (cl)

    with open(Documentsdir() + symbol.replace("/","_") + "_STUDY.ts", 'w+') as writing:
        writing.write("\n".join(reading))
        writing.close()


def printPivots():
    print("\n")
    print(" R3           :" + "     {:.2f}".format(r3) + "\n")
    print(" R2           :" + "     {:.2f}".format(r2) + "\n")
    print(" R1           :" + "     {:.2f}".format(r1) + "\n")
    print(" PIVOT        :" + "     {:.2f}".format(p)  + "\n")
    print(" S1           :" + "     {:.2f}".format(s1) + "\n")
    print(" S2           :" + "     {:.2f}".format(s2) + "\n")
    print(" S3           :" + "     {:.2f}".format(s3) + "\n\n\n")


def printHelp():
    print(" *STUDY.ts File Location > " + Documentsdir() + "{SYMBOL}_STUDY.ts")
    print("""
    Instructions for TOS:\n
    1. Open ThinkOrSwim
    2. Go to the Charts Tab
    3. Click on Studies > Edit Studies(Ctrl+E) > Import (Bottom Left)
    4. Hold Ctrl + {Click} to select all {SYMBOL}_STUDY.ts files

    Always select Import and proceed to import
    for EACH INDIVIDUAL USE OF SCRIPT

    Press 'Enter' to exit
    """)
    input("") # Let's you read before closing

def main():

        printInfo()
        writeTS()

#os.system('clear')

get_todays_data()

for products in data:

    r3,r2,r1,p,s1,s2,s3 = calculatePivots(getOHLC(products))
    main()

printHelp()
