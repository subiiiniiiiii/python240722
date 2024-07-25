#web2.py
import requests
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# <div class="card-desc">
#       <h2 class="card-title">제습기</h2>
#       <div class="card-price ">
#         9,000원
#       </div>
#       <div class="card-region-name">
#         부산 부산진구 범전동
#       </div>


posts = soup.find_all("div",attrs={"class":"card-desc"}) 
f = open("dangn.txt","a+",encoding="utf-8")
for post in posts:
    titleElem = post.find("h2",attrs={"class":"card-title"})
    priceElem = post.find("div",attrs={"class":"card-price"})
    addrElem = post.find("div",attrs={"class":"card-region-name"})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip()
    print(f"{title}, {price} ,{addr}")
    f.write(f"{title}, {price} ,{addr}\n")

f.close()