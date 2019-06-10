# metroArrival.py
import requests
import requests.exceptions
import csv
import datetime
import os
from time import sleep


def getMetroArrival():
    # 노선의 이름이 저장되어있는 list
    lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Suin', 'Bundang', 'GyeonguiJoungang', 'Airport', 'GyeongChun']
    # 노선 코드와 역 ID가 저장될 list
    idTable = []
    # 각각의 노선에 대하여
    for lineName in lineNames:
        # 각 노선의 역 ID 들을 저장할 list
        stationIds = []
        # 노선 코드, 역 ID 정보 등이 저장되어있는 파일 open
        file = open('data/metroId/line' + lineName + '.csv', 'r', encoding='euc-kr')
        csvReader = csv.reader(file)
        # 각 행에 대해
        for line in csvReader:
            # 노선 코드 지정
            subwayNum = line[0]
            # stationIds에 역 ID 추가
            stationIds.append({'stationId': line[1]})
        # idTable에 해당 노선 정보 추가
        idTable.append({'subwayNum': subwayNum, 'stationIds': stationIds})
        file.close()
    # 무한 루프
    while True:
        # 2시 이후와 4시 이전에는 작동하지 않음
        if datetime.datetime.now().hour < 2 or datetime.datetime.now().hour >= 4:
            # 호출할 api의 주소
            url = 'http://m.bus.go.kr/mBus/subway/getStatnTrainInfo.bms?'
            # 각각의 노선에 대해
            for row in idTable:
                # 노선 코드
                subwayNum = row['subwayNum']
                # 해당 노선이 각 역에 대해
                for stationIds in row['stationIds']:
                    # 역 ID
                    stationId = stationIds['stationId']
                    # 현재 시간
                    now = datetime.datetime.now()
                    # 20190610의 형식으로 변환
                    date = now.strftime("%Y%m%d")
                    # 현재 요일 지정(0: 월요일 ~ 6:일요일)
                    weekday = now.weekday()
                    # 오전 0시부터 2시까지는 전날의 요일을 따라가므로, 전날로 취급
                    if now.hour >= 0 and now.hour <= 2:
                        weekday = weekday - 1
                    # 월요일에서 전날로 넘어가 -1이 된다면, 일요일로 취급
                    if weekday == -1:
                        weekday = 6
                    # 평일이면
                    if weekday >= 0 and weekday <= 4:
                        # weekday를 1로 지정
                        weekday = 1
                    # 토요일이면
                    elif weekday == 5:
                        # weekday를 2로 지정
                        weekday = 2
                    # 일요일이면
                    else:
                        # weekday을 3으로 지정
                        weekday = 3
                    try:
                        # api를 POST method로 request
                        response = requests.post(url + 'subwayId={}&statnId={}'.format(subwayNum, stationId))
                    # 서버와의 통신에러가 뜰때, exception handling
                    except requests.exceptions.ConnectionError:
                        # 에러가 떴다고 출력
                        print('Timeout Error!')
                    # json type의 response를 저장
                    result = response.json()
                    # 해당역에 열차가 정차하지 않았다면 스킵
                    if result['resultList'] is None:
                        continue
                    # 수집한 데이터를 저장할 디렉토리가 존재하지 않는다면
                    if not os.path.exists('data/location/'+date):
                        # 디렉토리 생성
                        os.mkdir('data/location/'+date)
                    # 수집한 노선에 대한 파일이 존재한다면
                    if os.path.exists('data/location/'+date+'/'+subwayNum+'.csv'):
                        # append 방식으로 open
                        file = open('data/location/' + date + '/' + subwayNum + '.csv', 'a', encoding='euc-kr', newline='')
                    # 파일이 존재하지 않는다면
                    else:
                        # write 방식으로 open
                        file = open('data/location/'+date+'/'+subwayNum+'.csv', 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file)
                    # 결과의 각 행에 대하여
                    for resultRow in result['resultList']:
                        # 상/하행 여부
                        updownCode = ''
                        # 열차가 역에 도착하지 않았다면 스킵.
                        if resultRow['trainSttus'] != '1':
                            continue
                        # 실제 시간표의 상/하행 기준과 api의 상/하행 기준이 다른 노선이 존재하기에,
                        # 상/하행 기준이 다른 노선이라면
                        if subwayNum in ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1063', '1067', '1071', '1075']:
                            if resultRow['updnLine'] == '하행' or resultRow['updnLine'] == '내선':
                                updownCode = '1'
                            else:
                                updownCode = '2'
                        # 상/하행 기준이 같은 노선이라면
                        else:
                            if resultRow['updnLine'] == '상행' or resultRow['updnLine'] == '내선':
                                updownCode = '1'
                            else:
                                updownCode = '2'
                        # 시,분초,단위 까지만 arrivedTime에 저장한다.
                        arrivedTime = resultRow['arvlDt'][11:19]
                        # 열차 번호
                        trainNo = resultRow['trainNo']
                        # 종착역명
                        destination = resultRow['trainLineNm']
                        # 파일에 쓰기
                        csvWriter.writerow([stationId, trainNo, destination, arrivedTime, weekday, updownCode])
                        print(resultRow)
                    file.close()
                    # 과부하 방지와 과도한 중복데이터 입력 방지를 위해 각 역별로 0.1초간 sleep
                    sleep(0.1)


getMetroArrival()


