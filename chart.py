import csv
from collections import defaultdict

def load_expenses(filename):
    expenses = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['Amount'] = float(row['Amount'])
            expenses.append(row)
    return expenses

def summarize_by_category(expenses):
    totals = defaultdict(float)
    for e in expenses:
        totals[e['Category']] += e['Amount']
    return dict(totals)

expenses = load_expenses('expenses.csv')
totals = summarize_by_category(expenses)

categories = list(totals.keys())
amounts = list(totals.values())

print('Category Spending Chart')
print('=' * 40)
for category, amount in sorted(totals.items()):
    bar = '#' * int(amount / 5)
    print(f'{category:<15} {bar} ')
print('=' * 40)
print('(Each # represents  spent)')
