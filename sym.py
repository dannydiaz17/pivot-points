from datetime import datetime

mcode = {
    "01" : "F",
    "02" : "G",
    "03" : "H",
    "04" : "J",
    "05" : "K",
    "06" : "M",
    "07" : "N",
    "08" : "Q",
    "09" : "U",
    "10" : "V",
    "11" : "X",
    "12" : "Z"
    }

now = datetime.now()

symList = []

class SYM:
    def __init__(self, Smbl):
        self.Smbl = Smbl
        self.Mnth = mcode.get(now.strftime("%m"))
        self.Year = int(now.strftime("%Y")) - 2000
        self.FSYM = Smbl + self.Mnth + str(self.Year)
        symList.append(Smbl)

    def update(self):
        # self.Mnth() = ?
        pass


# Symbol List
NQ = SYM('NQ')
