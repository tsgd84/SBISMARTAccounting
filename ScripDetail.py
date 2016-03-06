from datetime import datetime

class ScripDetail(object):
    _date = datetime.now()
    _orderType = ""
    _quantity = 0
    _price = 0
    _totalPrice = 0
    _remainingQuantity = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, Date, OrderType, Quantity, Price, TotalPrice):
        quantityInternal = Quantity
        totalPriceInternal = TotalPrice
        self._date = datetime.strptime(Date, '%d-%m-%Y')
        self._orderType = OrderType

        if self.orderType == 'SELL':
            quantityInternal = -Quantity

        self._quantity = quantityInternal
        self._remainingQuantity = quantityInternal

        self._price = Price

        if self.orderType == 'BUY':
            totalPriceInternal = -TotalPrice

        self._totalPrice = totalPriceInternal

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

    @property
    def remainingQuantity(self):
        return self._remainingQuantity

    @remainingQuantity.setter
    def remainingQuantity(self, value):
        self._remainingQuantity = value

def make_ScripDetail(Date, OrderType, Quantity, Price, TotalPrice):
    scripDetail = ScripDetail(Date, OrderType, Quantity, Price, TotalPrice)
    return scripDetail