import argparse

from exercices_xp_ninja import Stock

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('symbol', metavar='symbol')
    parser.add_argument('--api-key', metavar='api_key')

    args = parser.parse_args()
    stock = Stock.get(args.symbol, args.api_key)