from env import *
import urllib.request
import xml.dom.minidom

subwayStationId = 'SUB228'
dailyTypeCode = '03'
upDownTypeCode ='U'
METRO_INFO_URL = "http://openapi.tago.go.kr/openapi/service/SubwayInfoService/getSubwaySttnAcctoSchdulList"
queryParams = '?'+'ServiceKey='+METRO_INFO_APIKEY+'&subwayStationId='+subwayStationId+'&dailyTypeCode='+dailyTypeCode+'&upDownTypeCode='+upDownTypeCode
webpage = urllib.request.urlopen(METRO_INFO_URL+queryParams)
dom=xml.dom.minidom.parse(webpage)
pretty_xml_as_string=dom.toprettyxml()
print(pretty_xml_as_string)
#webpage.close()

