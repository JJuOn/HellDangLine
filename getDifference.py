# getDifference.py
import csv
import os

# 노선 코드와 노선 명은 1:1로 매칭됨
# 노선 코드
subwayIds = ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1063', '1065', '1067', '1071', '1075']
# 노선 명
lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'GyeonguiJoungang', 'Airport', 'GyeongChun', 'Suin', 'Bundang']
# 열차번호에 들어있을 수 있는 알파벳
trainNoStr = ['K', 'S', 'C', 'A']


def getDifference():
    # subwayIds와 lineNames의 각 element에 대해
    for i in range(0, 14):
        idList = []
        # 해당 노선의 정보가 저장되어 있는 file open
        idFile = open('data/metroId/line'+lineNames[i]+'.csv', 'r')
        lines1 = csv.reader(idFile)
        # idFile의 각 행을 idList에 저장
        for line in lines1:
            idList.append(line)
        idFile.close()
        # 노선의 각 역에 대해
        for station in idList:
            # 각 요일에 대해
            for weekday in range(1, 4):
                # 상/하행에 대해
                for updown in range(1, 3):
                    # 현재 처리중인 파일 입력
                    print('{}_{}_{}_{}.csv'.format(subwayIds[i], station[3], weekday, updown))
                    # 도착시간의 평균값이 저장될 list
                    timeAverageList = []
                    # 도착시간의 평균값이 존재하지 않으면 스킵
                    if not os.path.exists('data/timeaverage/{}_{}_{}_{}.csv'.format(subwayIds[i], station[1], weekday, updown)):
                        continue
                    # 도착시간의 평균값이 저장되어 있는 파일 open
                    timeAverageFile = open('data/timeaverage/{}_{}_{}_{}.csv'.format(subwayIds[i], station[1], weekday, updown), 'r')
                    lines2 = csv.reader(timeAverageFile)
                    # 도착시간의 평균값 저장
                    for line in lines2:
                        timeAverageList.append(line)
                    timeAverageFile.close()
                    # 시간표 정보가 저장될 list
                    timetableList = []
                    # 시간표 파일이 존재하지 않으면 스킵
                    if not os.path.exists('data/timetable/{}_{}_{}_{}.csv'.format(subwayIds[i], station[3], weekday, updown)):
                        continue
                    # 시간표 파일 open
                    timetableFile = open('data/timetable/{}_{}_{}_{}.csv'.format(subwayIds[i], station[3], weekday, updown), 'r')
                    lines3 = csv.reader(timetableFile)
                    # 시간표 파일의 내용 저장
                    for line in lines3:
                        timetableList.append(line)
                    timetableFile.close()
                    # 첫행은 제거
                    del timetableList[0]
                    result = []
                    # 시간표상의 각 행에 대해
                    for timetableRow in timetableList:
                        # 알파벳을 제거한 열차번호
                        trainNoInTimetable = delAlphabetInTrainNo(timetableRow[0])
                        # 시간표상의 도착시간
                        arrivaltimeInTimetable = timeToSecond(timetableRow[3])
                        # 시간표상의 출발시간
                        lefttimeInTimetable = timeToSecond(timetableRow[4])
                        # 평균 도착시간의 각 행에 대해
                        for timeAverageRow in timeAverageList:
                            # 열차번호가 같고,
                            if delAlphabetInTrainNo(timeAverageRow[0]) == trainNoInTimetable:
                                # 기점이 아니면
                                if arrivaltimeInTimetable != 0:
                                    # 도착시간 차이 계산
                                    difference = abs(arrivaltimeInTimetable - int(timeAverageRow[2]))
                                    # result에 append
                                    result.append([station[2], timeAverageRow[1], difference, secondToTime(arrivaltimeInTimetable), secondToTime(timeAverageRow[2])])
                    # data/result 디렉토리가 없다면, 해당 디렉토리 생성
                    if not os.path.exists('data/result'):
                        os.mkdir('data/result')
                    # 결과 파일 write 방식으로 open
                    resultFile = open('data/result/{}_{}_{}_{}.csv'.format(subwayIds[i], station[2], weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(resultFile)
                    # 결과 파일 쓰기
                    for row in result:
                        csvWriter.writerow(row)
                    resultFile.close()


# 초 형식의 시간을 HH:MM:SS로 변환
def secondToTime(timesum):
    hour = int(timesum)//3600
    minute = (int(timesum)-hour*3600)//60
    second = int(timesum) % 60
    timestring = "{}:{}:{}".format(hour, minute, second)
    return timestring

# HH:MM:SS 형식의 시간을 초 형식으로 변환
def timeToSecond(time):
    timeList = time.split(':')
    if timeList[0] == '0':
        timeList[0] = '24'
    elif timeList[0] == '1':
        timeList[0] = '25'
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])


# 열차 번호에서 알파벳 삭제
def delAlphabetInTrainNo(string):
    for i in range(0, len(trainNoStr)):
        if trainNoStr[i] in string:
            return string.replace(trainNoStr[i], '')
    return string


getDifference()
