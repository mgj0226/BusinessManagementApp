import requests
from bs4 import BeautifulSoup

url = 'https://search.books.com.tw/search/query/key/python/cat/all'
r = requests.get(url)

# soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

title_tag = soup.title
# print(title_tag)
print(title_tag.string)
for tag in title_tag:
    title_str = tag.get_text().strip()
    link_str = "https:" + tag["href"]

# a_tags = soup.find_all('a')
# for tag in a_tags:
#     print(tag.get_text())
#     print("======")

attr = {'class': 'price'}
price_tags = soup.find_all('span', attrs=attr)
prices = []

for tag in price_tags:
    t = tag.get_text().strip()
    index_comma = t.find(',')
    index_dollar = t.find('元')

    if index_comma >= 0:
        price_str = t[index_comma + 2:index_dollar - 1]
    # else:
    #     index_colon = t.find(':')
    #     price_str = t[index_colon + 2:index_dollar - 1]

    prices.append(int(price_str))

# prices = prices[0:20]

print(prices)