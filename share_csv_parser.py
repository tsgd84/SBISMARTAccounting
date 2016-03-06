import csv
from datetime import datetime

import ScripDetail

def computeMargin(scripName, scripDetails = []):
    sellOrders = [sellOrder for sellOrder in scripDetails if sellOrder.orderType == 'SELL']
    buyOrders = [buyOrder for buyOrder in scripDetails if buyOrder.orderType == 'BUY']
    totalSoldQuantity = sum(c.quantity for c in sellOrders)
    soldAmount = 0.0
    boughtAmount = 0.0
    totalBoughtAmount = 0.0
    totalMargin = 0.0
    totalTransactionAmount = 0.0

    if totalSoldQuantity > 0:
        for sellOrder in sellOrders:
            for buyOrder in buyOrders:
                if(buyOrder.remainingQuantity > 0 and sellOrder.remainingQuantity > 0):
                    soldQuantityRemaining = sellOrder.remainingQuantity
                    if buyOrder.remainingQuantity > soldQuantityRemaining:
                        soldAmount = (soldQuantityRemaining * sellOrder.price)
                        boughtAmount = (buyOrder.price * soldQuantityRemaining)
                        buyOrder.remainingQuantity = buyOrder.remainingQuantity - soldQuantityRemaining
                        sellOrder.remainingQuantity = 0
                    elif buyOrder.remainingQuantity < soldQuantityRemaining:
                        soldAmount = (buyOrder.remainingQuantity * sellOrder.price)
                        boughtAmount = (buyOrder.price * buyOrder.remainingQuantity)
                        sellOrder.remainingQuantity = sellOrder.remainingQuantity - buyOrder.remainingQuantity
                        buyOrder.remainingQuantity = 0
                    else:
                        soldAmount = (sellOrder.remainingQuantity * sellOrder.price)
                        boughtAmount = (buyOrder.price * buyOrder.remainingQuantity)
                        buyOrder.remainingQuantity = sellOrder.remainingQuantity = 0

                    totalBoughtAmount += boughtAmount
                    totalTransactionAmount +=  (soldAmount + boughtAmount)
                    totalMargin += (soldAmount - boughtAmount)

        #print('Total boughtAmount : ', totalBoughtAmount)
        #print('Total transaction Amount : ', totalTransactionAmount)
        if totalBoughtAmount > 0 :
            print(key , " : ", (totalMargin * 100)/totalBoughtAmount)
            
dict = {}
with open ('Shares.csv', newline='') as csvfile:
    totalValidLines = 0
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        #print(' '.join(row))
        if len(row) == 8:
            #print(row)
            if row[0] == 'NSE' or row[0] == 'BSE':
                totalValidLines += 1
                #This is the actual line which contains information
                if row[2] in dict:
                    #This scrip is already available in the dictionary
                    dict[row[2]].append(ScripDetail.make_ScripDetail(row[1], row[3], int(row[4]), float(row[5]), float(row[6])))
                else:
                    dict[row[2]] = [];
                    dict[row[2]].append(ScripDetail.make_ScripDetail(row[1], row[3], int(row[4]), float(row[5]), float(row[6])))
        else:
            print('No. of colums in the csv file is not equal to 8')
            exit()

print ('Total number of valid lines : ', totalValidLines)

totalLinesParsed = 0
for key in dict.keys():
    #print (key)
    value = dict[key]
    totalLinesParsed += len(value)

print ('Total number of lines parsed : ', totalLinesParsed)
print ('Total items in the dictionary : ', len(dict))

if totalValidLines != totalLinesParsed:
    print ('There is a mismatch between the valid lines and number of lines parsed ',  totalValidLines,' != ', totalLinesParsed)
    exit()


#Calculate the profit/loss in each scrip
totalBuy = 0
totalSell = 0

for key in dict.keys():
    scripName = key
    scripDetails = dict[scripName]
    scripDetails.sort(key=lambda detail: detail.date)
    scripTotalSell = 0
    scripTotalBuy = 0
    scripCount = 0;
    scripsSoldNo = 0;
    scripsBoughtNo = 0;
    scripAverageBoughtPrice = 0;

    computeMargin(key, scripDetails)

    for detail in scripDetails:
        #adding up sell together
        if detail.orderType == 'SELL':
            scripTotalSell += detail.totalPrice
            scripsSoldNo += detail.quantity
        #adding up buy together
        if detail.orderType == 'BUY':
            #Since BUY items are marked as negative making them positive by negating it with minus symbol
            scripTotalBuy += detail.totalPrice
            scripsBoughtNo += detail.quantity

    if scripsBoughtNo > 0 and scripsSoldNo > 0 :
        scripAverageBoughtPrice = scripTotalBuy/scripsBoughtNo
        scripGainOrLoss = (((scripAverageBoughtPrice * scripsSoldNo) - scripTotalSell) * 100)/scripTotalSell
        #print('Capital gain/loss percentage in the scrip ', scripName, ' : ', '%.sf' %scripGainOrLoss)

    totalSell += scripTotalSell
    totalBuy += scripTotalBuy
    #print (scripName , '\t\t', scripCount, '\t', scripTotalBuy - scripTotalSell)

print('Total capital outflow : ', "%.2f" %totalBuy)
print('Total capital inflow  : ', "%.2f" %totalSell)
print('Total investment     : ', "%.2f" %(totalBuy - totalSell))