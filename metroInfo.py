import urllib.request
import urllib.parse
import xml.dom.minidom
from env import *


def getMetroInfo(subwayStationId, dailyTypeCode, upDownTypeCode):
    METRO_INFO_URL = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList"
    METRO_INFO_QUERY = '?'+'ServiceKey=' + METRO_INFO_APIKEY + '&subwayStationId=' + subwayStationId + '&dailyTypeCode=' + dailyTypeCode + '&upDownTypeCode=' + upDownTypeCode
    METRO_INFO = urllib.request.urlopen(METRO_INFO_URL+METRO_INFO_QUERY)
    METRO_INFO_DOM = xml.dom.minidom.parse(METRO_INFO)
    PRETTY_METRO_INFO_DOM = METRO_INFO_DOM.toprettyxml()
    print(PRETTY_METRO_INFO_DOM)
    return PRETTY_METRO_INFO_DOM
