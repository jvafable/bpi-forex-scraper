import sys

from bs4 import BeautifulSoup

html = sys.stdin.read()
soup = BeautifulSoup(html, 'html.parser')
rates_table = soup.find("table")

rates = {}
skip_header = True
for row in rates_table.find_all("tr"):
    if skip_header:
        skip_header = False
        continue

    row_data = [cell.text for cell in row.find_all("td")]
    currency = row_data[0]
    buying_rate = float(row_data[1])
    selling_rate = float(row_data[2])

    rates[currency] = {
        "Buying Rate (PHP)" : buying_rate,
        "Selling Rate (PHP)" : selling_rate
    }

print(rates)
