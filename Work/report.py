# report.py
#
# Exercise 2.4
import csv 
from pprint import pprint

def read_portfolio(filename):
    portfolio = list()
    with open(filename) as f: 
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows): 
            try: 
                holding = {
                    'name': row[0], 
                    'shares': int(row[1]), 
                    'price':float(row[2])
                    }
            except ValueError as e:
                print(f'Error: row {i+2}: {e}')
            else:
                portfolio.append(holding)
    return portfolio

def read_prices(filename='Data/prices.csv'):
    prices = dict()
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                name, price = row
                prices[name] = price
    return prices

if __name__ == "__main__":
    portfolio = read_portfolio('Data/portfolio.csv')
    pprint(portfolio)

class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('expected an integer')
        self._shares = value
    
    @property
    def cost(self):
        return self.shares * self.price
