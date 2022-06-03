import calendar, datetime, os, json, requests
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

length = len(watchlist)

def Dayofweek(date):
    dow = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    return (calendar.day_name[dow])

def Documentsdir():

    username = getuser()

    if system() == "Windows":
        return "C:\\Users\\" + username + "\\Documents\\"

    elif system() == "Linux":
        return "/home/" + username + "/Documents/"

    elif system() == "Darwin":
        return "/Users/" + username + "/Documents/"

    else:
        print("BSD?!")


def lastMarketClose():
    today = datetime.datetime.now().date()

    if Dayofweek(str(today)) == "Monday":

        last_friday = str(today - datetime.timedelta(days=3))
    
        return formatDate(last_friday)

    elif Dayofweek(str(today)) == "Sunday":
    
        last_friday = str(today - datetime.timedelta(days=2))
        
        return formatDate(last_friday)

    else:

        yesterday = str(today - datetime.timedelta(days=1))

        return formatDate(yesterday)


def formatDate(date):

        y, m, d = date.split("-")

        return m + '/' + d + '/' + y


def fetchCMEData():

    url = "https://www.cmegroup.com/CmeWS/mvc/Settlements/Futures/Settlements/146/FUT?tradeDate=" + lastMarketClose()
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}
    #url = 'https://www.cmegroup.com/CmeWS/mvc/Quotes/Future/146/G?'
    page = requests.get(url, headers=headers).text
    data = json.loads(page)

    global settlements

    try:

        print(url)
        settlements = data["settlements"]

    except:

        print("Error fetching CME vars")

def printSelection():
    print("\n")
    for i in range(5):
        temp = dict(settlements[i])
        name = temp['month']
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
    global op
    global hi
    global lo
    global ps
    global vl

    name = temp['month']
    if temp['open'] == '-':
        op = None

    elif temp['high'] == '-':
        hi = None

    elif temp['low'] == '-':
        lo = None

    elif temp['settle'] == '-':
        ps = None

    elif temp['volume'] == '-':
        vl = None

    else:
        op = float(temp['open'])
        hi = float(temp['high'])
        lo = float(temp['low'])
        ps = float(temp['settle'])

        volc = temp['volume']
        vl = int(volc.replace(",", ""))

    if op == None or hi == None or lo == None or ps == None:
        print("Can't get required variables from CME")
        quit()

    else:
        arth(hi, lo, ps)


def printInfo():
    print("\n " + name + "\n")
    print(" Open         :     " + str(op) + "\n")
    print(" High         :     " + str(hi) + "\n")
    print(" Low          :     " + str(lo) + "\n")
    print(" Prior Settle :     " + str(ps) + "\n")
    print(" Volume       :     " + str(vl) + "\n")
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
    reading[33] = "CL = %s;" % (ps)

    with open(Documentsdir() + "pivotsSTUDY.ts", 'w+') as writing:
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
    print(" S3           :" + "     {:.2f}".format(s3) + "\n")


def printInstr():
    print("*STUDY.ts File Location > " + Documentsdir() + "pivotsSTUDY.ts")
    print("""
    Instructions for TOS:\n
    1. Open ThinkOrSwim
    2. Go to the Charts Tab
    3. Click on Studies > Edit Studies(Ctrl+E) > Import (Bottom Left)
    4. Select pivotsSTUDY.ts

    Always select Import and proceed to import
    for EACH INDIVIDUAL USE OF SCRIPT

    Press 'Enter' to exit
    """)
    input("") # Let's you read before closing


def parseNwrite(num):
    global temp

    temp = dict(settlements[num])
    getInfo()
    printInfo()
    writeTS()
    printInstr()


def stocks():
    

def futures():
    fetchCMEData()
    printSelection()
    selSYM = int(input("Pick 0 - 4\nEnter number of selection:\n"))
    parseNwrite(selSYM)


futures()
