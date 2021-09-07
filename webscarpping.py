# #get, post
# import requests
# import re
# from bs4 import BeautifulSoup

# for i in range(1,6)
#     print("페이지:", i)
#      url= "https://pages.coupang.com/f/s477?from=home_C1&traid=home_C1&trcid=11079093"
# res = requests.get(url)
# res.raise_for_status
# soup = BeautifulSoup((res.text, "lxml"))

# print(res.text)

# items = soup. find_all("li", attrs={"class":re.compile("^search-product"})
# # print(items[0].find("div",attrs={"class:""name"}).get_text())

# or items in items
#     name= item. find("div",attrs={"class":"name"}).get_text() #제품명
#     price = item.find("strong", attrs={"class":"price-value"}).get_text()#가격
    
# if ad_badge:
#     print(" <평점없는 상품 제외합니다>")
#     continue

# print(name, price)
# print(f"제품명: {name}")
# print(f"가격 : {price}")
# print("바로가기:{}".format("")+link)

# import requests
# from bs4 import BeautifulSoup

# res=requests.get
# res.raise_for_status()

# soup =  BeautifulSoup(res.text,"lxml")

# images = soup.find_all("img", attrs={"class":"thumb_ing"})

# for image in images
#     image_url=image["src"]
#     if image_url.startsswithc("//"):
#         image_url = "https:" +image_url
    
#     print(image_url)
#     image_res = requests.get(image_url)\
#     image_res.raise_for_status()

#     with open("movie{}.jpg".format(idx+1),"Wb")as f:
#         f.write(image_res.content)

#csv기본

import csv
import re
import requests
from bs4 import BeautifulSoup

url= "https://finance.naver.com/sise/sise_market_sum.nhn"

for page in range(1,5):
    res= requests.get(url+str(page))
    res.raise_for_status()
    soup =BeautifulSoup(res.text)

    soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all
    for row in data_rows:
        