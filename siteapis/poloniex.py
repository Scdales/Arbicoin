import requests, json, types
from apis.poloniexapi import *

polo = poloniex('INSERT API KEY HERE'
             ,'INSERT API SECRET HERE')
class POLONIEX(object):

    def __init__(self):

        self.name = "POLONIEX"

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

        #Polo will store 20xrp to maintain address
        self.xrp_wallet = 'XRP WALLET ADDRESS HERE'
        self.xrp_amount = 99

        self.usd_amount = 99

        self.fees = [0, 0.2]
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
            self.ltcbtc_tickerdata = polo.returnOrderBook('BTC_LTC')
            #print self.ltcbtc_tickerdata
            self.dogebtc_tickerdata = polo.returnOrderBook('BTC_DOGE')
            #print self.dogebtc_tickerdata
            self.ethbtc_tickerdata = polo.returnOrderBook('BTC_ETH')
            self.etcbtc_tickerdata = polo.returnOrderBook('BTC_ETC')
            self.xrpbtc_tickerdata = polo.returnOrderBook('BTC_XRP')

        except:
            print self.name + ' Ticker Retrieve Error'

            #LTCBTC
        for q in range(0,len(self.ltcbtc_tickerdata['bids'])):
            self.ltcbtc_bid.append(float(self.ltcbtc_tickerdata['bids'][q][0]))
            self.ltcbtc_bvol.append(float(self.ltcbtc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.ltcbtc_tickerdata['asks'])):
            self.ltcbtc_ask.append(float(self.ltcbtc_tickerdata['asks'][q][0]))
            self.ltcbtc_avol.append(float(self.ltcbtc_tickerdata['asks'][q][1]))

            #DOGEBTC
        for q in range(0,len(self.dogebtc_tickerdata['bids'])):
            self.dogebtc_bid.append(float(self.dogebtc_tickerdata['bids'][q][0]))
            self.dogebtc_bvol.append(float(self.dogebtc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.dogebtc_tickerdata['asks'])):
            self.dogebtc_ask.append(float(self.dogebtc_tickerdata['asks'][q][0]))
            self.dogebtc_avol.append(float(self.dogebtc_tickerdata['asks'][q][1]))

            #ETHBTC
        for q in range(0,len(self.ethbtc_tickerdata['bids'])):
            self.ethbtc_bid.append(float(self.ethbtc_tickerdata['bids'][q][0]))
            self.ethbtc_bvol.append(float(self.ethbtc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.ethbtc_tickerdata['asks'])):
            self.ethbtc_ask.append(float(self.ethbtc_tickerdata['asks'][q][0]))
            self.ethbtc_avol.append(float(self.ethbtc_tickerdata['asks'][q][1]))

            #ETCBTC
        for q in range(0,len(self.etcbtc_tickerdata['bids'])):
            self.etcbtc_bid.append(float(self.etcbtc_tickerdata['bids'][q][0]))
            self.etcbtc_bvol.append(float(self.etcbtc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.etcbtc_tickerdata['asks'])):
            self.etcbtc_ask.append(float(self.etcbtc_tickerdata['asks'][q][0]))
            self.etcbtc_avol.append(float(self.etcbtc_tickerdata['asks'][q][1]))

            #XRPBTC
        for q in range(0,len(self.xrpbtc_tickerdata['bids'])):
            self.xrpbtc_bid.append(float(self.xrpbtc_tickerdata['bids'][q][0]))
            self.xrpbtc_bvol.append(float(self.xrpbtc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.xrpbtc_tickerdata['asks'])):
            self.xrpbtc_ask.append(float(self.xrpbtc_tickerdata['asks'][q][0]))
            self.xrpbtc_avol.append(float(self.xrpbtc_tickerdata['asks'][q][1]))

    def getWallet(self):
        
        try:
            wallet = polo.returnBalances()
            self.btc_amount = float(wallet['BTC'])
            self.ltc_amount = float(wallet['LTC'])
            self.doge_amount = float(wallet['DOGE'])
            self.eth_amount = float(wallet['ETH'])
            self.etc_amount = float(wallet['ETC'])
            self.xrp_amount = float(wallet['XRP'])
        except:
            print self.name + ' Wallet Retrieve Error'
            
    def trade(self, symbol, bs, price, amount):
        sym = ''
        if symbol == 'ltc_btc':
            sym = 'BTC_LTC'
        if symbol == 'doge_btc':
            sym = 'BTC_DOGE'
        if symbol == 'eth_btc':
            sym = 'ETH_BTC'
        if symbol == 'etc_btc':
            sym = 'ETC_BTC'
        if symbol == 'xrp_btc':
            sym = 'XRP_BTC'
            
        try:
            if bs == 'buy':
                b = polo.buy(sym,price,amount)
            if bs == 'sell':
                b = polo.sell(sym,price,amount)
        except:
            print self.name + ' Trade Error'
        return b

    def withdraw(self,symb,amount,address):
        sym = ''
        if symb == 'btc':
            sym = 'BTC'
        if symb == 'ltc':
            sym = 'LTC'
        if symb == 'doge':
            sym = 'DOGE'
        if symb == 'eth':
            sym = 'ETH'
        if symb == 'etc':
            sym = 'ETC'
        if symb == 'xrp':
            sym = 'XRP'
            
        try:
            b = polo.withdraw(sym, amount, address)
        except:
            print self.name + ' Withdraw Error'
        return b

    def name(self):
        return self.name
