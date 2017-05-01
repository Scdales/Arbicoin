
import requests, json, types
from apis.bittrexapi import *

bitt = Bittrex('INSERT API KEY HERE'
	       ,'INSERT API SECRET HERE')

class BITTREX(object):

    def __init__(self):

        self.name = "BITTREX"

        self.btc_wallet = 'BTC WALLET ADDRESS HERE'
        self.btc_amount = 99

        self.ltc_wallet = 'LTC WALLET ADDRESS HERE'
        self.ltc_amount = 99

        self.doge_wallet = 'DOGE WALLET ADDRESS HERE'
        self.doge_amount = 99

        self.eth_wallet = 'ETH WALLET ADDRESS HERE'
        self.eth_amount = 99

        self.etc_wallet = 'ETC WALLET ADDRESS HERE'
        self.etc_amount = 99

        self.xrp_wallet = 'XRP WALLET ADDRESS HERE'
        self.xrp_tag = 'XRP TAG HERE'
        self.xrp_amount = 99

        self.fees = [0, 0.25]
        self.withdrawfees = [0,0.001]
        
        self.dogebtc_bid = []
        self.dogebtc_bvol = []
        self.dogebtc_ask = []
        self.dogebtc_avol = []
        self.dogebtc_tickerdata = 0

        self.ltcbtc_bid = []
        self.ltcbtc_bvol = []
        self.ltcbtc_ask = []
        self.ltcbtc_avol = []
        self.ltcbtc_tickerdata = 0

        self.ethbtc_bid = []
        self.ethbtc_bvol = []
        self.ethbtc_ask = []
        self.ethbtc_avol = []
        self.ethbtc_tickerdata = 0

        self.etcbtc_bid = []
        self.etcbtc_bvol = []
        self.etcbtc_ask = []
        self.etcbtc_avol = []
        self.etcbtc_tickerdata = 0

        self.xrpbtc_bid = []
        self.xrpbtc_bvol = []
        self.xrpbtc_ask = []
        self.xrpbtc_avol = []
        self.xrpbtc_tickerdata = 0

    def clean(self):
        self.dogebtc_bid = []
        self.dogebtc_bvol = []
        self.dogebtc_ask = []
        self.dogebtc_avol = []
        self.dogebtc_tickerdata = 0

        self.ltcbtc_bid = []
        self.ltcbtc_bvol = []
        self.ltcbtc_ask = []
        self.ltcbtc_avol = []
        self.ltcbtc_tickerdata = 0

        self.ethbtc_bid = []
        self.ethbtc_bvol = []
        self.ethbtc_ask = []
        self.ethbtc_avol = []
        self.ethbtc_tickerdata = 0

        self.etcbtc_bid = []
        self.etcbtc_bvol = []
        self.etcbtc_ask = []
        self.etcbtc_avol = []
        self.etcbtc_tickerdata = 0

        self.xrpbtc_bid = []
        self.xrpbtc_bvol = []
        self.xrpbtc_ask = []
        self.xrpbtc_avol = []
        self.xrpbtc_tickerdata = 0

    def tickerRetrieve(self):
        self.clean()
        #Ticker data grab from web
        try:
            self.ltcbtc_tickerdata = bitt.get_orderbook('BTC-LTC', 'both', 100)
            #print self.ltcbtc_tickerdata
            self.dogebtc_tickerdata = bitt.get_orderbook('BTC-DOGE', 'both', 100)
            #print self.dogebtc_tickerdata
            self.ethbtc_tickerdata = bitt.get_orderbook('BTC-ETH', 'both', 100)
            self.etcbtc_tickerdata = bitt.get_orderbook('BTC-ETC', 'both', 100)
            self.xrpbtc_tickerdata = bitt.get_orderbook('BTC-XRP', 'both', 100)

            #LTCBTC
            for q in range(0,len(self.ltcbtc_tickerdata['result']['buy'])):
                self.ltcbtc_bid.append(float(self.ltcbtc_tickerdata['result']['buy'][q]['Rate']))
                self.ltcbtc_bvol.append(float(self.ltcbtc_tickerdata['result']['buy'][q]['Quantity']))
            for q in range(0,len(self.ltcbtc_tickerdata['result']['sell'])):    
                self.ltcbtc_ask.append(float(self.ltcbtc_tickerdata['result']['sell'][q]['Rate']))
                self.ltcbtc_avol.append(float(self.ltcbtc_tickerdata['result']['sell'][q]['Quantity']))

            #DOGEBTC
            for q in range(0,len(self.dogebtc_tickerdata['result']['buy'])):
                self.dogebtc_bid.append(float(self.dogebtc_tickerdata['result']['buy'][q]['Rate']))
                self.dogebtc_bvol.append(float(self.dogebtc_tickerdata['result']['buy'][q]['Quantity']))
            for q in range(0,len(self.dogebtc_tickerdata['result']['sell'])):
                self.dogebtc_ask.append(float(self.dogebtc_tickerdata['result']['sell'][q]['Rate']))
                self.dogebtc_avol.append(float(self.dogebtc_tickerdata['result']['sell'][q]['Quantity']))

            #ETHBTC
            for q in range(0,len(self.ethbtc_tickerdata['result']['buy'])):
                self.ethbtc_bid.append(float(self.ethbtc_tickerdata['result']['buy'][q]['Rate']))
                self.ethbtc_bvol.append(float(self.ethbtc_tickerdata['result']['buy'][q]['Quantity']))
            for q in range(0,len(self.ethbtc_tickerdata['result']['sell'])):    
                self.ethbtc_ask.append(float(self.ethbtc_tickerdata['result']['sell'][q]['Rate']))
                self.ethbtc_avol.append(float(self.ethbtc_tickerdata['result']['sell'][q]['Quantity']))

            #ETCBTC
            for q in range(0,len(self.etcbtc_tickerdata['result']['buy'])):
                self.etcbtc_bid.append(float(self.etcbtc_tickerdata['result']['buy'][q]['Rate']))
                self.etcbtc_bvol.append(float(self.etcbtc_tickerdata['result']['buy'][q]['Quantity']))
            for q in range(0,len(self.etcbtc_tickerdata['result']['sell'])):    
                self.etcbtc_ask.append(float(self.etcbtc_tickerdata['result']['sell'][q]['Rate']))
                self.etcbtc_avol.append(float(self.etcbtc_tickerdata['result']['sell'][q]['Quantity']))

            #XRPBTC
            for q in range(0,len(self.xrpbtc_tickerdata['result']['buy'])):
                self.xrpbtc_bid.append(float(self.xrpbtc_tickerdata['result']['buy'][q]['Rate']))
                self.xrpbtc_bvol.append(float(self.xrpbtc_tickerdata['result']['buy'][q]['Quantity']))
            for q in range(0,len(self.xrpbtc_tickerdata['result']['sell'])):    
                self.xrpbtc_ask.append(float(self.xrpbtc_tickerdata['result']['sell'][q]['Rate']))
                self.xrpbtc_avol.append(float(self.xrpbtc_tickerdata['result']['sell'][q]['Quantity']))

        except:
            print self.name + ' Ticker Retrieve Error'

    def getWallet(self):

        try:
            wallet = bitt.get_balances()
            self.btc_amount = float(wallet['result'][0]['Available'])
            self.doge_amount = float(wallet['result'][1]['Available'])
            self.ltc_amount = float(wallet['result'][2]['Available'])
            self.eth_amount = float(wallet['result'][3]['Available'])
            self.etc_amount = float(wallet['result'][4]['Available'])
            self.xrp_amount = float(wallet['result'][5]['Available'])
        except:
            print self.name + ' Wallet Retrieve Error'
            
    def trade(self, symbol, bs, price, amount):
        sym = ''
        if symbol == 'ltc_btc':
            sym = 'BTC-LTC'
        if symbol == 'doge_btc':
            sym = 'BTC-DOGE'
        if symbol == 'eth_btc':
            sym = 'BTC-ETH'
        if symbol == 'etc_btc':
            sym = 'BTC-ETC'
        if symbol == 'xrp_btc':
            sym = 'BTC-XRP'
            
        if bs == 'buy':
            try:
                b = bitt.buy_limit(sym,amount,price)
            except:
                print self.name + ' Trade Error'
        if bs == 'sell':
            try:
                b = bitt.sell_limit(sym,amount,price)
            except:
                print self.name + ' Trade Error'
                
        return b

    def withdraw(self,symbol,amount,address):
        sym = ''
        if symbol == 'btc':
            sym = 'BTC'
        if symbol == 'ltc':
            sym = 'LTC'
        if symbol == 'doge':
            sym = 'DOGE'
        if symbol == 'eth':
            sym = 'ETH'
        if symbol == 'etc':
            sym = 'ETC'
        if symbol == 'xrp':
            sym = 'XRP'
            
        try:
            b = bitt.withdraw(sym,amount,address)
        except:
            print self.name + ' Withdraw Error'

        return b

    def name(self):
        return self.name
