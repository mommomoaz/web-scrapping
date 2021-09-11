from selenium import webdriver

options= webdriver.chromeoptions()
options.headless =True
options.add.argument("windo-size=1920x1080")


browser = webdriver.Chrome()
browser.maximize_window()

url= "https://play.google.com/store/movies/new"
browser.get(url)

#스크롤 내리기
#모니터(해상도) 높이인 1080 위치로 스크롤 내리기 
browser.execute_script("window.scrollTo(0,1080")

#화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0,document.body.crollheight)")

import time
interval = 2 #2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollheight")

#반복수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight")

    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollheight")
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie_png")

import requests
from bs4 import BeautifulSoup

url="https://play.google.com/store/movies/top"
headers - {
    "User-Agent":"Mozilla/5.0(window NT 10.0; win64; x64) Applewebkit /537.36"
    "Accept-language":"ko-KR,ko"
    }

res=requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(browser.page_source,"lxml")
for movie in title
movies = soup.find_all("div",attrs={"class":"imzgtf mpg5gc"})
print(title)
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnk0zc"}).get_text()
    #할인 전 가격
    original price= movie.find("span",attrs={"class":"suzt4c djcuy"})
    if original_price:
        original price = original_price_get_text()
    else:
        print(title, : "<할인되지 않은 영화 제외> ")
        continue
    #할인된 가격
    price=movie.find("span",attrs={"class":"suzt4c djcuy"}))

    #링크
    link = movie.find("a",attrs={"class":"jc71ub"})

    print(f"제목:{title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 후 금액: {price}")
    print("링크 : " , "https//play.google.com" +링크)

    browser.quit()