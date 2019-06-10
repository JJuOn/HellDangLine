# getTimesum.py
import os
import csv


def getTimeSum():
    # 수집한 데이터들의 날짜 입력
    dates = os.listdir('data/location')
    # 각각의 날짜에 대해
    for date in dates:
        # 해당 디렉토리의 파일 list
        locationFiles = os.listdir('data/location/'+date)
        # 실제 데이터가 저장된 파일에 대해
        for locationFile in locationFiles:
            # 현재 처리중인 파일 출력
            print(locationFile)
            file1 = open('data/location/'+date+'/'+locationFile, 'r')
            lines1 = csv.reader(file1)
            # 노선코드.csv에서 .csv를 제거
            subwayId = locationFile[:-4]
            # 각 행에 대해서
            for line1 in lines1:
                # 역코드
                stationId = line1[0]
                # 열차번호
                trainNo = line1[1]
                # 종착역명
                destination = line1[2]
                # 도착 시간
                arrivalTime = line1[3]
                # 요일
                weekday = line1[4]
                # 상/하행
                updown = line1[5]
                # 결과를 저장할 디렉토리가 존재하지 않으면
                if not os.path.exists('data/timesum'):
                    # 디렉토리 생성
                    os.mkdir('data/timesum')
                # 쓰고자 하는 파일이 이미 존재하면
                if os.path.exists('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown)):
                    # 원본파일 읽어서 temp에 저장
                    file2 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'r')
                    lines2 = csv.reader(file2)
                    temp = []
                    for line2 in lines2:
                        temp.append(line2)
                    file2.close()
                    # 원본파일을 write 방식으로 열기
                    file3 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file3)
                    # 원본파일에서 해당하는 내용이 있는지 알려주는 flag
                    found = False
                    # 원본파일의 각 행에 대해
                    for row in temp:
                        # 열차 번호와, 종착역명이 같다면
                        if (row[0] == trainNo) and (row[1] == destination):
                            # 찾았다고 알림
                            found = True
                            # 원본 파일의 도착시간 합에 추가하고자 하는 역의 도착시간을 더한다
                            row[2] = int(row[2]) + timeToSecond(arrivalTime)
                            # count를 1 추가해준다
                            row[3] = int(row[3]) + 1
                        # 변경된 원본파일의 해당 행을 써준다
                        csvWriter.writerow(row)
                    # 만약 찾지 못했으면
                    if not found:
                        # count를 1로 한 채 파일을 쓴다
                        csvWriter.writerow([trainNo, destination, timeToSecond(arrivalTime), 1])
                    file3.close()
                # 쓰고자하는 파일이 존재하지 않으면
                else:
                    print('doesn\'t exists')
                    # 파일을 write 방식으로 열고
                    file2 = open('data/timesum/{}_{}_{}_{}.csv'.format(subwayId, stationId, weekday, updown), 'w', encoding='euc-kr', newline='')
                    csvWriter = csv.writer(file2)
                    # count를 1로 한 채 파일을 쓴다
                    csvWriter.writerow([trainNo, destination, timeToSecond(arrivalTime), 1])
                    file2.close()


# HH:MM:SS 형식의 시간을 초로 변환해주는 함수
def timeToSecond(time):
    # 시, 분, 초로 나눈다
    timeList = time.split(':')
    # 오전 0시와 오전 1시는 전날로 취급하며, 23:59:59과 0:00:00의 차이가 크게 발생할 수 있기 때문에
    # 0시는 24시로 변경
    if timeList[0] == '0':
        timeList[0] = '24'
    # 1시는 25시로 변경
    elif timeList[0] == '1':
        timeList[0] = '25'
    # 시, 분, 초를 초로 환산하여 return
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])


getTimeSum()


