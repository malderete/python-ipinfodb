# *-* coding: utf-8*-*
'''
ipinfodb.py

Copyright 2010 Martin Alderete

ipinfodb is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

ipinfodb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyPlugin; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

<<END_LICENSE>>
'''


import socket
import urllib2
import urllib
import simplejson


class API(object):
    '''
    Usage
    For city precision, simply do a query at this address (if you omit the IP
    parameter it will check with your own IP) :
        http://api.ipinfodb.com/v3/ip-city/?key=<your_api_key>&ip=74.125.45.100&format=json
        {'countryCode': 'AR', 'cityName': 'BUENOS AIRES', 'zipCode': '-',
        'longitude': '-58.47', 'countryName': 'ARGENTINA', 'latitude':
        '-34.613', 'timeZone': '-03:00', 'statusCode': 'OK', 'ipAddress':
        '190.191.58.56', 'statusMessage': '', 'regionName': 'DISTRITO FEDERAL'}

    For country precision (faster), simply do a query with the following API :
        http://api.ipinfodb.com/v3/ip-country/?key=<your_api_key>&ip=74.125.45.100&format=json
        {'countryName': 'ARGENTINA', 'ipAddress': '190.191.58.56',
        'countryCode': 'AR', 'statusMessage': '', 'statusCode': 'OK'}

    @author: Martin Alderete (malderete@gmail.com)
    '''
    def __init__(self, api_key):
        self._api_key = api_key

    def getCityUrl(self):
        return 'http://api.ipinfodb.com/v3/ip-city/'

    def getCountryUrl(self):
        return 'http://api.ipinfodb.com/v3/ip-country/'

    def GetCity(self, ip):
        query_parameters = {
                'key': self._api_key,
                'ip': ip,
                'format': 'json'
        }
        url = self.getCityUrl() + '?' + urllib.urlencode(query_parameters)
        try:
            file_obj = urllib2.urlopen(url)
        except urllib2.URLError, e:
            print "URLError"
            raise
        except urllib2.HTTPError, e:
            print "HTTPError"
            raise
            
        data = file_obj.read()
        data_dict = self._parseResponse(data)
        file_obj.close()
        return data_dict

    def GetCountry(self, ip):
        query_parameters = {
                'key': self._api_key,
                'ip': ip,
                'format': 'json'
        }
        url = self.getCountryUrl() + '?' + urllib.urlencode(query_parameters)
        try:
            file_obj = urllib2.urlopen(url)
        except urllib2.URLError, e:
            print "URLError"
            raise
        except urllib2.HTTPError, e:
            print "HTTPError"
            raise
            
        data = file_obj.read()
        data_dict = self._parseResponse(data)
        file_obj.close()
        return data_dict

    def _parseResponse(self, data):
        return simplejson.loads(data)

def get_ip_from_name(name, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((name, port))
        return s.getpeername()[0]
    except Exception, e:
        print "Socket Error: %s" % e
        raise

