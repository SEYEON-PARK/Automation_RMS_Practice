'''
이 코드는 정책 추가하는 코드입니다.
[운영관리] → [정책 관리] → [정책 추가]

장비 : https://10.0.5.174
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# 센서 버전
sensor_version = {1:"3.0.4", 2:"3.1.0", 3:"3.1.1", 4:"3.1.2"}

# Chrome 옵션 설정 (첫 번째 스크립트와 동일한 사용자 데이터 디렉토리 사용)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")  # 여기에서 포트 번호 사용
chrome_options.add_argument('--ignore-certificate-errors')  # 신뢰할 수 없는 사이트 문구 무시 옵션 추가
chrome_options.add_argument('--log-level=3')  # 오류만 표시, 경고 및 정보 로그 숨김

# ChromeDriver 경로 설정
driver_path = 'C:\\Users\\WINS\\Downloads\\chromedriver\\chromedriver-win64\\chromedriver.exe'

# Chrome 서비스 시작
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 로그인된 상태에서 작업 수행
    driver.get("https://10.0.5.174/dashboard")  # 로그인된 페이지로 이동
    
    # 대기 시간 설정
    wait = WebDriverWait(driver, 10)

    # 메뉴바 모든 버튼 불러오기
    menu_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.hd_icon_btn'))
    )
    print(menu_buttons)

    # 상위 버튼(운영 관리) 클릭 
    menu_buttons[4].click()
    print(len(menu_buttons))

    # 하위 버튼(운영 관리 -> 정책 관리) 클릭
    wait.until(
        EC.element_to_be_clickable(menu_buttons[5])
    ).click()

    # +(정책 추가) 버튼 클릭
    add_policy_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.mat-focus-indicator.add_btn.mat-flat-button.mat-button-base.ng-star-inserted'))
    ).click()

    # 여러 개의 input 요소 선택
    input_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".mat-input-element.mat-form-field-autofill-control.ng-invalid"))
    )
    
    # 사용자로부터 센서 버전, 정책명, 정책 설명 입력받기
    sensor_choice = int(input("센서 버전을 선택하세요. \n1) 3.0.4 \n2) 3.1.0 \n3) 3.1.1 \n4) 3.1.2 \n번호 입력: "))
    policy_name = input("정책명을 입력하세요: ")
    policy_explanation = input("정책 설명을 입력하세요: ")
    
    # mat-select 클릭하여 드롭다운 열기
    mat_select = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-select"))
    )
    print("now", len(mat_select))
    
    mat_select[2].click() # 1은 [센서 타입], 2는 [센서 버전]
    
    # 선택지들(mat-option) 불러서 리스트 mat_option_elements에 저장
    mat_option_elements = [wait.until(
        EC.presence_of_element_located((By.XPATH, f"/html/body/div[2]/div[4]/div/div/div/mat-option[{i}]/span"))
    ) for i in range(1, 5)]
    
    # 사용자가 입력한 센서 버전을 찾아 클릭(드롭다운)
    for i, mat_option_element in enumerate(mat_option_elements):
        if(mat_option_element.text == sensor_version[sensor_choice]):
            desired_option = wait.until(
               EC.element_to_be_clickable((By.XPATH, f"(/html/body/div[2]/div[4]/div/div/div/mat-option[{i+1}]/span)"))
            )
    desired_option.click()
    
    # 입력받은 정책명과 설명 input 태그에 채우기
    input_elements[0].send_keys(policy_name)  # 정책명
    input_elements[1].send_keys(policy_explanation)  # 설명
    
    # 확인 버튼 클릭
    add_policy_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'PolicyContinue'))
    ).click()


except Exception as e:
    print('  Failed to compile, exception is %s' % repr(e))
