import os
import csv


def getTimeSum():
    dates = os.listdir('data/location')
    for date in dates:
        locationFiles = os.listdir('data/location/'+date)
        for locationFile in locationFiles:
            file1 = open('data/location/'+date+'/'+locationFile, 'r')
            lines1 = csv.reader(file1)
            subwayId = locationFile[:-4]
            print(subwayId)
            for line1 in lines1:
                stationId = line1[0]
                trainNo = line1[1]
                destination = line1[2]
                arrivalTime = line1[3]
                weekday = line1[4]
                updown = line1[5]
                if os.path.exists('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown)):
                    file2 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'r')
                    lines2 = csv.reader(file2)
                    file2.close()
                    file3 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file3)
                    found = False
                    for line2 in lines2:
                        if line2[0] == trainNo and line2[1] == destination:
                            found = True
                            line2[2] = int(line2[2]) + timeToSecond(arrivalTime)
                            line2[3] = int(line2[3]) + 1
                        csvWriter.writerow(line2)
                    if not found:
                        csvWriter.writerow([trainNo, destination, arrivalTime, 1])
                    file3.close()
                else:
                    file2 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file2)
                    csvWriter.writerow([trainNo, destination, arrivalTime, 1])
                    file2.close()


def timeToSecond(time):
    timeList = time.split(':')
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])


getTimeSum()




