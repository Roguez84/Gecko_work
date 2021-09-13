# This is WIP
import pandas as pd
import requests
from IPython.display import display
from pprint import pprint
#from all_exchange_tokens import get_exchange_tokens
import csv

token_array = []

with open("kucoin_tickers.csv") as file_name:
    file_read = csv.reader(file_name)
    for row in file_read:        
        token_array.append(row[0]) 


def get_ticker_data(tokens):
    ticker_data = []

    for coin_id in tokens:
        #print(coin_id)
        if coin_id == 'bitcoin' or coin_id == 'ethereum':
            next
        else:
            response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}/tickers',
                                    headers={'Content-Type': 'application/json'})

            # print(response.json())
            tickers = response.json()['tickers']
            #print(len(tickers))
            for i in range(len(tickers)):

                parsed_ticker = {
                    'coin_id': tickers[i]['coin_id'],
                    'base': tickers[i]['base'],
                    'target': tickers[i]['target'],
                    # 'target_coin_id': tickers[i]['target_coin_id'] if 'target_coin_id' in tickers[i].keys() else "N/A",
                    'market_identifier': tickers[i]['market']['identifier'],
                    # 'volume': tickers[i]['volume'],
                    'converted_volume_usd': tickers[i]['converted_volume']['usd'],
                    'trust_score': tickers[i]['trust_score'],
                    # 'timestamp': tickers[i]['timestamp'],
                    # 'is_anomaly': tickers[i]['is_anomaly'],
                    # 'is_stale': tickers[i]['is_stale'],
                }
                ticker_data.append(parsed_ticker)
    df = pd.DataFrame(ticker_data)
    # display(df)
    # df.to_csv(f'./ticker_data/{coin_id}.csv', header=True)
    # pass coin_id from other csv
    return(df)


# a = get_ticker_data(['iotex','ethereum'])
tickers_to_check = pd.DataFrame(token_array[0:49])
tickers_to_check.to_csv(f'./tickers_checked.csv', index=False)
# a = get_ticker_data(tickers_to_check)
# a.to_csv(f'./token_volumes.csv', index=False)
#print(a)
