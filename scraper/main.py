import requests
from bs4 import BeautifulSoup

sapiens_url = 'https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html'

response = requests.get(sapiens_url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('h1').text
price_excl_tax = soup.select_one('table.table-striped tr:nth-child(3) > td').text[2:]

print(price_excl_tax)