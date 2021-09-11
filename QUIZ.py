# QuizPermalink
# 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오.

# [조회조건]

# http://daum.net 접속

# ‘송파 헬리오시티’ 검색

# 다음 부동산 부분에 나오는 결과 정보

# [출력 결과]

# ========= 매물 1 =========

# 거래: 매매

# 면적: 84/59 (공급/전용)

# 가격: 165,000 (만원)

# 동: 214동

# 층: 고/23

# ========= 매물 2 =========
from bs4  import BeautifulSoup
import requests

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

estate = soup.find("div", attrs={"id":"estateCollTabContents"})
estate_tbl = estate.find("tbody").find_all("tr")

# 나의 풀이
for i, estate in enumerate(estate_tbl):
    # lst = estate.find_all("td")
    lst = estate.get_text().split(" ")
    lst = list(filter(None, lst))
    print(f"========= 매물 {i+1} =========\n\
거래: {lst[0]}\n\
면적: {lst[1]} (공급/전용)\n\
가격: {lst[2]} (만원)\n\
동: {lst[3]}\n\
층: {lst[4]}")
# ========= 매물 1 =========
# 거래: 매매
# 면적: 71/49 (공급/전용)
# 가격: 160,000 (만원)
# 동: 407동
# 층: 고/29
# ========= 매물 2 =========
# 거래: 월세
# 면적: 163/130 (공급/전용)
# 가격: 140,000/240 (만원)
# 동: 312동
# 층: 고/35
# ========= 매물 3 =========
# 거래: 월세
# 면적: 84/59 (공급/전용)
# 가격: 60,000/85 (만원)
# 동: 409동
# 층: 고/20
# ========= 매물 4 =========
# 거래: 월세
# 면적: 84/59 (공급/전용)
# 가격: 60,000/80 (만원)
# 동: 507동
# 층: 고/18
# ========= 매물 5 =========
# 거래: 월세
# 면적: 84/59 (공급/전용)
# 가격: 40,000/150 (만원)
# 동: 215동
# 층: 고/12
# 강의 정답
for i, estate in enumerate(estate_tbl):
    lst = estate.find_all("td")
    
    print(f"========= 매물 {i+1} =========\n\
거래: {lst[0].get_text()}\n\
면적: {lst[1].get_text()} (공급/전용)\n\
가격: {lst[2].get_text()} (만원)\n\
동: {lst[3].get_text()}\n\
층: {lst[4].get_text()}")


# 참고
# 행 정보: tr
# tr 밑에 각 정보: td
# 모든 tr을 불러와 전체 행 정보를 저장하였고 for문 이용 각 행마다 정보를 출력
# 정보는 td 태그에 나눠져 있으므로 모든 td를 불러온 후 각 td별 텍스트 정보 출력
# 이 문제에선 td 정보가 5개 였지만 좀 더 정확하게 하려면 한줄 for 등을 사용하면 좋을 듯 함
# ========= 매물 1 =========
# 거래:  매매 
# 면적:  71/49  (공급/전용)
# 가격:  160,000  (만원)
# 동:  407동 
# 층:  고/29 
# ========= 매물 2 =========
# 거래:  월세 
# 면적:  163/130  (공급/전용)
# 가격:  140,000/240  (만원)
# 동:  312동 
# 층:  고/35 
# ========= 매물 3 =========
# 거래:  월세 
# 면적:  84/59  (공급/전용)
# 가격:  60,000/85  (만원)
# 동:  409동 
# 층:  고/20 
# ========= 매물 4 =========
# 거래:  월세 
# 면적:  84/59  (공급/전용)
# 가격:  60,000/80  (만원)
# 동:  507동 
# 층:  고/18 
# ========= 매물 5 =========
# 거래:  월세 
# 면적:  84/59  (공급/전용)
# 가격:  40,000/150  (만원)
# 동:  215동 
# 층:  고/12 
# 다시 짠 정답
for i, estate in enumerate(estate_tbl):
    lst = estate.find_all("td")
    
    lst2 = [j.get_text() for j in lst]    
    
    print(f"========= 매물 {i+1} =========")
    print(f"거래: {lst2[0]}")
    print(f"면적: {lst2[1]} (공급/전용)")
    print(f"가격: {lst2[2]} (만원)")
    print(f"동: {lst2[3]}")
    print(f"층: {lst2[4]}")
