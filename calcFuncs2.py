from operator import itemgetter
import xlwt
from datetime import *
## Helper Functions

def difference(bid,ask):
    return (float(bid)-float(ask))
def percentage(bid,ask):
    return (bid-ask)/bid*100

def writeExcel(exchangelist, q, wb, ws, name, buyname, buyamount):
    
    style0 = xlwt.easyxf('font: name Times New Roman, bold on',
    num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='h:mm:ss')
    
    if q == 1:
        for z in range(len(exchangelist)):
            ws.write(0, z, exchangelist[z][1], style0)
        ws.write(0, len(exchangelist)+2, 'Bought At', style0)
    for z in range(len(exchangelist)):
        ws.write(q, z, exchangelist[z][0])
    ws.write(q, len(exchangelist)+2, buyname)
    ws.write(q, len(exchangelist)+3, buyamount)
        
    a = name + '.xls'

    wb.save('Log2.xls')
    
    return

def display(bidsort, bidname, asksort, askname, name):
    #print bidsort
    bid = bidsort[0][0]
    ask = asksort[0][0]

    a = difference(bid,ask)
    b = percentage(bid,ask)

    if name == 'dogebtc':
        print len(bidsort),'/',len(asksort),'DOGEBTC Difference between',\
        bidname,'at:','%.9f' % (bid),'Bid and',askname,'Ask at','%.9f' % (ask),\
        'with difference at','%.9f' % (difference(bid,ask)),\
        'and percentage at',percentage(bid,ask),'%','\n'
                                       
    else:
        print len(bidsort),'/',len(asksort),name, 'Difference between',\
        bidname,'Bid at:',\
        '%f.9' %(bid),'and',askname,'Ask at:','%f.9' % (ask),\
        'with difference at','%f' % a,\
        'and percentage at','%f' % b,'%','\n'


##  DOGEBTC
def dogebtcDiff(exes, rowCounter, ws, wb):
    exchanges = []
    for a in exes:
        if hasattr(a, 'dogebtc_tickerdata'):
            exchanges.append(a)
            print a.name + "has teh dogey"
    
    bidList = []
    for z in exchanges:
        bidList.append([tradeAmount(z.dogebtc_ask, z.dogebtc_avol,1),z.name])
        bidSort = sorted(bidList,key=itemgetter(0),reverse=True)
    askList = []
    print 'DOGEBTC'
    print bidSort
    for z in exchanges:
        askList.append([tradeAmount2(z.dogebtc_bid, z.dogebtc_bvol, bidSort[0][0]),z.name])
        print z.name + ' = ' + str(tradeAmount2(z.dogebtc_bid, z.dogebtc_bvol, bidSort[0][0]))
    askSort = sorted(askList,key=itemgetter(0),reverse=True)
    print ''

    writeExcel(askSort, rowCounter, ws, wb, 'dogebtc', bidSort[0][1], bidSort[0][0])

##  ETHBTC
def ethbtcDiff(exes, rowCounter, ws, wb):
    exchanges = []
    for a in exes:
        if hasattr(a, 'ethbtc_tickerdata'):
            exchanges.append(a)
            print a.name + "has teh ether"
    
    bidList = []
    for z in exchanges:
        bidList.append([tradeAmount(z.ethbtc_ask, z.ethbtc_avol,1),z.name])
        bidSort = sorted(bidList,key=itemgetter(0),reverse=True)
    askList = []
    print 'ETHBTC'
    print bidSort
    for z in exchanges:
        askList.append([tradeAmount2(z.ethbtc_bid, z.ethbtc_bvol, bidSort[0][0]),z.name])
        print z.name + ' = ' + str(tradeAmount2(z.ethbtc_bid, z.ethbtc_bvol, bidSort[0][0]))
    askSort = sorted(askList,key=itemgetter(0),reverse=True)
    print ''

    writeExcel(askSort, rowCounter, ws, wb, 'ethbtc', bidSort[0][1], bidSort[0][0])
    
