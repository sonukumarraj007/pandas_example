
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd

#generate trading session
api_key = "4mskpbib2ifglgv7"
access_token = "hXdjB3MlIfGp6YuobGpyg3ECOZTl3hU1"

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)

def tokenLookup(instrument_df,symbol_list):
    """Looks up instrument token for a given script from instrument dump"""
    token_list = []
    for symbol in symbol_list:
        token_list.append(int(instrument_df[instrument_df.tradingsymbol==symbol].instrument_token.values[0]))
    return token_list

#####################update ticker list######################################
tickers = ["INFY", "ACC", "ICICIBANK"]
#############################################################################

#create KiteTicker object
kws = KiteTicker(api_key,kite.access_token)
tokens = tokenLookup(instrument_df,tickers)

def on_ticks(ws,ticks):
    # Callback to receive ticks.
    #logging.debug("Ticks: {}".format(ticks))
    print(ticks)

def on_connect(ws,response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    #logging.debug("on connect: {}".format(response))
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL,tokens) # Set all token tick in `full` mode.
    #ws.set_mode(ws.MODE_FULL,[tokens[0]])  # Set one token tick in `full` mode.
 

kws.on_ticks=on_ticks
kws.on_connect=on_connect
kws.connect()
