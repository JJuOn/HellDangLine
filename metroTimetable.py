# metroTimetable.py
import csv
import urllib.request
import urllib.parse
import json
import os
from env import *

baseUrl = 'http://openAPI.seoul.go.kr:8088/'+METRO_TIMETABLE_APIKEY2+'/json/SearchSTNTimeTableByIDService/1/610'
# 1: 평일, 2: 토요일, 3: 주말
WEEK_TAG = ['1', '2', '3']
# 1: 상행, 2: 하행
INOUT_TAG = ['1', '2']
# 파일을 열고 처리하기 위한 list
lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Suin', 'Bundang', 'SinBundang', 'GyeonguiJoungang', 'Airport', 'GyeongChun']


def getMetroTimetable():
    # 모든 노선에 대하여
    for lineName in lineNames:
        # 역코드를 얻기 위한 csv파일 열기
        input = open('data/metroId/line'+lineName+'.csv', 'r')
        lines = csv.reader(input)
        # 각행에 대하여
        for line in lines:
            # 역코드를 의미하는 list[3]을 stationCode에 추가한다
            stationCode = line[3]
            # api호출시 stationCode의 길이는 4자리이어야 하므로, 만약 3자리면 0을 앞에 추가해준다
            if len(stationCode) == 3:
                stationCode = '0' + stationCode
            # 모든 요일에 대해
            for week in WEEK_TAG:
                # 상행, 하행에 대해
                for inout in INOUT_TAG:
                    # api 호출
                    timetable = urllib.request.urlopen(baseUrl+'/'+stationCode+'/'+week+'/'+inout)
                    # json형태의 response를 dict로 변환한다
                    dictTimetable = json.load(timetable)
                    # 열차번호 list
                    TRAIN_NOs = []
                    # 출발역코드 list
                    ORIGINSTATIONs = []
                    # 종착역코드 list
                    DESTSTATIONs = []
                    # 도착시간 list
                    ARRIVETIMEs = []
                    # 출발시간 list
                    LEFTTIMEs = []
                    # 급행여부 list
                    EXPRESS_YNs = []
                    # api의 호출 결과 출력
                    print(dictTimetable)
                    # 오류가 발생하면, errorList.csv라는 파일에 추가한다
                    if not 'SearchSTNTimeTableByIDService' in dictTimetable:
                        output = open('data/timetable/errorList.csv', 'a', encoding='euc-kr', newline='')
                        outputWriter = csv.writer(output)
                        # error.csv에 노선 코드, 역코드, 요일, 상/하행을 쓴다
                        outputWriter.writerow([line[0], line[3], week, inout])
                        output.close()
                        continue
                    # 오류가 발생하지 않으면 각각의 행에 대하여
                    for row in dictTimetable['SearchSTNTimeTableByIDService']['row']:
                        # 해당하는 내용을 append 한다
                        TRAIN_NOs.append(row['TRAIN_NO'])
                        ORIGINSTATIONs.append(row['ORIGINSTATION'])
                        DESTSTATIONs.append(row['DESTSTATION'])
                        ARRIVETIMEs.append(row['ARRIVETIME'])
                        LEFTTIMEs.append(row['LEFTTIME'])
                        EXPRESS_YNs.append(row['EXPRESS_YN'])
                    # 노선코드_역코드_요일_상/하행.csv 파일을 쓴다.
                    output = open('data/timetable/' + line[0] + '_' + line[3] + '_' + week + '_' + inout + '.csv', 'w', encoding='euc-kr', newline='')
                    outputWriter = csv.writer(output)
                    outputWriter.writerow(['TRAIN_NO', 'ORIGINSTATION', 'DESTSTATION', 'ARRIVETIME', 'LEFTTIME', 'EXPRESS_YN'])
                    for i in range(0, len(TRAIN_NOs)):
                        outputWriter.writerow([TRAIN_NOs[i], ORIGINSTATIONs[i], DESTSTATIONs[i], ARRIVETIMEs[i], LEFTTIMEs[i], EXPRESS_YNs[i]])
                    output.close()
        input.close()


