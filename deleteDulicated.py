# deleteDuplicated.py
import os
import csv


def deleteDuplicated():
    # 데이터가 중복된 날짜
    targetDate = '20190610'
    # 해당 날짜에 해당하는 디렉토리의 파일 list
    fileNameList = os.listdir('data/location/{}'.format(targetDate))
    # 각각의 파일에 대해
    for fileName in fileNameList:
        # 현재 처리중인 파일 출력
        print(fileName)
        # 원본파일 open
        original = open('data/location/{}/{}'.format(targetDate, fileName), 'r')
        lines = csv.reader(original)
        temp = []
        # 각각의 행에 대해
        for line in lines:
            # 중복되지 않은 행만
            if not line in temp:
                # temp에 append
                temp.append(line)
        original.close()
        # 원본파일을 write 방식으로 연다
        output = open('data/location/{}/{}'.format(targetDate, fileName), 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(output)
        # temp의 내용을 쓴다
        for row in temp:
            csvWriter.writerow(row)
        output.close()


deleteDuplicated()
