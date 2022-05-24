

from kiteconnect import KiteConnect

print(dir(KiteConnect))

api_key = "4mskpbib2ifglgv7"
api_secret = "t4j3z6wt3ahlh6x0tlgl02jh4xdm97e9"
request_token = "xrGaGyXptdj80wuPAJOgQdm5rS1CzRuU"
access_token = "WdsGSKmWjYtaY1Rp7KIeashtYwTlIR6t"

kite = KiteConnect(api_key=api_key)

#get access token
data = kite.generate_session(request_token, api_secret=api_secret)
print(data)

#kite.set_access_token(access_token=access_token)
#print(kite.orders())