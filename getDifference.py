import csv
import os
import operator


subwayIds = ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1063', '1065', '1067', '1071', '1075']
lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'GyeonguiJoungang', 'Airport', 'GyeongChun', 'Suin', 'Bundang']
trainNoStr = ['K', 'S', 'C', 'A']


def getDifference():
    for i in range(0, 14):
        idList = []
        idFile = open('data/metroId/line'+lineNames[i]+'.csv', 'r')
        lines1 = csv.reader(idFile)
        for line in lines1:
            idList.append(line)
        idFile.close()
        for station in idList:
            for weekday in range(1, 4):
                for updown in range(1, 3):
                    print('{}_{}_{}_{}.csv'.format(subwayIds[i], station[3], weekday, updown))
                    timeAverageList = []
                    if not os.path.exists('data/timeaverage/{}_{}_{}_{}.csv'.format(subwayIds[i], station[1], weekday, updown)):
                        continue
                    timeAverageFile = open('data/timeaverage/{}_{}_{}_{}.csv'.format(subwayIds[i], station[1], weekday, updown), 'r')
                    lines2 = csv.reader(timeAverageFile)
                    for line in lines2:
                        timeAverageList.append(line)
                    timeAverageFile.close()
                    timetableList = []
                    if not os.path.exists('data/timetable/{}_{}_{}_{}.csv'.format(subwayIds[i], station[3], weekday, updown)):
                        continue
                    timetableFile = open('data/timetable/{}_{}_{}_{}.csv'.format(subwayIds[i], station[3], weekday, updown), 'r')
                    lines3 = csv.reader(timetableFile)
                    for line in lines3:
                        timetableList.append(line)
                    timetableFile.close()
                    del timetableList[0]
                    result = []
                    for timetableRow in timetableList:
                        trainNoInTimetable = delAlphabetInTrainNo(timetableRow[0])
                        arrivaltimeInTimetable = timeToSecond(timetableRow[3])
                        lefttimeInTimetable = timeToSecond(timetableRow[4])
                        for timeAverageRow in timeAverageList:
                            if timeAverageRow[0] == trainNoInTimetable:
                                if arrivaltimeInTimetable != 0:
                                    print('found')
                                    difference = abs(arrivaltimeInTimetable - int(timeAverageRow[2]))
                                    result.append([station[2], timeAverageRow[1], difference])
                    if not os.path.exists('data/result'):
                        os.mkdir('data/result')
                    resultFile = open('data/result/{}_{}_{}_{}.csv'.format(subwayIds[i], station[2], weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(resultFile)
                    for row in result:
                        csvWriter.writerow(row)
                    resultFile.close()





def secondToTime(timesum):
    hour = int(timesum)//3600
    minute = (int(timesum)-hour*3600)//60
    second = int(timesum) % 60
    timestring = "{}:{}:{}".format(hour, minute, second)
    return timestring


def timeToSecond(time):
    print(time)
    timeList = time.split(':')
    if timeList[0] == '0':
        timeList[0] = '24'
    elif timeList[0] == '1':
        timeList[0] = '25'
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])


def isTimeZero(time):
    return timeToSecond(time) == 0


def delAlphabetInTrainNo(string):
    for i in range(0, len(trainNoStr)):
        if trainNoStr[i] in string:
            return string.replace(trainNoStr[i], '')


getDifference()

