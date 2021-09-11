from selenium import webdriver

options= webdriver.chromeoptions()
options.headless =True
options.add.argument("windo-size=1920x1080")
options.add_argument ("user_agent" :)
browser =webdriver.Chrome(options=options)
browser.maximize_window()

url="http://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
#https://whatismybrowser.com/w/AKW4JR2
detected_value = browser.find_element_by_id("detcted_value")
print(detected_value)
browser.quit


