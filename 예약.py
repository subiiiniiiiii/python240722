import pyautogui
import time
import pyperclip

# 웹 브라우저 열기 (예: Chrome)
pyautogui.hotkey('win', 'r')  # 실행 창 열기
time.sleep(1)
pyperclip.copy('chrome')  # 'chrome' 문자열을 클립보드에 복사
pyautogui.hotkey('ctrl', 'v')  # 클립보드의 내용을 붙여넣기
pyautogui.press('enter')  # Enter 키 누르기
time.sleep(3)  # 브라우저가 열릴 때까지 대기



# 잔여 좌석 페이지 열기
pyperclip.copy('https://www.dataq.or.kr/www/mypage/accept/list.do')  # 잔여 좌석 확인 페이지 URL을 클립보드에 복사
pyautogui.hotkey('ctrl', 'v')  # URL 붙여넣기
pyautogui.press('enter')  # Enter 키 누르기
time.sleep(5)  # 페이지가 로드될 때까지 대기
pyautogui.hotkey('alt', 'space','x')
time.sleep(1)
# 잔여 좌석 확인 (예시: 특정 위치 클릭 후 텍스트 확인)
pyautogui.click(750, 950)  # 잔여 좌석 정보가 있는 위치 클릭 (좌표는 실제 위치로 변경)
time.sleep(1)

# 시험 장소 변경
if True:  # 실제 조건으로 대체 (예: OCR 결과에 "잔여좌석 있음"이 포함된 경우)

    pyautogui.click(1100, 800)  # 원하는 시험 장소 선택 (좌표는 실제 위치로 변경)
    time.sleep(1)
    print("시험 장소 변경을 시도했습니다.")
    
    pyautogui.press('down')
    time.sleep(0.1)
    pyautogui.press('down')
    time.sleep(0.1)
    pyautogui.press('down')
    time.sleep(0.1)
    print("경원중학교을 시도했습니다.")
    
    pyautogui.click(1050, 440)

    pyautogui.hotkey('end')
    time.sleep(3)
    pyautogui.click(1500, 800)


print("작업 완료")