##  LTCBTC
def ltcbtcDiff(exes, rowCounter, ws, wb):    
    exchanges = []
    for a in exes:
        if hasattr(a, 'ltcbtc_tickerdata'):
            exchanges.append(a)
            print a.name + "has teh lite"
    
    bidList = []
    for z in exchanges:
        bidList.append([tradeAmount(z.ltcbtc_ask, z.ltcbtc_avol,1),z.name])
        
    bidSort = sorted(bidList,key=itemgetter(0),reverse=True)
    askList = []
    print 'LTCBTC'
    print bidSort
    for z in exchanges:
        askList.append([tradeAmount2(z.ltcbtc_bid, z.ltcbtc_bvol, bidSort[0][0]),z.name])
        print z.name + ' = ' + str(tradeAmount2(z.ltcbtc_bid, z.ltcbtc_bvol, bidSort[0][0]))
    askSort = sorted(askList,key=itemgetter(0),reverse=True)
    print ''
    
    writeExcel(askSort, rowCounter, ws, wb, 'ltcbtc', bidSort[0][1], bidSort[0][0])

##  ETCBTC
def etcbtcDiff(exes, rowCounter, ws, wb):
    exchanges = []
    for a in exes:
        if hasattr(a, 'etcbtc_tickerdata'):
            exchanges.append(a)
            print a.name + "has teh etherSEE"
    
    bidList = []
    for z in exchanges:
        bidList.append([tradeAmount(z.etcbtc_ask, z.etcbtc_avol,1),z.name])
        bidSort = sorted(bidList,key=itemgetter(0),reverse=True)
    askList = []
    print 'ETCBTC'
    print bidSort
    for z in exchanges:
        askList.append([tradeAmount2(z.etcbtc_bid, z.etcbtc_bvol, bidSort[0][0]),z.name])
        print z.name + ' = ' + str(tradeAmount2(z.etcbtc_bid, z.etcbtc_bvol, bidSort[0][0]))
    askSort = sorted(askList,key=itemgetter(0),reverse=True)
    print ''

    writeExcel(askSort, rowCounter, ws, wb, 'etcbtc', bidSort[0][1], bidSort[0][0])

##  XRPBTC
def xrpbtcDiff(exes, rowCounter, ws, wb):
    exchanges = []
    for a in exes:
        if hasattr(a, 'xrpbtc_tickerdata'):
            exchanges.append(a)
            print a.name + "has teh ripple"
    
    bidList = []
    for z in exchanges:
        bidList.append([tradeAmount(z.xrpbtc_ask, z.xrpbtc_avol,1),z.name])
        bidSort = sorted(bidList,key=itemgetter(0),reverse=True)
    askList = []
    print 'XRPBTC'
    print bidSort
    for z in exchanges:
        askList.append([tradeAmount2(z.xrpbtc_bid, z.xrpbtc_bvol, bidSort[0][0]),z.name])
        print z.name + ' = ' + str(tradeAmount2(z.xrpbtc_bid, z.xrpbtc_bvol, bidSort[0][0]))
    askSort = sorted(askList,key=itemgetter(0),reverse=True)
    print ''

    writeExcel(askSort, rowCounter, ws, wb, 'xrpbtc', bidSort[0][1], bidSort[0][0])

    
def tradeAmount(price, quant, btc):
    summ = 0
    for a in range(0,len(price)):

        temp  = btc - (price[a]*quant[a])
        if temp >= 0:
            #print 'trade:',price[a]*quant[a],'BTC for',quant[a],'at:',price[a]
            summ = summ + quant[a]
            btc = temp
            #print '>= 0' , btc
        elif temp < 0:
            #print 'trade:',btc,'BTC for',(btc / price[a]),'at:',price[a]
            summ = summ + (btc/price[a])
            btc = 0
            #print '< 0' , btc
        if btc == 0:
            #print 'btc == 0'
            break
        #print a
    return summ

def tradeAmount2(price, quant, ltc):
    summ = 0
    
    for a in range(0,len(price)):

        temp  = ltc - quant[a]
        if temp >= 0:
            #print 'trade:',quant[a],'LTC for',(price[a]*quant[a]),'BTC at:',price[a]
            summ = summ + price[a]*quant[a]
            ltc = temp
            #print '>=0' , ltc
        elif temp < 0:
            #print 'trade:',ltc,'BTC for',(price[a]*ltc),'at:',price[a]
            summ = summ + (ltc * price[a])
            ltc = 0
            #print '<0' , ltc

        if ltc == 0:
            #print 'ltc == 0'
            break
        #print a
    return summ
