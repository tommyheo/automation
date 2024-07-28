from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pyperclip
import pyautogui


chrome_options = webdriver.ChromeOptions()

# 브라우저 꺼짐 방지 옵션
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")


# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, '#id')
id.click()
pyperclip.copy('jyhuh8775')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.click()
pyperclip.copy('jy814092!@#')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, '#log\.login').click()
time.sleep(2)

