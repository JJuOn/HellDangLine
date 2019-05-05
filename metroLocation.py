import urllib.request
import urllib.parse
import xml.dom.minidom
from env import *


def getMetroLocation(END_INDEX,START_INDEX,rawSubwayNm):
    subwayNm = urllib.parse.quote_plus(rawSubwayNm)
    METRO_LOCATION_URL = "http://swopenapi.seoul.go.kr/api/subway/" + METRO_LOCATION_APIKEY + "/xml/realtimePosition/" + str(START_INDEX) + "/" + str(END_INDEX) + "/" + subwayNm
    # print(METRO_LOCATION_URL)
    METRO_LOCATION = urllib.request.urlopen(METRO_LOCATION_URL)
    METRO_LOCATION_DOM = xml.dom.minidom.parse(METRO_LOCATION)
    PRETTY_METRO_LOCATION_DOM = METRO_LOCATION_DOM.toprettyxml()
    # print(PRETTY_METRO_LOCATION_DOM)
    return PRETTY_METRO_LOCATION_DOM

