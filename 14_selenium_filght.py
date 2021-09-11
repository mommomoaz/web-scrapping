from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.chrome()
browser.maximize_window()

url= "https://flight.naver.com/"
browser.get(url)

#가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

#이번달 27일, 28일 선택
# browser.find_elemets_by_link_text("27")[0].click()>이번달
# browser.find_elemets_by_link_text("28")[0].click()

# browser.find_elemets_by_link_text("27")[1].click()>다음달
# browser.find_elemets_by_link_text("28")[1].click()

# 이번달 27일, 다음달 28일 선택
browser.find_elemets_by_link_text("27")[0].click()
browser.find_elemets_by_link_text("28")[1].click()

#제주도 선택
browser.find_element_by_xpath("")

#항공권 선택
browser.find_element_by_link_text("항공권 검색").click()

elem= WebDriverWait(browser,10).until(EC.presence_of_element_located((BY.XPATH,))

finally:
    browser.quit

elem= browser.find_element_by_xpath("<i class=""item_num__3R0Vz"">824,800")
print(elem.text)

