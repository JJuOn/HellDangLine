import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import csv
import os


def getGraph():
    font_name = fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
    mpl.rc('font', family=font_name)
    mpl.rcParams.update({'figure.autolayout': True})
    subwayDifference = []
    fileNameList = os.listdir('data/result')
    for fileName in fileNameList:
        split = fileName.split('_')
        subwayId = split[0]
        stationName = split[1]
        weekday = split[2]
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
    if not os.path.exists('data/img'):
        os.mkdir('data/img')
    for wd in ['1', '2', '3']:
        x1 = []
        y1 = []
        for row in subwayDifference:
            x2 = []
            y2 = []
            subwaySum = 0
            subwayCount = 0
            for station in row['stations']:
                subwaySum += station['difference']
                subwayCount += station['count']
            subwayAverage = subwaySum // subwayCount
            row['subwayDifference'] = subwayAverage
            row['subwayCount'] = subwayCount
            for station in row['stations']:
                if station['weekday'] == wd and station['count'] != 0:
                    station['difference'] = station['difference'] // station['count']
                    x2.append(station['stationName'])
                    y2.append(station['difference'])
            print('Drawing : {}_{}'.format(row['subwayId'], wd))
            plt.figure(figsize=(16, 9))
            plt.bar(x2, y2)
            plt.xlabel('지하철 역명')
            plt.ylabel('평균 지연 시간')
            plt.title('{}_{}'.format(row['subwayId'], wd))
            plt.xticks(rotation=90)
            plt.savefig('data/img/{}_{}.png'.format(row['subwayId'], wd), dpi=500)
            plt.close()
            x1.append(row['subwayId'])
            y1.append(row['subwayDifference'])
        print('Drawing : all_{}'.format(wd))
        plt.figure(figsize=(16, 9))
        plt.bar(x1, y1)
        plt.xlabel('지하철 노선 코드')
        plt.ylabel('평균 지연 시간')
        plt.title('전체노선_{}'.format(wd))
        plt.xticks(rotation=90)
        plt.savefig('data/img/all_{}.png'.format(wd), dpi=500)
        plt.close()
        del x1[9]
        del y1[9]
        print('Drawing : except_1063_{}'.format(wd))
        plt.figure(figsize=(16, 9))
        plt.bar(x1, y1)
        plt.xlabel('지하철 노선 코드')
        plt.ylabel('평균 지연 시간')
        plt.title('전체노선_{}'.format(wd))
        plt.xticks(rotation=90)
        plt.savefig('data/img/except_1063_{}.png'.format(wd), dpi=500)
        plt.close()


def isSubwayIdExists(dictList, subwayId):
    for row in dictList:
        if row['subwayId'] == subwayId:
            return True
    return False


getGraph()
