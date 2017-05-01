import requests, json, types
import apis.krakenex

Krak = apis.krakenex.API('INSERT API KEY HERE'
             ,'INSERT API SECRET HERE')

class KRAKEN(object):

    def __init__(self):

        self.name = "KRAKEN"

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

        self.tradefees = [0,0.26]
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
        self.ethbtc_tickerdata = 00

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
            self.ltcbtc_tickerdata = Krak.query_public('Depth',{'pair':'XLTCXXBT','count':100})
            self.dogebtc_tickerdata = Krak.query_public('Depth',{'pair':'XXDGXXBT','count':100})
            self.ethbtc_tickerdata = Krak.query_public('Depth',{'pair':'XETHXXBT','count':100})
            self.etcbtc_tickerdata = Krak.query_public('Depth',{'pair':'XETCXXBT','count':100})
            self.xrpbtc_tickerdata = Krak.query_public('Depth',{'pair':'XXRPXXBT','count':100})


        except:
                print self.name + ' Ticker Retrieve Error'

            #BTXLTX
        for q in range(0,len(self.ltcbtc_tickerdata['result']['XLTCXXBT']['asks'])):
            self.ltcbtc_ask.append(float(self.ltcbtc_tickerdata['result']['XLTCXXBT']['asks'][q][0]))
            self.ltcbtc_avol.append(float(self.ltcbtc_tickerdata['result']['XLTCXXBT']['asks'][q][1]))
        for q in range(0,len(self.ltcbtc_tickerdata['result']['XLTCXXBT']['bids'])):
            self.ltcbtc_bid.append(float(self.ltcbtc_tickerdata['result']['XLTCXXBT']['bids'][q][0]))
            self.ltcbtc_bvol.append(float(self.ltcbtc_tickerdata['result']['XLTCXXBT']['bids'][q][1]))

            #BTCDOGE
            #Needs reversing for comparing
        for q in range(0,len(self.dogebtc_tickerdata['result']['XXDGXXBT']['asks'])):
            self.dogebtc_ask.append(float(self.dogebtc_tickerdata['result']['XXDGXXBT']['asks'][q][0]))
            self.dogebtc_avol.append(float(self.dogebtc_tickerdata['result']['XXDGXXBT']['asks'][q][1]))
        for q in range(0,len(self.dogebtc_tickerdata['result']['XXDGXXBT']['bids'])):
            self.dogebtc_bid.append(float(self.dogebtc_tickerdata['result']['XXDGXXBT']['bids'][q][0]))
            self.dogebtc_bvol.append(float(self.dogebtc_tickerdata['result']['XXDGXXBT']['bids'][q][1]))

            #ETHBTC
        for q in range(0,len(self.ethbtc_tickerdata['result']['XETHXXBT']['bids'])):
            self.ethbtc_bid.append(float(self.ethbtc_tickerdata['result']['XETHXXBT']['bids'][q][0]))
            self.ethbtc_bvol.append(float(self.ethbtc_tickerdata['result']['XETHXXBT']['bids'][q][1]))
        for q in range(0,len(self.ethbtc_tickerdata['result']['XETHXXBT']['asks'])):
            self.ethbtc_ask.append(float(self.ethbtc_tickerdata['result']['XETHXXBT']['asks'][q][0]))
            self.ethbtc_avol.append(float(self.ethbtc_tickerdata['result']['XETHXXBT']['asks'][q][1]))

            #ETCBTC
        for q in range(0,len(self.etcbtc_tickerdata['result']['XETCXXBT']['bids'])):
            self.etcbtc_bid.append(float(self.etcbtc_tickerdata['result']['XETCXXBT']['bids'][q][0]))
            self.etcbtc_bvol.append(float(self.etcbtc_tickerdata['result']['XETCXXBT']['bids'][q][1]))
        for q in range(0,len(self.etcbtc_tickerdata['result']['XETCXXBT']['asks'])):
            self.etcbtc_ask.append(float(self.etcbtc_tickerdata['result']['XETCXXBT']['asks'][q][0]))
            self.etcbtc_avol.append(float(self.etcbtc_tickerdata['result']['XETCXXBT']['asks'][q][1]))

            #XRPBTC
        for q in range(0,len(self.xrpbtc_tickerdata['result']['XXRPXXBT']['bids'])):
            self.xrpbtc_bid.append(float(self.xrpbtc_tickerdata['result']['XXRPXXBT']['bids'][q][0]))
            self.xrpbtc_bvol.append(float(self.xrpbtc_tickerdata['result']['XXRPXXBT']['bids'][q][1]))
        for q in range(0,len(self.xrpbtc_tickerdata['result']['XXRPXXBT']['asks'])):
            self.xrpbtc_ask.append(float(self.xrpbtc_tickerdata['result']['XXRPXXBT']['asks'][q][0]))
            self.xrpbtc_avol.append(float(self.xrpbtc_tickerdata['result']['XXRPXXBT']['asks'][q][1]))

        
    def getWallet(self):
        
        #FOLLOWING MUST BE TESTED
        try:
            wallet = Krak.query_private('Balance')
            self.ltc_amount = float(Krak.query_private('Balance'))
            self.doge_amount = float(Krak.query_private('Balance'))
            self.eth_amount = float(Krak.query_private('Balance'))
            self.etc_amount = float(Krak.query_private('Balance'))
            self.xrp_amount = float(Krak.query_private('Balance'))
        except:
            print self.name + ' Wallet Retrieve Error'


    def trade(self, symbol, bs, price, amount):
        sym = ''
        if symbol == 'btc_ltc': #NOTE: BITCOIN -> LITECOIN
            sym = 'XBTLTC'
        if symbol == 'btc_doge': #NOTE: BITCOIN -> DOGECOIN
            sym = 'XBTXDG'
        if symbol == 'eth_btc':
            sym = 'ETHXBT'
        if symbol == 'etc_btc':
            sym = 'ETCXBT'
        if symbol == 'xrp_btc':
            sym = 'XRPXBT'
            
        try:
            b = Krak.query_private('AddOrder',{'pair':sym,'type':bs
                                           ,'price':price,'ordertype':'limit','volume':amount})
        except:
            print self.name + ' Trade Error'

        return b

    def withdraw(self,symbol,amount,address):
        try:
            print 'Not Yet Implemented'
        except:
            print self.name + ' Withdraw Error'

    def name(self):
        return self.name
