import csv
import os


def getTimeaverage():
    targetFileList = os.listdir('data/timesum')
    for targetFile in targetFileList:
        print('processing : '+targetFile)
        inputFile = open('data/timesum/'+targetFile, 'r')
        lines = csv.reader(inputFile)
        temp = []
        for line in lines:
            temp.append([line[0], line[1], int(line[2])//int(line[3])])
        inputFile.close()
        if not os.path.exists('data/timeaverage'):
            os.mkdir('data/timeaverage')
        outputFile = open('data/timeaverage/'+targetFile, 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(outputFile)
        for row in temp:
            csvWriter.writerow(row)
        outputFile.close()


getTimeaverage()
