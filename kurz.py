import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=B258AA39BBA7DB0504C4F806C0F4DBA4?date=23.01.2023"

res = httpx.request("GET", url)

data = res.text
rows = data.split("\n")

rows = rows[2:-1]
pprint(rows)


"""
result = amount * data['EUR']

data = {
     "EUR": 23.880,
     "USD": 21.971

}
"""
data = {}

for r in rows:
    cols = r.split('|')
    currency = cols[-2]
    rate = cols[-1]
    rate = rate.replace(",", ".")
    rate = float(rate)
    data[currency] = rate


pprint(data)

user_amount = float(input("Zadej castu CZK: "))
#user_src = "CZK"
user_target= (input("Zadej cilovou menu: "))

if user_target in ['PHP', 'JPY', 'HUF', 'THB', 'KRW', 'INR', 'ISK']:
    result = user_amount / data[user_target]
    result = round(result, 3)
    print(f"Vysledek je: {result * 100} {user_target}.")
    
if user_target in ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'DKK', 'EUR', 'GBP', 'HKD', 'ILS', 'MXN', 'MYR', 'NOK', 'NZD', 'PLN', 'RON', 'SEK', 'SGD', 'TRY', 'USD', 'XDR', 'ZAR']:
    result = user_amount / data[user_target]
    result = round(result, 3)
    print(f"Vysledek je: {result} {user_target}.")

if user_target in ['IDR']:
    result = user_amount / data[user_target]
    result = round(result, 3)
    print(f"Vysledek je: {result * 1000} {user_target}.")
    
    

