import csv
import urllib.request
import urllib.parse
import xml.dom.minidom
import xml.etree.ElementTree as etree
import json
from time import sleep
from env import *

baseUrl = 'http://openAPI.seoul.go.kr:8088/'+METRO_TIMETABLE_APIKEY2+'/json/SearchSTNTimeTableByIDService/1/610'
# 1: 평일, 2: 토요일, 3: 주말
WEEK_TAG = ['1', '2', '3']
# 1: 상행, 2: 하행
INOUT_TAG = ['1', '2']
lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Suin', 'Bundang', 'SinBundang', 'GyeonguiJoungang', 'Airport', 'GyeongChun']


def getMetroTimetable(lineName):
    input = open('data/metroId/line'+lineName+'.csv', 'r')
    lines = csv.reader(input)
    for line in lines:
        stationCode = line[3]
        if len(stationCode) == 3:
            stationCode = '0' + stationCode
        for week in WEEK_TAG:
            for inout in INOUT_TAG:
                timetable = urllib.request.urlopen(baseUrl+'/'+stationCode+'/'+week+'/'+inout)
                dictTimetable = json.load(timetable)
                TRAIN_NOs = []
                ORIGINSTATIONs = []
                DESTSTATIONs = []
                ARRIVETIMEs = []
                LEFTTIMEs = []
                EXPRESS_YNs = []
                print(dictTimetable)
                if not 'SearchSTNTimeTableByIDService' in dictTimetable:
                    output = open('data/timetable/errorList.csv', 'a', encoding='euc-kr', newline='')
                    outputWriter = csv.writer(output)
                    outputWriter.writerow([line[0], line[3], week, inout])
                    output.close()
                    continue
                for row in dictTimetable['SearchSTNTimeTableByIDService']['row']:
                    TRAIN_NOs.append(row['TRAIN_NO'])
                    ORIGINSTATIONs.append(row['ORIGINSTATION'])
                    DESTSTATIONs.append(row['DESTSTATION'])
                    ARRIVETIMEs.append(row['ARRIVETIME'])
                    LEFTTIMEs.append(row['LEFTTIME'])
                    EXPRESS_YNs.append(row['EXPRESS_YN'])
                output = open('data/timetable/' + line[0] + '_' + line[3] + '_' + week + '_' + inout + '.csv', 'w', encoding='euc-kr', newline='')
                outputWriter = csv.writer(output)
                outputWriter.writerow(['TRAIN_NO', 'ORIGINSTATION', 'DESTSTATION', 'ARRIVETIME', 'LEFTTIME', 'EXPRESS_YN'])
                for i in range(0, len(TRAIN_NOs)):
                    outputWriter.writerow([TRAIN_NOs[i], ORIGINSTATIONs[i], DESTSTATIONs[i], ARRIVETIMEs[i], LEFTTIMEs[i], EXPRESS_YNs[i]])
                output.close()
    input.close()


for lineName in lineNames:
    getMetroTimetable(lineName)

