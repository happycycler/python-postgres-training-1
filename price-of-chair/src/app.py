import requests
from bs4 import BeautifulSoup


request = requests.get("https://www.johnlewis.com/john-lewis-partners-isaac-ergonomic-office-chair-black/p3575108")
content = request.content
soup = BeautifulSoup(content, "html.parser")
# element = soup.find("meta", {"itemprop": "price"})["content"]
element = soup.find("p", {"class": "price price--large"})
string_price = element.text.strip()

price_without_symbol = string_price[1:]

actual_price = float(price_without_symbol)
if actual_price < 300:
    print("Buy it!")
    print("The current price is {}.".format(string_price))
else:
    print("The price is too damn high!")

# https://www.johnlewis.com/john-lewis-partners-isaac-ergonomic-office-chair-black/p3575108
# https://www.johnlewis.com/john-lewis-partners-isaac-ergonomic-office-chair-black/p3575108
# <p class="price price--large">£279.00</p>

# print(element.strip())
# print(element.text.strip())
# print("{0:.2f}".format(float(string_price)))
# print(float(string_price) < 200)
