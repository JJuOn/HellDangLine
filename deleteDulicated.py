import os
import csv


def deleteDuplicated():
    targetDate = '20190606'
    fileNameList = os.listdir('data/location/{}'.format(targetDate))
    for fileName in fileNameList:
        print(fileName)
        original = open('data/location/{}/{}'.format(targetDate, fileName), 'r')
        lines = csv.reader(original)
        temp = []
        for line in lines:
            if not line in temp:
                temp.append(line)
            else:
                print('found duplicated')
        original.close()
        output = open('data/location/{}/{}'.format(targetDate, fileName), 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(output)
        for row in temp:
            csvWriter.writerow(row)
        output.close()


deleteDuplicated()