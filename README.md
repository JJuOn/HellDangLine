# 2019-01-웹/파이썬프로그래밍 Term Project 헬당선
- 지하철 시간표상의 도착 시간과 실제 지하철 도착시간 비교

# 지하철 노선 코드
- 1001 : 1호선
- 1002 : 2호선
- 1003 : 3호선
- 1004 : 4호선
- 1005 : 5호선
- 1006 : 6호선
- 1007 : 7호선
- 1008 : 8호선
- 1009 : 9호선
- 1063 : 경의중앙선
- 1065 : 공항철도
- 1067 : 경춘선
- 1071 : 수인선
- 1075 : 분당선
- 1077 : 신분당선

# python
- metroIds.py : 지하철 노선 코드와 역 ID, 역명 획득
- metroCodes.py : data/metroId에 역코드, 역외부코드 추가
- metroIdTimetable.py : 지하철역별 시간표 획득
- metroLocation.py : 서울시 지하철 API를 바탕으로 지하철 노선별 위치정보 획득
- metroArrival.py : 서울시 대중교통 정보 API를 바탕으로 지하철 역별 도착정보 획득
- getResult.py : 획득한 지하철 도착정보를 바탕으로 지하철 노선별, 역별, 열차번호별로 도착시간의 합 계산 

# data
## data/raw
- 가공전 원본 데이터 저장

## data/metroId
- 지하철 노선별로 지하철 노선 코드, 역 ID, 역명, 역코드, 역외부코드 저장

## data/timetable
- (지하철 노선 코드)\_(역코드)\_(요일)\_(상/하행).csv
- 열차 번호, 출발 역코드, 종착 역코드, 도착 시간, 출발 시간, 급행여부 저장

## data/location/(date)
- 지하철의 도착시간 데이터 저장
- 역 ID, 열차 번호, 종착 역명, 도착 시간, 요일, 상/하행 저장

## data/timesum
- (지하철 노선 코드)\_(역 ID)\_(요일)\_(상/하행).csv
- 열차 번호, 종착 역명, 도착 시간의 합, 카운트 저장