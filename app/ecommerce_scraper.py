import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    print("Title:", title)
    print("Price:", price)
    print("Rating:", rating)
    print("-" * 40)