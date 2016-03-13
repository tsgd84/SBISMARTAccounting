class TranscationData(object):
    _soldAmount = 0
    _boughtAmount = 0

    def __init__(self, SoldAmout, BoughtAmount):
        self._boughtAmount = BoughtAmount
        self._soldAmount = SoldAmout

    @property
    def boughtAmount(self):
        return self._boughtAmount

    @property
    def soldAmount(self):
        return self._soldAmount

class ScripTransaction(object):
    _scripName = ""
    _shortTermTransactions = list()
    _longTermTransactions = list()

    # The class "constructor" - It's actually an initializer
    def __init__(self, ScripName):
        self._scripName = ScripName
        self._shortTermTransactions = []
        self._longTermTransactions = []

    @property
    def scripName(self):
        return self._scripName

    @property
    def shortTermTrans(self):
        return self._shortTermTransactions

    @property
    def longTermTrans(self):
        return self._longTermTransactions

class FinYearWiseData(object):
    _financialYear = ""
    _scripTransactions = []

    # The class "constructor" - It's actually an initializer
    def __init__(self, FinancialYear):
        self._financialYear = FinancialYear
        self._scripTransactions = []

    @property
    def financialYear(self):
        return self._financialYear

    @property
    def scripTransactions(self):
        return self._scripTransactions

    @scripTransactions.setter
    def scripTransactions(self, value):
        self._scripTransactions = value

    def getMargin(self, transactionType):
        toReturn = {}
        if transactionType == "ShortTerm":
            for scripTransaction in self._scripTransactions:
                soldAmtTotal = sum(x.soldAmount for x in scripTransaction.shortTermTrans)
                boughtAmtTotal = sum(x.boughtAmount for x in scripTransaction.shortTermTrans)
                toReturn[scripTransaction._scripName] = ((soldAmtTotal - boughtAmtTotal)*100/boughtAmtTotal if boughtAmtTotal > 0 and soldAmtTotal > 0 else 0)
        elif transactionType == "LongTerm":
            for scripTransaction in self._scripTransactions:
                soldAmtTotal = sum(x.soldAmount for x in scripTransaction.longTermTrans)
                boughtAmtTotal = sum(x.boughtAmount for x in scripTransaction.longTermTrans)
                toReturn[scripTransaction._scripName] = ((soldAmtTotal - boughtAmtTotal)*100/boughtAmtTotal if boughtAmtTotal > 0 and soldAmtTotal > 0 else 0)
        return toReturn