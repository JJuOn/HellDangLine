import requests
import requests.exceptions
import csv
import datetime
import os
from time import sleep

def getMetroArrival():
    lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Suin', 'Bundang', 'SinBundang', 'GyeonguiJoungang', 'Airport', 'GyeongChun']
    idTable = []
    for lineName in lineNames:
        stationIds = []
        file = open('data/metroId/line' + lineName + '.csv', 'r',encoding='euc-kr')
        csvReader = csv.reader(file)
        for line in csvReader:
            subwayNum = line[0]
            stationIds.append({'stationId': line[1]})
        idTable.append({'subwayNum': subwayNum, 'stationIds': stationIds})
        file.close()
    while True:
        if datetime.datetime.now().hour < 2 or datetime.datetime.now().hour >= 4:
            url = 'http://m.bus.go.kr/mBus/subway/getStatnTrainInfo.bms?'
            for row in idTable:
                subwayNum = row['subwayNum']
                for stationIds in row['stationIds']:
                    stationId = stationIds['stationId']
                    now = datetime.datetime.now()
                    date = now.strftime("%Y%m%d")
                    time = now.strftime("%H%M%S")
                    weekday = now.weekday()
                    if now.hour >= 0 or now.hour <= 2:
                        weekday = weekday - 1
                    if weekday >= 0 or weekday <= 4:
                        weekday = 1
                    elif weekday == 5:
                        weekday = 2
                    else:
                        weekday = 3
                    try:
                        response = requests.post(url + 'subwayId={}&statnId={}'.format(subwayNum, stationId))
                    except requests.exceptions.ConnectionError:
                        print('Timeout Error!')
                    result = response.json()
                    if result['resultList'] is None:
                        continue
                    if not os.path.exists('data/location/'+date):
                        os.mkdir('data/location/'+date)
                    if os.path.exists('data/location/'+date+'/'+subwayNum+'.csv'):
                        file = open('data/location/' + date + '/' + subwayNum + '.csv', 'a', encoding='euc-kr', newline='')
                    else:
                        file = open('data/location/'+date+'/'+subwayNum+'.csv', 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file)
                    for resultRow in result['resultList']:
                        updownCode = ''
                        if resultRow['trainSttus'] != '1':
                            continue
                        if resultRow['updnLine'] == '상행' or resultRow['updnLine'] == '내선':
                            updownCode = '1'
                        else:
                            updownCode = '2'
                        arrivedTime = resultRow['arvlDt'][11:19]
                        trainNo = resultRow['trainNo']
                        destination = resultRow['trainLineNm']
                        csvWriter.writerow([stationId, trainNo, destination, arrivedTime, weekday, updownCode])
                        print(resultRow)
                    file.close()
                    sleep(0.1)


getMetroArrival()


