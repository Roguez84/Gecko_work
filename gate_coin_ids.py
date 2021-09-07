import pandas as pd
import requests

from collections import OrderedDict
from IPython.display import display
from pprint import pprint


def get_coin_list(page_number):
    coin_list = []
    response = requests.get(f'https://api.coingecko.com/api/v3/exchanges/gate/tickers?pages={page_number}',
                            headers={'Content-Type': 'application/json'})
    tickers = response.json()['tickers']
    # print(type(tickers))
    for i in range(len(tickers)):
        coin_id_info = {'coin_id': tickers[i]['coin_id']}
        coin_list.append(coin_id_info)

    df = pd.DataFrame(coin_list)
    return df.drop_duplicates(subset=['coin_id'])


def csv_writer():
    for i in range(16):
        coin_id_list = get_coin_list(str(i))
        if i == 0:
            # print(type(coin_id_list))
            coin_id_list.to_csv(f'./exchange_tickers/coin_list.csv', mode='a', header=True, index=False)
        else:
            coin_id_list.to_csv(f'./exchange_tickers/coin_list_pg{i}.csv',mode='a', header=False, index=False)


csv_writer()