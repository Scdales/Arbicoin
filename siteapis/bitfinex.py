
import requests, json, types
from apis.bitfinexapi import *

bitfTrade = Trading('INSERT API KEY HERE'
	       ,'INSERT API SECRET HERE')

bitfPublic = Public()

class BITFINEX(object):

    def __init__(self):

        self.name = "BITFINEX"

        self.btc_wallet = 'BTC WALLET ADDRESS HERE'
        self.btc_amount = 99

        self.ltc_wallet = 'LTC WALLET ADDRESS HERE'
        self.ltc_amount = 99

        self.eth_wallet = 'ETH WALLET ADDRESS HERE'
        self.eth_amount = 99

        self.etc_wallet = 'ETC WALLET ADDRESS HERE'
        self.eth_amount = 99

        self.fees = [0, 0.2]
        self.withdrawfees = [0,0.001]

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

    def clean(self):
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

    def tickerRetrieve(self):
        #Ticker data grab from web
        self.clean()
        
        try:
            self.ltcbtc_tickerdata = bitfPublic.book('ltcbtc')
            self.ethbtc_tickerdata = bitfPublic.book('ethbtc')
            self.etcbtc_tickerdata = bitfPublic.book('etcbtc')
            
        except:
            print self.name + ' Ticker Retrieve Error'

        #LTCBTC
        for q in range(0,len(self.ltcbtc_tickerdata['bids'])):
            self.ltcbtc_bid.append(float(self.ltcbtc_tickerdata['bids'][q]['price']))
            self.ltcbtc_bvol.append(float(self.ltcbtc_tickerdata['bids'][q]['amount']))
        for q in range(0,len(self.ltcbtc_tickerdata['asks'])):
            self.ltcbtc_ask.append(float(self.ltcbtc_tickerdata['asks'][q]['price']))
            self.ltcbtc_avol.append(float(self.ltcbtc_tickerdata['asks'][q]['amount']))

        #ETHBTC
        for q in range(0,len(self.ethbtc_tickerdata['bids'])):
            self.ethbtc_bid.append(float(self.ethbtc_tickerdata['bids'][q]['price']))
            self.ethbtc_bvol.append(float(self.ethbtc_tickerdata['bids'][q]['amount']))
        for q in range(0,len(self.ethbtc_tickerdata['asks'])):    
            self.ethbtc_ask.append(float(self.ethbtc_tickerdata['asks'][q]['price']))
            self.ethbtc_avol.append(float(self.ethbtc_tickerdata['asks'][q]['amount']))

        #ETCBTC
        for q in range(0,len(self.etcbtc_tickerdata['bids'])):
            self.etcbtc_bid.append(float(self.etcbtc_tickerdata['bids'][q]['price']))
            self.etcbtc_bvol.append(float(self.etcbtc_tickerdata['bids'][q]['amount']))
        for q in range(0,len(self.etcbtc_tickerdata['asks'])):    
            self.etcbtc_ask.append(float(self.etcbtc_tickerdata['asks'][q]['price']))
            self.etcbtc_avol.append(float(self.etcbtc_tickerdata['asks'][q]['amount']))

    def getWallet(self):
        try:
            #Needs fixing
            wallet = bitfTrade.balances()
            self.btc_amount = float(wallet['result'][0]['Available'])
            self.eth_amount = float(wallet['result'][1]['Available'])
            self.ltc_amount = float(wallet['result'][2]['Available'])
            self.etc_amount = float(wallet['result'][3]['Available'])
            
        except:
            print self.name + ' Wallet Retrieve Error'
            
    def trade(self, symbol, bs, price, amount):
        sym = ''
        if symbol == 'ltc_btc':
            sym = 'ltcbtc'
        if symbol == 'eth_btc':
            sym = 'ethbtc'
        if symbol == 'etc_btc':
            sym = 'etcbtc'

        order_type = 'exchange' #may need changing
            
        if bs == 'buy':
            #try:
                b = bitfTrade.new_order(amount, price, bs, order_type, sym)
            #except:
            #    print self.name + ' Trade Error'
        if bs == 'sell':
            try:
                b = bitfTrade.new_order(amount, price, bs, order_type, sym)
            except:
                print self.name + ' Trade Error'
                
        return b

    def withdraw(self,symbol,amount,address):
        sym = ''
        if symbol == 'btc':
            sym = 'bitcoin'
        if symbol == 'ltc':
            sym = 'litecoin'
        if symbol == 'eth':
            sym = 'ethereum'
        if symbol == 'etc':
            sym = 'ethereumclassic'

        walletselected = 'exchange' #may need changing
            
        try:
            b = bitfTrade.withdraw(sym,address,amount,walletselected)
        except:
            print self.name + ' Withdraw Error'

        return b

    def name(self):
        return self.name
