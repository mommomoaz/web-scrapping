import requests
from bs4 import BeautifulSoup

url= "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Jul0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Jul0121-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=CjwKCAjwhOyJBhA4EiwAEcJdcZQGm9vfzkxTqokYRtFtWsuvE1feEiu-ZcGbX4F5OXYkGuJN8Tg62BoCeuoQAvD_BwE&gclsrc=aw.ds"
res = requests.get(url)
res.raise_for_status()
soup= BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
print(len)