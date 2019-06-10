# metroCodes.py
import csv


def addMetroCodes():
    # 노선을 나타내는 문자 list
    lineNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'G', 'I', 'K', 'S']
    # 역코드와 역 외부코드가 저장되어 있는 csv파일 열기
    file = open('data/raw/서울시 역코드로 지하철역 정보 검색.csv', 'r', encoding='utf-8')
    # 역코드, 역명, 역외부코드, 호선을 저장할 list
    metroCodes = []
    lines = csv.reader(file)
    # 첫행은 제외
    i = 0
    for line in lines:
        if i != 0:
            # line[3]는 호선을 의미하는데, 해당 호선이 가공하고자 하는 대상 노선이면,
            if line[3] in lineNumbers:
                # 같은 정보의 중복 입력 방지
                if not [line[0], line[1], line[4], line[3]] in metroCodes:
                    # 역코드, 역명, 역외부코드, 호선정보를 metroCode에 추가한다
                    metroCodes.append([line[0], line[1], line[4], line[3]])
        # 첫행을 제외하면, 더이상 행을 제외하지 않는다.
        else:
            i += 1
    file.close()
    print(metroCodes)
    # 파일을 열고 처리하기 위한 list
    lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Suin', 'Bundang', 'SinBundang', 'GyeonguiJoungang', 'Airport', 'GyeongChun']
    # 각각의 노선에 대해
    for name in lineNames:
        # 원본 파일의 내용을 저장하기 위한 list
        original = []
        # 원본 파일을 열고, 읽은 후 original에 저장
        fileRead = open('data/metroId/line' + name + '.csv', 'r', encoding='euc-kr')
        lines = csv.reader(fileRead)
        for line in lines:
            original.append(line)
        fileRead.close()
        # 원본파일을 새로 쓰기 위해 다시 연다
        fileWrite = open('data/metroId/line' + name + '.csv', 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(fileWrite)
        for i in range(0, len(original)):
            # 이미 원본파일에 역정보가 쓰여져 있다면 원본내용의 해당 행을 그대로 쓴다
            if len(original[i]) != 3:
                csvWriter.writerow(original[i])
                continue
            # metroCodes에서 찾고자 하는 위치를 나타내는 idx
            idx = -1
            # metroCodes의 모든 행에 대하여
            for j in range(0, len(metroCodes)):
                # 역명이 서로 동일하다면
                if original[i][2] == metroCodes[j][1]:
                    # 각각의 노선이 일치하는지 확인한다. 환승역의 경우 역명은 동일하나 노선이 다르기 때문
                    # 1호선
                    if (original[i][0] == '1001') and (metroCodes[j][3] == '1'):
                        idx = j
                        break
                    # 2호선
                    elif (original[i][0] == '1002') and (metroCodes[j][3] == '2'):
                        idx = j
                        break
                    # 3호선
                    elif (original[i][0] == '1003') and (metroCodes[j][3] == '3'):
                        idx = j
                        break
                    # 4호선
                    elif (original[i][0] == '1004') and (metroCodes[j][3] == '4'):
                        idx = j
                        break
                    # 5호선
                    elif (original[i][0] == '1005') and (metroCodes[j][3] == '5'):
                        idx = j
                        break
                    # 6호선
                    elif (original[i][0] == '1006') and (metroCodes[j][3] == '6'):
                        idx = j
                        break
                    # 7호선
                    elif (original[i][0] == '1007') and (metroCodes[j][3] == '7'):
                        idx = j
                        break
                    # 8호선
                    elif (original[i][0] == '1008') and (metroCodes[j][3] == '8'):
                        idx = j
                        break
                    # 9호선
                    elif (original[i][0] == '1009') and (metroCodes[j][3] == '9'):
                        idx = j
                        break
                    # 경의중앙선
                    elif (original[i][0] == '1063') and (metroCodes[j][3] == 'K'):
                        idx = j
                        break
                    # 공항철도
                    elif (original[i][0] == '1065') and (metroCodes[j][3] == 'A'):
                        idx = j
                        break
                    # 경춘선
                    elif (original[i][0] == '1067') and (metroCodes[j][3] == 'G'):
                        idx = j
                        break
                    # 수인선
                    elif (original[i][0] == '1071') and (metroCodes[j][3] == 'SU'):
                        idx = j
                        break
                    # 분당선
                    elif (original[i][0] == '1075') and (metroCodes[j][3] == 'B'):
                        idx = j
                        break
                    # 신분당선
                    elif (original[i][0] == '1077') and (metroCodes[j][3] == 'S'):
                        idx = j
                        break
            # 해당하는 위치를 찾았다면, original[i]에 해당역 코드와 해당역 외부코드를 확장하고, 파일을 쓴다
            if idx != -1:
                original[i].extend([metroCodes[idx][0], metroCodes[idx][2]])
                csvWriter.writerow(original[i])
            # 해당하는 위치를 찾지 못했다면, 원본 내용을 파일에 쓴다
            else:
                csvWriter.writerow(original[i])
        fileWrite.close()


addMetroCodes()
