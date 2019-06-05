import os
import csv


def removeDuplicatedTrainNo():
    fileList = os.listdir('data/timetable')
    for fileName in fileList:
        if '1002_211' in fileName:
            input = open('data/timetable/'+fileName, 'r')
            lines = csv.reader(input)
            result = []
            for line in lines:
                if line[1] == line[2]:
                    if timeToSecond(line[3]) == 0:
                        result.append(line)
                else:
                    result.append(line)
            input.close()
            output = open('data/timetable/'+fileName, 'w', encoding='euc-kr', newline='')
            csvWriter = csv.writer(output)
            for row in result:
                csvWriter.writerow(row)
            output.close()


def timeToSecond(time):
    timeList = time.split(':')
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])

removeDuplicatedTrainNo()
