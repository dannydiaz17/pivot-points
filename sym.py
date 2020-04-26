
'''def select():
    fetch()
    arth()
    writer()
    printInfo()

#from parse import *
'''

List = []

class SYMBOL:
    def __init__(self, list, hi, lo, ps, vl):
        product = list['productCode']
        self.symbol = list['code']
        symbol = self.symbol

        hi = float(list['high'])
        lo = float(list['low'])
        ps = float(list['priorSettle'])

        volc = list['volume']
        self.vl = volc.replace(",", "")

        List.append(symbol)

    def update(self):
        # self.Mnth() = ?
        pass

fetch()

print(List)
# Symbol List
