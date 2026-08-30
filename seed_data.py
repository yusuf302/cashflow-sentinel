#!/usr/bin/env python3
import csv, random, datetime, os

# Fixed seed for reproducibility
SEED = 42
random.seed(SEED)
BASE_DATE = datetime.date(2024, 1, 1)
MONTHS = 12

# Output path
os.makedirs('data', exist_ok=True)
outfile = 'data/bakery_ledger.csv'

CHANNELS = ['M-Pesa', 'Bank', 'Cash']
CATEGORIES = {
    'sales': ['customer', 'wholesale'],
    'expense': ['inventory', 'rent', 'utilities', 'misc']
}

CUSTOMERS = ['Local Market', 'Town Hall', 'Café A', 'Cafe B', 'Wholesale Co.']
wholesale_customer = 'Wholesale Co.'

rows = []

# Helper to get a random date inside a month

def rand_day(year, month):
    start = datetime.date(year, month, 1)
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    delta = (next_month - start).days - 1
    return start + datetime.timedelta(days=random.randint(0, delta))

for m in range(1, MONTHS + 1):
    year = BASE_DATE.year
    month = BASE_DATE.month + m - 1
    if month > 12:
        year += (month - 1) // 12
        month = ((month - 1) % 12) + 1

    # Sales inflows
    num_sales = random.randint(15, 25)
    for _ in range(num_sales):
        date = rand_day(year, month)
        if random.random() < 0.20 and month <= 6:
            customer = wholesale_customer
            amount = random.randint(2000, 4000)
        else:
            customer = random.choice([c for c in CUSTOMERS if c != 'Wholesale Co.'])
            amount = random.randint(500, 1500)
        channel = random.choice(CHANNELS)
        rows.append([date.isoformat(), 'in', amount, channel, 'sales', customer, f'Sale to {customer}'])

    # Expense outflows
    base_inventory = 800
    inventory = int(base_inventory * (1 + 0.05 * (m - 1)))
    date = rand_day(year, month)
    rows.append([date.isoformat(), 'out', inventory, 'Bank', 'expense', 'inventory', 'Inventory purchase'])

    rent = 2000
    date = rand_day(year, month)
    rows.append([date.isoformat(), 'out', rent, 'Bank', 'expense', 'rent', 'Monthly rent'])

    utilities = 300
    date = rand_day(year, month)
    rows.append([date.isoformat(), 'out', utilities, 'Cash', 'expense', 'utilities', 'Utilities bill'])

    misc = int(50 * (1 + 0.10 * (m - 1)))
    date = rand_day(year, month)
    rows.append([date.isoformat(), 'out', misc, 'Cash', 'expense', 'misc', 'Miscellaneous expense'])

# Seasonal dip in month 7
rows = [r for r in rows if not (r[1] == 'in' and r[0].startswith('2024-07'))]

# Write CSV
with open(outfile, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['date', 'type', 'amount', 'channel', 'category', 'counterparty', 'description'])
    w.writerows(rows)

print(f'Generated {len(rows)} transactions to {outfile}')
