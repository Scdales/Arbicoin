import httplib
import urllib
import json
import hashlib
import hmac
from collections import OrderedDict

class Livecoin(object):

#methods must be strings starting with / and using ""
#args must be in dictionary form

    def get(self, methodical, args):

        server = "api.livecoin.net"
        method = methodical
        #"/exchange/order_book"
        api_key = "INSERT API KEY HERE"
        secret_key = "INSERT API SECRET HERE"
         
        #data = OrderedDict([('currencyPair', 'BTC/USD')])
        data = OrderedDict(args)
        
        encoded_data = urllib.urlencode(data)
         
        sign = hmac.new(secret_key, msg=encoded_data, digestmod=hashlib.sha256).hexdigest().upper()
         
        headers = {"Api-key": api_key, "Sign": sign}
         
        conn = httplib.HTTPSConnection(server)
        conn.request("GET", method + '?' + encoded_data, '', headers)
         
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
         
        return data

    def post(self, methodical, arge):
        #arge must be an array of tuples
        
        
        server = "api.livecoin.net"
        method = methodical
        #"/exchange/buylimit"
        api_key = "INSERT API KEY HERE"
        secret_key = "INSERT API SECRET HERE"
         
        data = OrderedDict(sorted([('currencyPair', 'BTC/USD'),('price', '100'),('quantity', '0.01')]))
        #data = OrderedDict(arge)
        encoded_data = urllib.urlencode(data)
         
        sign = hmac.new(secret_key, msg=encoded_data, digestmod=hashlib.sha256).hexdigest().upper()
         
        headers = {"Api-key": api_key, "Sign": sign, "Content-type": "application/x-www-form-urlencoded"}
         
        conn = httplib.HTTPSConnection(server)
        conn.request("POST", method, encoded_data, headers)
         
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
         
        return data
