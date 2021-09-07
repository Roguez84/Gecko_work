# This is WIP
import pandas as pd
import requests
from IPython.display import display
from pprint import pprint

def get_ticker_data(tokens):
    ticker_data = []

    for coin_id in tokens
        response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}/tickers',
                                headers={'Content-Type': 'application/json'})
        # print(response.json())
        tickers = response.json()['tickers']
        for i in range(len(tickers)):
            parsed_ticker = {
                'coin_id': tickers[i]['coin_id'],
                'base': tickers[i]['base'],
                'target': tickers[i]['target'],
                'target_coin_id': tickers[i]['target_coin_id'] if 'target_coin_id' in tickers[i].keys() else "N/A",
                'market_identifier': tickers[i]['market']['identifier'],
                'volume': tickers[i]['volume'],
                'converted_volume_usd': tickers[i]['converted_volume']['usd'],
                'trust_score': tickers[i]['trust_score'],
                'timestamp': tickers[i]['timestamp'],
                'is_anomaly': tickers[i]['is_anomaly'],
                'is_stale': tickers[i]['is_stale'],
            }
            ticker_data.append(parsed_ticker)
    df = pd.DataFrame(ticker_data)
    # display(df)
    # df.to_csv(f'./ticker_data/{coin_id}.csv', header=True)
    # pass coin_id from other csv
    return(df)


a = get_ticker_data(['iotex','ethereum'])
