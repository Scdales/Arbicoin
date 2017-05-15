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

## Understanding the output
Currently, this program hasn't yet been connected to the trading accounts on any of the exchanges, however the basic functionality has been implemented. Running the program essentially runs a test on the order book data it receives assuming you are trading with 1 BTC.
After the orderbook data has been collected from each site, the program will display a list of the volume of each cryptocurrency you would receive on each site respectively. The trade deal.
The program then takes the highest amount, then iterates through the sell data on each site to see if that volume can be traded back at a profit. The second set of output lists what you would receive on each site when converting back to Bitcoin.

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
