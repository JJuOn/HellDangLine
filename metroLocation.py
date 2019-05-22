import urllib.request
import urllib.parse
import json
import csv
import datetime
from time import sleep
from env import *


def getMetroLocation():
    lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Suin', 'Bundang', 'SinBundang', 'GyeonguiJoungang', 'Airport', 'GyeongChun']
    while True:
        if datetime.datetime.now().hour < 2 or datetime.datetime.now().hour >= 4:
            for lineName in lineNames:
                subwayName = ''
                subwayId = ''
                if lineName == '1':
                    subwayName = '1호선'
                    subwayId = '1001'
                elif lineName == '2':
                    subwayName = '2호선'
                    subwayId = '1002'
                elif lineName == '3':
                    subwayName = '3호선'
                    subwayId = '1003'
                elif lineName == '4':
                    subwayName = '4호선'
                    subwayId = '1004'
                elif lineName == '5':
                    subwayName = '5호선'
                    subwayId = '1005'
                elif lineName == '6':
                    subwayName = '6호선'
                    subwayId = '1006'
                elif lineName == '7':
                    subwayName = '7호선'
                    subwayId = '1007'
                elif lineName == '8':
                    subwayName = '8호선'
                    subwayId = '1008'
                elif lineName == '9':
                    subwayName = '9호선'
                    subwayId = '1009'
                elif lineName == 'Suin':
                    subwayName = '수인선'
                    subwayId = '1071'
                elif lineName == 'Bundang':
                    subwayName = '분당선'
                    subwayId = '1075'
                elif lineName == 'SinBundang':
                    subwayName = '신분당선'
                    subwayId = '1077'
                elif lineName == 'GyeonguiJoungang':
                    subwayName = '경의중앙선'
                    subwayId = '1063'
                elif lineName == 'Airport':
                    subwayName = '공항철도'
                    subwayId = '1065'
                elif lineName == 'GyeongChun':
                    subwayName = '경춘선'
                    subwayId = '1067'
                subwayNameQuoted = urllib.parse.quote_plus(subwayName)
                url = "http://swopenapi.seoul.go.kr/api/subway/" + METRO_LOCATION_APIKEY + "/json/realtimePosition/0/100/" + subwayNameQuoted
                now = datetime.datetime.now()
                dateToString = now.strftime("%Y%m%d_%H%M%S")
                weekday = now.weekday()
                if now.hour >= 0 or now.hour <= 2:
                    weekday = weekday-1
                if weekday >= 0 or weekday <= 4:
                    weekday = 1
                elif weekday == 5:
                    weekday = 2
                else:
                    weekday = 3
                response = urllib.request.urlopen(url)
                dictResult = json.load(response)
                if not 'realtimePositionList' in dictResult:
                    continue
                statnIds = []
                statnTids = []
                trainNos = []
                updnLines = []
                recptnDts = []
                for row in dictResult['realtimePositionList']:
                    if row['trainSttus'] != '1':
                        continue
                    statnIds.append(row['statnId'])
                    statnTids.append(row['statnTid'])
                    trainNos.append(row['trainNo'])
                    updnLines.append(int(row['updnLine'])+1)
                    recptnDts.append(row['recptnDt'][11:])
                file = open('data/location/' + dateToString + '_' + subwayId + '.csv', 'w', encoding='euc-kr', newline='')
                csvWriter = csv.writer(file)
                csvWriter.writerow(['STATNID', 'TRAIN_NO', 'STATNTID', 'RECPTNDT', 'WEEKDAY', 'UPDNLINE'])
                for i in range(0, len(statnIds)):
                    csvWriter.writerow([statnIds[i], trainNos[i], statnTids[i], recptnDts[i], weekday, updnLines[i]])
                    print([statnIds[i], trainNos[i], statnTids[i], recptnDts[i], weekday, updnLines[i]])
                file.close()
            sleep(10)


getMetroLocation()

