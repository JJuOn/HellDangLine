# editSeongsu.py
import os
import csv


def removeDuplicatedTrainNo():
    # 지하철 시간표가 저장되어 있는 디렉토리의 파일 리스트 저장
    fileList = os.listdir('data/timetable')
    # 각각의 시간표 파일에 대해
    for fileName in fileList:
        # 2호선 성수역이라면
        if '1002_211' in fileName:
            # 2호선 성수역의 시간표파일 열기
            input = open('data/timetable/'+fileName, 'r')
            lines = csv.reader(input)
            # 결과를 저장할 list
            result = []
            # 각각의 행에 대하여
            for line in lines:
                # 기점역과 종착역이 같을 때
                if line[1] == line[2]:
                    # 도착시간이 0이라면 즉, 기점인 경우라면
                    if timeToSecond(line[3]) == 0:
                        # result에 append
                        result.append(line)
                # 기점역과 종착역이 같지 않다면
                else:
                    # result에 append
                    result.append(line)
            input.close()
            # result의 내용을 다시 덮어 쓴다
            output = open('data/timetable/'+fileName, 'w', encoding='euc-kr', newline='')
            csvWriter = csv.writer(output)
            for row in result:
                csvWriter.writerow(row)
            output.close()


# HH:MM:SS의 시간형식을 초로 변환해주는 함수
def timeToSecond(time):
    # 시, 분, 초로 나눈다
    timeList = time.split(':')
    # 초로 계산한 값 return
    return int(timeList[0])*3600+int(timeList[1])*60+int(timeList[2])


removeDuplicatedTrainNo()
