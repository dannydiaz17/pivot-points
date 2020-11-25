import os
import json
import requests
from getpass import getuser
from platform import system


global empty
global symbol


empty = False
invalid = False


#symbol = str(input("Which symbol would you like pivots for?\n"))


stocks = ["AAPL","AMD","FB","TSLA","MSFT","NFLX","QQQ","RYCEY","SNAP"]
futures = []
watchlist = stocks + futures


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


def defineVars():

    global op
    global hi
    global lo
    global cl

    op = float(todays_ohlc[0])
    hi = float(todays_ohlc[2])
    lo = float(todays_ohlc[1])
    cl = float(todays_ohlc[3])

    getPivots(hi,lo,cl)

def getPivots(h, l, c):
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


def get_todays_ohlc(symbol):

    global todays_ohlc

    global todays_pivots

    url = "https://api.tdameritrade.com/v1/marketdata/" + symbol + "/pricehistory?apikey=" + apikey + "&periodType=month&period=1&frequencyType=daily&frequency=1&needExtendedHoursData=true"

    page = requests.get(url).text

    data = json.loads(page)

    if data["empty"] == 'true':

        empty = True
        pass

    else:

        try:

            candles = tuple(data["candles"])
            daily_ohlc = []
            pivots = []

            days_of_data = len(candles)

            for i in range(days_of_data):

                day_data = candles[i]

                op = float(day_data["open"])
                hi = float(day_data["high"])
                lo = float(day_data["low"])
                cl = float(day_data["close"])

                ohlc = (op, lo, hi, cl)
                daily_ohlc.append(ohlc)

                pivot_points = getPivots(hi,lo,cl)
                pivots.append(pivot_points)

                try:

                    todays_pivots = pivots[-1]
                    todays_ohlc = daily_ohlc[-1]

                except:

                     print("Invalid Symbol")
                     invalid = True
                     pass

            return todays_ohlc


        except:

            pass


def get_todays_pivots():

    return todays_pivots


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

    with open(Documentsdir() + symbol + "_STUDY.ts", 'w+') as writing:
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

    defineVars()

    if invalid == True:

        pass

    else:

        printInfo()
        writeTS()

os.system('clear')

for i in range(length):

    symbol = watchlist[i]

    todays_ohlc = get_todays_ohlc(watchlist[i])
    todays_pivots = get_todays_pivots()

    main()

printHelp()
