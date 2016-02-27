class ScripDetail1(object):
    _date = ""
    _orderType = ""
    _quantity = 0
    _price = 0
    _totalPrice = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, Date, OrderType, Quantity, Price, TotalPrice):
        self._date = Date
        self._orderType = OrderType
        self._quantity = Quantity
        self._price = Price
        self._totalPrice = TotalPrice

def make_ScripDetail(Date, OrderType, Quantity, Price, TotalPrice):
    scripDetail = ScripDetail1(Date, OrderType, Quantity, Price, TotalPrice)
    return scripDetail

@property
def date(self):
    return self._date

@property
def orderType(self):
    return self._orderType

@property
def quantity(self):
    return self._quantity

@property
def price(self):
    return self._price

@property
def totalPrice(self):
    return self._totalPrice
