import csv
from datetime import datetime

import ScripDetail

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
                    dict[row[2]].append(ScripDetail.make_ScripDetail(row[1], row[3], row[4], row[5], row[6]))
                else:
                    dict[row[2]] = [];
                    dict[row[2]].append(ScripDetail.make_ScripDetail(row[1], row[3], row[4], row[5], row[6]))
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

    for detail in scripDetails:
        #adding up sell together
        if detail.orderType == 'SELL':
            scripTotalSell += float(detail.totalPrice)
            scripsSoldNo += -int(detail.quantity)
        #adding up buy together
        if detail.orderType == 'BUY':
            #Since BUY items are marked as negative making them positive by negating it with minus symbol
            scripTotalBuy += -float(detail.totalPrice)
            scripsBoughtNo += int(detail.quantity)

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

