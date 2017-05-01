import requests, json, types
from apis.btceapi import BtceSetup
import apis.btceapi2

try:
    
    BtceTrade = BtceSetup('INSERT API KEY HERE'
	       ,'INSERT API SECRET HERE',
                     False)

    #Currencies must be defined here
    BtcePub = apis.btceapi2.PublicAPIv3('ltc_btc-eth_btc-eth_ltc')

    apikey = {'Key': 'INSERT API KEY HERE'
              ,'Secret':'INSERT API SECRET HERE'}
    BtceTr = apis.btceapi2.TradeAPIv1(apikey)
except:
    print 'BTCE Setup Failure'

class BTCE(object):

    def __init__(self):

        self.name = "BTCE"
        self.nonce = 1

        self.btc_wallet = 'BTC WALLET ADDRESS HERE'
        self.btc_amount = 99

        self.ltc_wallet = 'LTC WALLET ADDRESS HERE'
        self.ltc_amount = 99

        self.eth_wallet = 'ETH WALLET ADDRESS HERE'
        self.eth_amount = 99

        self.fees = [0, 0.25]
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

        self.ethltc_bid = []
        self.ethltc_bvol = []
        self.ethltc_ask = []
        self.ethltc_avol = []
        self.ethltc_tickerdata = 0

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

        self.ethltc_bid = []
        self.ethltc_bvol = []
        self.ethltc_ask = []
        self.ethltc_avol = []
        self.ethltc_tickerdata = 0

    def tickerRetrieve(self):
        self.clean()
        #Ticker data grab from web
        try:
            temp = BtcePub.call('depth', limit=100, ignore_invalid=1)
            self.ltcbtc_tickerdata = temp['ltc_btc']
            #print self.ltcbtc_tickerdata
            self.ethbtc_tickerdata = temp['eth_btc']
            #print self.ethbtc_tickerdata
            self.ethltc_tickerdata = temp['eth_ltc']
            #print self.ethltc_tickerdata
        except:
            print self.name + ' Ticker Retrieve Error'
            
        #LTCBTC
        for q in range(0,len(self.ltcbtc_tickerdata['bids'])):
            self.ltcbtc_bid.append(float(self.ltcbtc_tickerdata['bids'][q][0]))
            self.ltcbtc_bvol.append(float(self.ltcbtc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.ltcbtc_tickerdata['bids'])):
            self.ltcbtc_ask.append(float(self.ltcbtc_tickerdata['asks'][q][0]))
            self.ltcbtc_avol.append(float(self.ltcbtc_tickerdata['asks'][q][1]))

        #ETHBTC
        for q in range(0,len(self.ethbtc_tickerdata['bids'])):
            self.ethbtc_bid.append(float(self.ethbtc_tickerdata['bids'][q][0]))
            self.ethbtc_bvol.append(float(self.ethbtc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.ethbtc_tickerdata['bids'])):
            self.ethbtc_ask.append(float(self.ethbtc_tickerdata['asks'][q][0]))
            self.ethbtc_avol.append(float(self.ethbtc_tickerdata['asks'][q][1]))

        #ETHLTC
        for q in range(0,len(self.ethltc_tickerdata['bids'])):
            self.ethltc_bid.append(float(self.ethltc_tickerdata['bids'][q][0]))
            self.ethltc_bvol.append(float(self.ethltc_tickerdata['bids'][q][1]))
        for q in range(0,len(self.ltcbtc_tickerdata['bids'])):
            self.ethltc_ask.append(float(self.ethltc_tickerdata['asks'][q][0]))
            self.ethltc_avol.append(float(self.ethltc_tickerdata['asks'][q][1]))

    def getWallet(self):
            
        try:
            wallet = BtceTrade.getInfo()
            self.btc_amount = float(wallet['return']['funds']['btc'])
            self.ltc_amount = float(wallet['return']['funds']['ltc'])
            self.ltc_amount = float(wallet['return']['funds']['eth'])
            
        except:
            print self.name + ' Wallet Retrieve Error'
        

        

    def trade(self, symbol, bs, price, amount):
        #All values to be strings. Price and amount are string float values
        try:
            b = BtceTrade.Trade(symbol,bs,str(price),str(amount))
        except:
            print self.name + ' Trade Error'
            
        return b

    def withdraw(self, coin, amt, add):
        try:
            b = BtceTr.call('WithdrawCoin', coinName = coin, amount = str(amt), address = add)
            #b = BtceSetup.WithdrawCoin(coinName,amount,address)
        except:
            print self.name + ' Withdraw Error'
            
        return b

    def name(self):
        return self.name
