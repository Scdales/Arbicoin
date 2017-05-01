import requests, json, types
from apis.livecoinapi import *

livecoin = Livecoin()
#Keys in api

class LIVECOIN(object):

    def __init__(self):

        self.name = "LIVECOIN"

        self.btc_wallet = 'BTC WALLET ADDRESS HERE'
        self.btc_amount = 99

        self.ltc_wallet = 'LTC WALLET ADDRESS HERE'
        self.ltc_amount = 99

        self.doge_wallet = 'DOGE WALLET ADDRESS HERE'
        self.doge_amount = 99

        self.eth_wallet = 'ETH WALLET ADDRESS HERE'
        self.eth_amount = 99

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

    def tickerRetrieve(self):
        self.clean()
        #Ticker data grab from web
        try:
            self.ltcbtc_tickerdata = livecoin.get("/exchange/order_book",[('currencyPair', 'LTC/BTC')])
            #print self.ltcbtc_tickerdata
            self.dogebtc_tickerdata = livecoin.get("/exchange/order_book",[('currencyPair', 'DOGE/BTC')])
            #print self.dogebtc_tickerdata
            self.ethbtc_tickerdata = livecoin.get("/exchange/order_book",[('currencyPair', 'ETH/BTC')])

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

    def getWallet(self):
        
        try:
            wallet = polo.returnBalances()
            self.btc_amount = float(wallet['BTC'])
            self.ltc_amount = float(wallet['LTC'])
            self.doge_amount = float(wallet['DOGE'])
            self.eth_amount = float(wallet['ETH'])
        except:
            print self.name + ' Wallet Retrieve Error'
            
    def trade(self, symbol, bs, price, amount):
        sym = ''
        if symbol == 'ltc_btc':
            sym = 'LTC/BTC'
        if symbol == 'doge_btc':
            sym = 'DOGE/BTC'
        if symbol == 'eth_btc':
            sym = 'ETH/BTC'
            
        try:
            if bs == 'buy':
                b = livecoin.post('/exchange/buylimit',[('currencyPair',sym),('price',price),
                                                       ('quantity',amount)])
            if bs == 'sell':
                b = livecoin.post('/exchange/selllimit',[('currencyPair',sym),('price',price),
                                                       ('quantity',amount)])
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
            
        try:
            b = livecoin.post("/payment/out/coin",[('amount',amount),('currency',symb),
                                                   ('wallet',address)])
        except:
            print self.name + ' Withdraw Error'
        return b

    def name(self):
        return self.name
