import csv
from collections import defaultdict
dict = {}
with open ('Shares.csv', newline='') as csvfile:
    totalValidLines = 0
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        #print(' '.join(row))
        if len(row) == 8:
            print(row)
            if row[0] == 'NSE' or row[0] == 'BSE':
                totalValidLines += 1
                #This is the actual line which contains information
                if row[2] in dict:
                    #This scrip is already available in the dictionary
                    dict[row[2]].append({row[1], row[3], row[4], row[5], row[6]})
                else:
                    dict[row[2]] = list()
                    dict[row[2]].append({row[1], row[3], row[4], row[5], row[6]})
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
    print (scripName)
    scripDetails = dict[scripName]
    print (scripDetails)
    for detail in scripDetails:
        if detail[1] == 'SELL':
            totalSell -= int(detail[4])
        if detail[1] == 'BUY':
            totalBuy += int(detail[4])

print (totalBuy - totalSell)