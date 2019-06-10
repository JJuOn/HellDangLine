# getGraph.py
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import csv
import os


def getGraph():
    # 한글폰트 지정
    font_name = fm.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
    mpl.rc('font', family=font_name)
    mpl.rcParams.update({'figure.autolayout': True})
    subwayDifference = []
    # data/result의 파일 list
    fileNameList = os.listdir('data/result')
    # 각각의 파일에 대해
    for fileName in fileNameList:
        # _로 구분
        split = fileName.split('_')
        # 노선 코드
        subwayId = split[0]
        # 역명
        stationName = split[1]
        # 요일
        weekday = split[2]
        # 결과파일 open
        inputFile = open('data/result/'+fileName, 'r')
        lines = csv.reader(inputFile)
        # count 초기값 0
        count = 0
        # 시간차이의 합 초기값 0
        sum = 0
        # 각 노선에 대해서
        for line in lines:
            # 열차별 시간차이의 합 계산
            sum += int(line[2])
            # count 추가
            count += 1
        # 처리된적이 있는 노선인가
        found = False
        # 해당 노선이 계산되지 않았으면
        if not isSubwayIdExists(subwayDifference, subwayId):
            # 해당 노선 추가
            subwayDifference.append({'subwayId': subwayId, 'stations': []})
        # 각 노선에 대해
        for row in subwayDifference:
            # 처리하고자 하는 노선이라면
            if row['subwayId'] == subwayId:
                # 각각의 역에 대해서
                for station in row['stations']:
                    # 역 이름과, 요일이 같다면
                    if station['stationName'] == stationName and station['weekday'] == weekday:
                        # 찾았음
                        found = True
                        # 역별 시간차 합 추가
                        station['difference'] += sum
                        # count 추가
                        station['count'] += count
        # 처리된적이 없는 노선이라면
        if not found:
            # 각 노선에 대해
            for row in subwayDifference:
                # 노선이 같으면
                if row['subwayId'] == subwayId:
                    # 'station'에 append
                    row['stations'].append({'stationName': stationName, 'weekday': weekday, 'difference': sum, 'count': count})
    # 결과 그래프를 저장할 data/img가 존재하지 않는다면 디렉토리 생성
    if not os.path.exists('data/img'):
        os.mkdir('data/img')
    # 각각의 요일에 대해
    for wd in ['1', '2', '3']:
        # 전체 노선의 x축 y축
        x1 = []
        y1 = []
        # 각각에 노선에 대해
        for row in subwayDifference:
            # 각 노선의 x축 y축
            x2 = []
            y2 = []
            subwaySum = 0
            subwayCount = 0
            # 각각의 역 평균 계산
            for station in row['stations']:
                subwaySum += station['difference']
                subwayCount += station['count']
            subwayAverage = subwaySum // subwayCount
            row['subwayDifference'] = subwayAverage
            row['subwayCount'] = subwayCount
            for station in row['stations']:
                # 요일과, count가 0이 일치하면 x축과 y축에 append
                if station['weekday'] == wd and station['count'] != 0:
                    station['difference'] = station['difference'] // station['count']
                    x2.append(station['stationName'])
                    y2.append(station['difference'])
            # 노선_요일 그래프 그리기
            print('Drawing : {}_{}'.format(row['subwayId'], wd))
            plt.figure(figsize=(16, 9))
            plt.bar(x2, y2)
            plt.xlabel('지하철 역명')
            plt.ylabel('평균 지연 시간')
            plt.title('{}_{}'.format(row['subwayId'], wd))
            plt.xticks(rotation=90)
            plt.savefig('data/img/{}_{}.png'.format(row['subwayId'], wd), dpi=500)
            plt.close()
            x1.append(row['subwayId'])
            y1.append(row['subwayDifference'])
        # 전체노선_요일 그래프 그리기
        print('Drawing : all_{}'.format(wd))
        plt.figure(figsize=(16, 9))
        plt.bar(x1, y1)
        plt.xlabel('지하철 노선 코드')
        plt.ylabel('평균 지연 시간')
        plt.title('전체노선_{}'.format(wd))
        plt.xticks(rotation=90)
        plt.savefig('data/img/all_{}.png'.format(wd), dpi=500)
        plt.close()
        # 경의중앙선의 오차가 너무 커, 경의중앙선을 제외한 그래프 그리기
        del x1[9]
        del y1[9]
        print('Drawing : except_1063_{}'.format(wd))
        plt.figure(figsize=(16, 9))
        plt.bar(x1, y1)
        plt.xlabel('지하철 노선 코드')
        plt.ylabel('평균 지연 시간')
        plt.title('전체노선_{}'.format(wd))
        plt.xticks(rotation=90)
        plt.savefig('data/img/except_1063_{}.png'.format(wd), dpi=500)
        plt.close()


# 해당 노선이 존재하는지 반환
def isSubwayIdExists(dictList, subwayId):
    for row in dictList:
        if row['subwayId'] == subwayId:
            return True
    return False


getGraph()
