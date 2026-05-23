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

def total_spent(expenses):
    return sum(e['Amount'] for e in expenses)

if __name__ == '__main__':
    expenses = load_expenses('expenses.csv')

    print('=' * 35)
    print('   EXPENSE SUMMARY')
    print('=' * 35)

    category_totals = summarize_by_category(expenses)
    for category, amount in sorted(category_totals.items()):
        print(f'  {category:<15} ${amount:>8.2f}')

    print('-' * 35)
    print(f'  TOTAL           ${total_spent(expenses):>8.2f}')
    print('=' * 35)
