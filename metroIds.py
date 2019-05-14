import csv

def getMetroIds():
    file = open('../실시간도착_역정보.csv', 'r', encoding='utf-8')
    metros = []
    lines = csv.reader(file)
    line1 = open('data/line1.csv', 'w', encoding='euc-kr', newline='')
    line2 = open('data/line2.csv', 'w', encoding='euc-kr', newline='')
    line3 = open('data/line3.csv', 'w', encoding='euc-kr', newline='')
    line4 = open('data/line4.csv', 'w', encoding='euc-kr', newline='')
    line5 = open('data/line5.csv', 'w', encoding='euc-kr', newline='')
    line6 = open('data/line6.csv', 'w', encoding='euc-kr', newline='')
    line7 = open('data/line7.csv', 'w', encoding='euc-kr', newline='')
    line8 = open('data/line8.csv', 'w', encoding='euc-kr', newline='')
    line9 = open('data/line9.csv', 'w', encoding='euc-kr', newline='')
    lineInc1 = open('data/lineInc1.csv', 'w', encoding='euc-kr', newline='')
    #lineInc2 = open('data/lineInc2.csv', 'w', encoding='euc-kr', newline='')
    lineBundang = open('data/lineBundang.csv', 'w', encoding='euc-kr', newline='')
    lineSinBundang = open('data/lineSinBundang.csv', 'w', encoding='euc-kr', newline='')
    lineGyeonguiJoungang = open('data/lineGyeonGuiJoungang.csv', 'w', encoding='euc-kr', newline='')
    lineAirport = open('data/lineAirport.csv', 'w', encoding='euc-kr', newline='')
    lineGyeongChun = open('data/lineGyeongChun.csv', 'w', encoding='euc-kr', newline='')
    #lineSuin = open('data/lineSuin.csv', 'w', encoding='euc-kr', newline='')
    #lineUijeongbu = open('data/lineUijeongbu.csv', 'w', encoding='euc-kr', newline='')
    #lineEver = open('data/lineEver.csv', 'w', encoding='euc-kr', newline='')
    #lineGyeonggang = open('data/lineGyeonggang.csv', 'w', encoding='euc-kr', newline='')
    #lineWooeSinseul = open('data/lineWooeSinseul.csv', 'w', encoding='euc-kr', newline='')
    #lineSeohae = open('data/lineSeohae.csv', 'w', encoding='euc-kr', newline='')
    i = 0
    for line in lines:
        if i != 0:
            if line[0] == '1001':
                writeLine1 = csv.writer(line1)
                writeLine1.writerow(line)
            elif line[0] == '1002':
                writeLine2 = csv.writer(line2)
                writeLine2.writerow(line)
            elif line[0] == '1003':
                writeLine3 = csv.writer(line3)
                writeLine3.writerow(line)
            elif line[0] == '1004':
                writeLine4 = csv.writer(line4)
                writeLine4.writerow(line)
            elif line[0] == '1005':
                writeLine5 = csv.writer(line5)
                writeLine5.writerow(line)
            elif line[0] == '1006':
                writeLine6 = csv.writer(line6)
                writeLine6.writerow(line)
            elif line[0] == '1007':
                writeLine7 = csv.writer(line7)
                writeLine7.writerow(line)
            elif line[0] == '1008':
                writeLine8 = csv.writer(line8)
                writeLine8.writerow(line)
            elif line[0] == '1009':
                writeLine9 = csv.writer(line9)
                writeLine9.writerow(line)
            elif line[0] == '1063':
                writeLineGyeonguiJoungang = csv.writer(lineGyeonguiJoungang)
                writeLineGyeonguiJoungang.writerow(line)
            elif line[0] == '1065':
                writeLineAirport = csv.writer(lineAirport)
                writeLineAirport.writerow(line)
            elif line[0] == '1067':
                writeLineGyeongChun = csv.writer(lineGyeongChun)
                writeLineGyeongChun.writerow(line)
            elif line[0] == '1071':
                writeLineInc1 = csv.writer(lineInc1)
                writeLineInc1.writerow(line)
            elif line[0] == '1075':
                writeLineBundang = csv.writer(lineBundang)
                writeLineBundang.writerow(line)
            elif line[0] == '1077':
                writeLineSinBundang = csv.writer(lineSinBundang)
                writeLineSinBundang.writerow(line)


        i += 1
    file.close()
    line1.close()
    line2.close()
    line3.close()
    line4.close()
    line5.close()
    line6.close()
    line7.close()
    line8.close()
    line9.close()
    lineInc1.close()
    #lineInc2.close()
    lineBundang.close()
    lineSinBundang.close()
    lineGyeonguiJoungang.close()
    lineAirport.close()
    lineGyeongChun.close()
    #lineSuin.close()
    #lineUijeongbu.close()
    #lineEver.close()
    #lineGyeonggang.close()
    #lineWooeSinseul.close()
    #lineSeohae.close()

getMetroIds()
