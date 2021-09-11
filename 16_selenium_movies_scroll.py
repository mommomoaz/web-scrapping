from selenium import webdriver
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