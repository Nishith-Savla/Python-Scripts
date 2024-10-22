import os
import requests
import pandas as pd
import csv

pd.set_option('display.max_columns', None)


def get_stock_data(url, body):
    """Fetch stock data from the API."""
    response = requests.post(url, json=body)
    data = response.json()
    return data["data"]["results"]


def rank_column(df, column_name):
    # Set negative and missing values to a large number
    df[column_name] = df[column_name].mask(
        (df[column_name].isna()) | (df[column_name] <= 0), 100000)

    # Divide the df into 10 sections based on the column and rank them from 1 to 10
    df[f'{column_name}_rank'] = pd.qcut(
        df[column_name].rank(method='first'), 10, labels=False) + 1

    return df


def save_to_csv(stocks, filename):
    """Save stock data to a CSV file."""

    keys = ["26wpct", "subindustry", "apef", "mrktCapf", "name", "divDps", "priceCfoR",
            "4wpct", "sector", "lastPrice", "ticker", "pbr", "ps", "evebitd", "5yCagrPct"]

    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        for stock in stocks:
            dict_writer.writerow(
                stock['stock']['advancedRatios'] | stock['stock']['info'])


def process_stocks(filename):
    df = pd.read_csv(filename)

    # Remove ETFs
    df = df[df['sector'] != 'ETF']

    # List of columns to rank
    columns_to_rank = ['apef', 'divDps', 'pbr', 'ps', 'evebitd', 'priceCfoR']

    # Apply the ranking function to the columns
    for column in columns_to_rank:
        df = rank_column(df, column)

    # Calculate the total rank
    rank_columns = [f'{col}_rank' for col in columns_to_rank]
    df['total_rank'] = df[rank_columns].sum(axis=1)

    # Sort the df by the total rank
    df = df.sort_values(by='total_rank', ascending=True)

    # Take the top 10% stocks
    df = df.head(int(len(df) * 0.1))

    # Sort the df by 6m momentum
    df = df.sort_values(by='26wpct', ascending=False)

    # Save the df to a new csv file
    df.to_csv('stocks_processed.csv', index=False)


def main():
    url = "https://api.tickertape.in/screener/query"
    body = {
        "match": {
            "mrktCapf": {
                "g": 500
            }
        },
        "sortBy": "mrktCapf",
        "sortOrder": -1,
        "project": [
            "subindustry",
            "mrktCapf",
            "lastPrice",
            "apef",
            "4wpct",
            "26wpct",
            "divDps",
            "pbr",
            "ps",
            "evebitd",
            "priceCfoR",
            "5yCagrPct",
        ],
        "offset": 0,
        "count": 2000,
        "sids": []
    }

    stocks = get_stock_data(url, body)

    save_to_csv(stocks, 'stocks.csv')
    process_stocks('stocks.csv')
    os.remove('stocks.csv')


if __name__ == "__main__":
    main()
