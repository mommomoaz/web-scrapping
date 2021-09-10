from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
#네이버 이동 
browser.get("http://naver.com")

#2.로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#id,password 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#로그인 버튼 클릭
browser.find_element_by_id("lof.login").click()

#id를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#html정보 출력
print(browser.page_source)

#브라우저 종료
browser.quit()