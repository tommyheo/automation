import pyautogui
import time

# 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
# time.sleep(2) # 2초 정지 후 
# print(pyautogui.position())

# 3. 마우스 이동
# mac = 손쉬운 사용 vscode 사용 권한 설정
# pyautogui.moveTo(1300,240)
# pyautogui.moveTo(1300,240, 2) # 3번째 인자 => 초

# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right') # 오른쪽 마우스 클릭
# pyautogui.doubleClick() # 더블 클릭
# pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다 클릭

# 5. 마우스 드래그
# 1763,53
# 1914,50

pyautogui.moveTo(1763,53,2)
pyautogui.dragTo(1914,50)