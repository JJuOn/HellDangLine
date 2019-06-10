# getTimeaverage.py
import csv
import os


def getTimeaverage():
    # data/timesum 디렉토리의 파일 list
    targetFileList = os.listdir('data/timesum')
    # 각각의 파일에 대해
    for targetFile in targetFileList:
        # 처리중인 파일 출력
        print(targetFile)
        inputFile = open('data/timesum/'+targetFile, 'r')
        lines = csv.reader(inputFile)
        temp = []
        # 원본 파일의 각 행에 대해
        for line in lines:
            # 각 행의 도착시간 합을 count로 나눈 후 temp에 append
            temp.append([line[0], line[1], int(line[2])//int(line[3])])
        inputFile.close()
        # data/timeaverage 디렉토리가 존재하지 않으면, 해당 디렉토리 생성
        if not os.path.exists('data/timeaverage'):
            os.mkdir('data/timeaverage')
        # 도착시간의 평균값을 저장할 파일
        outputFile = open('data/timeaverage/'+targetFile, 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(outputFile)
        # temp의 각 행 쓰기
        for row in temp:
            csvWriter.writerow(row)
        outputFile.close()


getTimeaverage()