#     ========= 매물 1 =========
# 거래:  매매 
# 면적:  71/49  (공급/전용)
# 가격:  160,000  (만원)
# 동:  407동 
# 층:  고/29 
# ========= 매물 2 =========
# 거래:  월세 
# 면적:  163/130  (공급/전용)
# 가격:  140,000/240  (만원)
# 동:  312동 
# 층:  고/35 
# ========= 매물 3 =========
# 거래:  월세 
# 면적:  84/59  (공급/전용)
# 가격:  60,000/85  (만원)
# 동:  409동 
# 층:  고/20 
# ========= 매물 4 =========
# 거래:  월세 
# 면적:  84/59  (공급/전용)
# 가격:  60,000/80  (만원)
# 동:  507동 
# 층:  고/18 
# ========= 매물 5 =========
# 거래:  월세 
# 면적:  84/59  (공급/전용)
# 가격:  40,000/150  (만원)
# 동:  215동 
# 층:  고/12 

# QuizPermalink
# 웹 스크래핑을 이용하여 나만의 비서를 만드시오.

# [조건]

# 네이버에서 오늘 서울의 날씨정보 가져오기

# 헤드라인 뉴스 3건 가져오기

# IT 뉴스 3건 가져오기

# 1. 네이버 날씨
from bs4  import BeautifulSoup
import requests

def weather_scrape():
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "Accept-Language":"ko-KR,ko"
    }

    # 네이버: 분당 날씨 링크
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%B6%84%EB%8B%B9+%EB%82%A0%EC%94%A8&tqi=hKuVAwprvxsssFXannwsssssszw-158329"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    weather = soup.find("div", attrs={"class":"weather_area _mainArea"})


    # 날씨 정보
    w1 = weather.find("div", attrs={"class":"main_info"})

    today_text = w1.find("p", attrs={"class":"cast_txt"}).get_text()
    today_temp = w1.find("p", attrs={"class":"info_temperature"}).get_text().strip().replace("도씨","")
    min_temp = w1.find("span", attrs={"class":"min"}).get_text()
    max_temp = w1.find("span", attrs={"class":"max"}).get_text()

    # 미세먼지 정보
    w2 = weather.find("div", attrs={"class":"sub_info"})

    dust_1 = w2.find_all("dd")[0].find("span", attrs={"class":"num"}).get_text()
    dust_2 = w2.find_all("dd")[1].find("span", attrs={"class":"num"}).get_text()

    # 강수 정보
    w3 = weather.find("div", attrs={"class":"table_info weekly _weeklyWeather"})

    rain_morning = w3.find_all("span", attrs={"class":"rain_rate"})[0].get_text().strip()
    rain_afternoon = w3.find_all("span", attrs={"class":"rain_rate"})[1].get_text().strip()


    print("[오늘의 날씨]\n")
    print(f"{today_text}")
    print(f"현재 {today_temp} (최저 {min_temp} / 최고 {max_temp})")
    print(f"오전 {rain_morning} / 오후 {rain_afternoon}\n")
    print(f"미세먼지 {dust_1}\n초미세먼지 {dust_2}")
    def head_news():
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Accept-Language":"ko-KR,ko"
        }

    # 네이버 뉴스
    url = "https://news.naver.com"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    head_news = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)

    print("[헤드라인 뉴스]")
    for i, news in enumerate(head_news):
        news_info = news.find("a")
        print(str(i+1) + ".",  news_info.get_text().strip())
        
        link = url + news_info["href"]
        print(f"링크: {link}")
        def it_news():
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
            "Accept-Language":"ko-KR,ko"
        }

    # 네이버 IT 뉴스
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    head_news = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)

    print("[IT 뉴스]")
    for i, news in enumerate(head_news):
        news_info = news.find_all("dt")[1].find("a")
        print(str(i+1) + ".",  news_info.get_text().strip())
                
        link = news_info["href"]
        print(f"링크: {link}")