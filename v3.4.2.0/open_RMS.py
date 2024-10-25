'''
이 코드는 RMS를 열고, 로그인하는 코드입니다.

장비 : https://10.0.5.94
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


# Chrome 옵션 설정 (필요 시)
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')  # 신뢰할 수 없는 사이트 문구 무시
chrome_options.add_experimental_option("detach", True)  # 자동으로 꺼지지 않도록 설정
chrome_options.add_argument('--remote-debugging-port=9222') # 원하는 포트번호 지정
chrome_options.add_argument("--incognito") # 시크릿 모드로 실행하기 위한 옵션 추가
chrome_options.add_argument('--log-level=3')  # 오류만 표시, 경고 및 정보 로그 숨김

# ChromeDriver 경로 설정
driver_path = 'C:\\Users\\WINS\\Downloads\\chromedriver\\chromedriver-win64\\chromedriver.exe'

# Chrome 서비스 시작
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 아이디, 비번 불러오기
username = os.environ.get('RMS_ID')
password = os.environ.get('RMS_PW')
# print(username, password)

try:
    # 1. RMS 메인 홈 화면에 진입한다.
    driver.get('https://10.0.5.94/login')
    
    # 대기 시간 설정
    wait = WebDriverWait(driver, 10)
   
    # 2. 유효한 아이디를 입력한다.
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='mat-input-0']"))).send_keys(username)
    
    # 3. 유효한 비밀번호를 입력한다.
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='mat-input-1']"))).send_keys(password)
    
    # 4. 로그인 버튼을 탭한다.
    driver.find_element(By.XPATH, "/html/body/rms-root/rms-login/div/form/div[2]/button").click()
 
except Exception as e:
    print('  Failed to compile, exception is %s' % repr(e))