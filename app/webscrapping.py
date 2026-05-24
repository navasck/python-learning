import requests
from bs4 import BeautifulSoup

url = "https://www.aarong.com"


# Extract Links (<a> tags)

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

for link in links:
    print(link.get("href"))