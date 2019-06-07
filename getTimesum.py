import os
import csv


def getTimeSum():
    # dates = os.listdir('data/location')
    dates = ['20190607']
    for date in dates:
        locationFiles = os.listdir('data/location/'+date)
        for locationFile in locationFiles:
            file1 = open('data/location/'+date+'/'+locationFile, 'r')
            lines1 = csv.reader(file1)
            subwayId = locationFile[:-4]
            for line1 in lines1:
                stationId = line1[0]
                trainNo = line1[1]
                destination = line1[2]
                arrivalTime = line1[3]
                weekday = line1[4]
                updown = line1[5]
                if not os.path.exists('data/timesum'):
                    os.mkdir('data/timesum')
                print('date : {}, subwayId : {}, stationId : {}'.format(date, subwayId, stationId))
                if os.path.exists('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown)):
                    file2 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'r')
                    lines2 = csv.reader(file2)
                    temp = []
                    for line2 in lines2:
                        temp.append(line2)
                    file2.close()
                    file3 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file3)
                    found = False
                    for row in temp:
                        if (row[0] == trainNo) and (row[1] == destination):
                            found = True
                            row[2] = int(row[2]) + timeToSecond(arrivalTime)
                            row[3] = int(row[3]) + 1
                        csvWriter.writerow(row)
                    if not found:
                        csvWriter.writerow([trainNo, destination, timeToSecond(arrivalTime), 1])
                    file3.close()
                else:
                    print('doesn\'t exists')
                    file2 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file2)
                    csvWriter.writerow([trainNo, destination, timeToSecond(arrivalTime), 1])
                    file2.close()


def timeToSecond(time):
    timeList = time.split(':')
    if timeList[0] == '0':
        timeList[0] = '24'
    elif timeList[0] == '1':
        timeList[0] = '25'
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])


getTimeSum()


