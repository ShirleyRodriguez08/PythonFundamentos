import os 
import csv
import pandas as pd

def obtener_dato(path,num):

    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data = [*csv_reader]

    return data[num]['text']


def read_pandas(path):

    return pd.read_csv(path)


if __name__ == "__main__":
    path = '../data/re/short_tweets.csv'
    s = obtener_dato(106)

    print(s)