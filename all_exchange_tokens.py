import pandas as pd
import requests
from IPython.display import display
from pprint import pprint

def get_exchange_tokens(exchange,page_num):
    ticker_data = []
    
    for p in range(1,page_num,1):
        #ticker_data = []
        response = requests.get(f'https://api.coingecko.com/api/v3/exchanges/{exchange}/tickers?page={p}',
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
        #df.to_csv(f'./ticker_data/{exchange}_{page_num}.csv', header=True)
        # pass coin_id from other csv       
    return(df)

a = get_exchange_tokens('gate',19)
#a.to_csv(f'./ticker_data/gate_test.csv', header=True)

gate_tokens = a.coin_id.unique().tolist()
print(len(gate_tokens))