# getMetroTimetable()에서 실패한 내용을 다시 호출
def getTimeTableFromErrorList():
    # errorList.csv 파일 열기
    errorFileInput = open('data/timetable/errorList.csv', 'r')
    lines = csv.reader(errorFileInput)
    # 원본파일의 내용
    errorList = []
    for line in lines:
        errorList.append(line)
    errorFileInput.close()
    # 기존파일 삭제
    os.remove('data/timetable/errorList.csv')
    # 각각의 행에 대하여
    for errorRow in errorList:
        # 요일
        weekday = errorRow[2]
        # 상하행
        updown = errorRow[3]
        # api호출시 stationCode의 길이는 4자리이어야 하므로, 만약 3자리면 0을 앞에 추가해준다
        if len(errorRow[1]) == 3:
            stationCode = '0'+errorRow[1]
        else:
            stationCode = errorRow[1]
        # api 호출
        timetable = urllib.request.urlopen(baseUrl+'/'+stationCode+'/'+weekday+'/'+updown)
        # json형태의 response를 dict로 변환한다
        dictTimetable = json.load(timetable)
        # 열차번호 list
        TRAIN_NOs = []
        # 출발역코드 list
        ORIGINSTATIONs = []
        # 종착역코드 list
        DESTSTATIONs = []
        # 도착시간 list
        ARRIVETIMEs = []
        # 출발시간 list
        LEFTTIMEs = []
        # 급행여부 list
        EXPRESS_YNs = []
        # api 호출 결과 출력
        print(dictTimetable)
        # 오류가 발생하면
        if not 'SearchSTNTimeTableByIDService' in dictTimetable:
            # 만약 errorList.csv가 존재하지 않으면
            if not os.path.exists('data/timetable/errorList.csv'):
                # errorList.csv 생성
                temp = open('data/timetable/errorList.csv', 'w', encoding='euc-kr', newline='')
                temp.close()
            # append 로 errorList.csv를 연다
            output = open('data/timetable/errorList.csv', 'a', encoding='euc-kr', newline='')
            outputWriter = csv.writer(output)
            # 오류가 발생한 역의 정보를 쓴다
            print('error : {}'.format([errorRow[0], errorRow[1], weekday, updown]))
            outputWriter.writerow([errorRow[0], errorRow[1], weekday, updown])
            output.close()
            continue
        # 각각의 api 호출 결과에 대해서
        for row in dictTimetable['SearchSTNTimeTableByIDService']['row']:
            # 해당하는 내용을 append
            TRAIN_NOs.append(row['TRAIN_NO'])
            ORIGINSTATIONs.append(row['ORIGINSTATION'])
            DESTSTATIONs.append(row['DESTSTATION'])
            ARRIVETIMEs.append(row['ARRIVETIME'])
            LEFTTIMEs.append(row['LEFTTIME'])
            EXPRESS_YNs.append(row['EXPRESS_YN'])
        # 노선코드_역코드_요일_상/하행.csv 파일을 쓴다.
        output = open('data/timetable/' + errorRow[0] + '_' + errorRow[1] + '_' + weekday + '_' + updown + '.csv', 'w', encoding='euc-kr', newline='')
        outputWriter = csv.writer(output)
        outputWriter.writerow(['TRAIN_NO', 'ORIGINSTATION', 'DESTSTATION', 'ARRIVETIME', 'LEFTTIME', 'EXPRESS_YN'])
        for i in range(0, len(TRAIN_NOs)):
            outputWriter.writerow([TRAIN_NOs[i], ORIGINSTATIONs[i], DESTSTATIONs[i], ARRIVETIMEs[i], LEFTTIMEs[i], EXPRESS_YNs[i]])
        output.close()


getMetroTimetable()
getTimeTableFromErrorList()
