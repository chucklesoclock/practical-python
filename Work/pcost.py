# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    with open(filename) as f: 
        rows = csv.reader(f)
        headers = next(rows)
        # headers = [name, shares, price]
        # return sum(int(row[1]) * float(row[2]) for row in rows)
        cost = 0.
        for i, row in enumerate(rows): 
            name, shares, price = row
            try: 
                shares = int(shares)
                price = float(price)
            except ValueError as e:
                print(f'Error: row {i+2}: {e}')
            else:
                cost += shares * price
        return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:.2f}')
