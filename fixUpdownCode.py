import csv
import os

errorLines = ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1063', '1067', '1071', '1075']


def fixUpdownCode():
    dates = os.listdir('data/location')
    for date in dates:
        for errorLine in errorLines:
            temp = []
            inputFile = open('data/location/{}/{}.csv'.format(date, errorLine), 'r')
            lines = csv.reader(inputFile)
            for line in lines:
                temp.append(line)
            inputFile.close()
            outputFile = open('data/location/{}/{}.csv'.format(date, errorLine), 'w', encoding='euc-kr', newline='')
            csvWriter = csv.writer(outputFile)
            for row in temp:
                if errorLine == '1063':
                    csvWriter.writerow([row[0], row[1], row[2], row[3], row[4], (int(row[1])+1) % 2 + 1])
                else:
                    csvWriter.writerow([row[0], row[1], row[2], row[3], row[4], int(row[1]) % 2 + 1])
            outputFile.close()


fixUpdownCode()


