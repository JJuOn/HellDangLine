import matplotlib.pyplot as plt
import csv
import os


def getGraph():
    subwayDifference = []
    fileNameList = os.listdir('data/result')
    for fileName in fileNameList:
        split = fileName.split('_')
        subwayId = split[0]
        stationName = split[1]
        weekday = split[2]
        updown = split[3][:-4]
        inputFile = open('data/result/'+fileName, 'r')
        lines = csv.reader(inputFile)
        count = 0
        sum = 0
        for line in lines:
            sum += int(line[2])
            count += 1
        found = False
        if not isSubwayIdExists(subwayDifference, subwayId):
            subwayDifference.append({'subwayId': subwayId, 'stations': []})
        for row in subwayDifference:
            if row['subwayId'] == subwayId:
                for station in row['stations']:
                    if station['stationName'] == stationName and station['weekday'] == weekday:
                        found = True
                        station['difference'] += sum
                        station['count'] += count
        if not found:
            for row in subwayDifference:
                if row['subwayId'] == subwayId:
                    row['stations'].append({'stationName': stationName, 'weekday': weekday, 'difference': sum, 'count': count})
    for row in subwayDifference:
        for station in row['stations']:
            if station['count'] != 0:
                station['difference'] = station['difference'] // station['count']
    print(subwayDifference)


def isSubwayIdExists(dictList, subwayId):
    for row in dictList:
        if row['subwayId'] == subwayId:
            return True
    return False

getGraph()