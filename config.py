# Bitstamp ticker endpoint. More datails here https://www.bitstamp.net/api/
endpoint = "https://www.bitstamp.net/api/v2/ticker_hour/" 

# Watched crypto pairs. All available pairs - https://www.bitstamp.net/api/v2/trading-pairs-info/
watchedCryptos = [{"pair":"ethusd", "min":2000, "max":3000},{"pair":"btcusd", "min":50000, "max":60000}] 

# Emailing config
mailConfig = {"address":"smtp address", "username":"login", "password":"password","From":"sender email", "To":"receiver email", "Subject":"Crypto alert", "Body": "Crypto pair X has reached the Y limit"}