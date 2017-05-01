# Cryptocoin Arbitrage Tracker

This compilation of scripts was written as an experiment to see if automatic arbitrage trading could be acheived accross different cryptocurrency exchange websites.

## The Rundown

Executing Run.py will request order book data from the following sites:
- <a href="https://btc-e.com/" target="_blank">Btce</a>
- <a href="https://www.kraken.com/" target="_blank">Kraken </a>
- <a href="https://www.livecoin.net/" target="_blank">Poloniex</a>
- <a href="https://www.bitfinex.com/" target="_blank">Bittrex</a>
- <a href="https://bittrex.com/" target="_blank">Bitfinex</a>
- <a href="https://poloniex.com/exchange" target="_blank">Livecoin</a>

The methods in 'calcFuncs2.py' are then called to process the data and calculate if arbitrage is possible

Each scripts inside 'siteapis' contains the class constructors that parses the returned JSON data from each website, and the 'apis' folder within contains the scripts for handling authentication and API interaction.

This project could be condensed a long way by making one script capable of talking to all the APIs, which is is planned for the future.

## Libraries

XLWT is a python excel library used for logging purposes<br/>
https://github.com/python-excel/xlwt

## Things left on the todo list
- [x] Upload to Github
- [ ] Factor in transaction costs in arbitrage calculation (each site is different)
- [ ] Finalise trade execution methods
- [ ] Wallet balance tracking
- [ ] Error/Exception handler + logger
- [ ] Tracking wallet transaction times
