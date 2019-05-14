import csv


def addMetroCodes():
    lineNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'G', 'I', 'K', 'S']
    file = open('data/raw/서울시 역코드로 지하철역 정보 검색.csv', 'r', encoding='utf-8')
    metroCodes = []
    lines = csv.reader(file)
    i = 0
    for line in lines:
        if i != 0:
            if line[3] in lineNumbers:
                if not [line[0], line[1], line[4], line[3]] in metroCodes:
                    metroCodes.append([line[0], line[1], line[4], line[3]])
        else:
            i += 1
    file.close()

    print(metroCodes)
    lineNames = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'Suin', 'Bundang', 'SinBundang', 'GyeonguiJoungang', 'Airport', 'GyeongChun']
    for name in lineNames:
        original = []
        fileRead = open('data/metroId/line' + name + '.csv', 'r', encoding='euc-kr')
        lines = csv.reader(fileRead)
        for line in lines:
            original.append(line)
        fileRead.close()
        fileWrite = open('data/metroId/line' + name + '.csv', 'w', encoding='euc-kr', newline='')
        csvWriter = csv.writer(fileWrite)
        for i in range(0, len(original)):
            if len(original[i]) != 3:
                csvWriter.writerow(original[i])
                continue
            idx = -1
            for j in range(0, len(metroCodes)):
                if original[i][2] == metroCodes[j][1]:
                    if (original[i][0] == '1001') and (metroCodes[j][3] == '1'):
                        idx = j
                        break
                    elif (original[i][0] == '1002') and (metroCodes[j][3] == '2'):
                        idx = j
                        break
                    elif (original[i][0] == '1003') and (metroCodes[j][3] == '3'):
                        idx = j
                        break
                    elif (original[i][0] == '1004') and (metroCodes[j][3] == '4'):
                        idx = j
                        break
                    elif (original[i][0] == '1005') and (metroCodes[j][3] == '5'):
                        idx = j
                        break
                    elif (original[i][0] == '1006') and (metroCodes[j][3] == '6'):
                        idx = j
                        break
                    elif (original[i][0] == '1007') and (metroCodes[j][3] == '7'):
                        idx = j
                        break
                    elif (original[i][0] == '1008') and (metroCodes[j][3] == '8'):
                        idx = j
                        break
                    elif (original[i][0] == '1009') and (metroCodes[j][3] == '9'):
                        idx = j
                        break
                    elif (original[i][0] == '1063') and (metroCodes[j][3] == 'K'):
                        idx = j
                        break
                    elif (original[i][0] == '1065') and (metroCodes[j][3] == 'A'):
                        idx = j
                        break
                    elif (original[i][0] == '1067') and (metroCodes[j][3] == 'G'):
                        idx = j
                        break
                    elif (original[i][0] == '1071') and (metroCodes[j][3] == 'SU'):
                        idx = j
                        break
                    elif (original[i][0] == '1075') and (metroCodes[j][3] == 'B'):
                        idx = j
                        break
                    elif (original[i][0] == '1077') and (metroCodes[j][3] == 'S'):
                        idx = j
                        break
            if idx != -1:
                original[i].extend([metroCodes[idx][0], metroCodes[idx][2]])
                csvWriter.writerow(original[i])
            else:
                csvWriter.writerow(original[i])
        fileWrite.close()


addMetroCodes()