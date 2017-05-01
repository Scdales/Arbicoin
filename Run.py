import requests, json, types, os
from time import sleep
from calcFuncs2 import *

import siteapis.btce
import siteapis.kraken
import siteapis.poloniex
import siteapis.bittrex
import siteapis.bitfinex
import siteapis.livecoin

import xlwt
from datetime import datetime

#Wallets still remaining to be fixed
Btce = siteapis.btce.BTCE() 
Kraken = siteapis.kraken.KRAKEN() 
Poloniex = siteapis.poloniex.POLONIEX() 
Bittrex = siteapis.bittrex.BITTREX()
Bitfinex = siteapis.bitfinex.BITFINEX()
Livecoin = siteapis.livecoin.LIVECOIN()
#AnxPro
#Gdax
#Yunbi
#Coinbase?


#Setup Logging Excel Workbook
excelTracker = xlwt.Workbook()
ltcbtc = excelTracker.add_sheet('LTCBTC', cell_overwrite_ok=True)
ethbtc = excelTracker.add_sheet('ETHBTC', cell_overwrite_ok=True)
dogebtc = excelTracker.add_sheet('DOGEBTC', cell_overwrite_ok=True)
etcbtc = excelTracker.add_sheet('ETCBTC', cell_overwrite_ok=True)
xrpbtc = excelTracker.add_sheet('XRPBTC', cell_overwrite_ok=True)

rowCounter = 1

exchanges = [Btce, Kraken, Poloniex, Bittrex, Bitfinex, Livecoin]

print
print "hello"

#raise RuntimeError
sleeptime = 1

while (True):

    for a in range(len(exchanges)):
        print exchanges[a].name + " ding!"
        exchanges[a].tickerRetrieve()
    print ''
    print 'BOOM'
    print ''

    dogebtcDiff(exchanges, rowCounter, excelTracker, dogebtc)
    ltcbtcDiff(exchanges, rowCounter, excelTracker, ltcbtc)
    ethbtcDiff(exchanges, rowCounter, excelTracker, ethbtc)
    etcbtcDiff(exchanges, rowCounter, excelTracker, etcbtc)
    xrpbtcDiff(exchanges, rowCounter, excelTracker, xrpbtc)
    rowCounter = rowCounter + 1

    #raise RuntimeError

    print '-------------------------------------------'
    sleep(sleeptime)
    print 'zzz.....'+str(sleeptime)
    print
