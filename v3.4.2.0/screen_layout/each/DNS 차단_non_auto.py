'''
이 코드는 RMS의 [DNS 차단] 화면구성(카테고리)이 ONE의 화면구성과 같은지 확인하는 코드입니다.
[운영 관리] -> [정책 관리] -> [정책 편집] -> [탐지 정책 설정] -> [DNS 차단] -> [화면구성]

장비 : https://10.0.5.94
부분 자동화 코드이기 때문에 해당 메뉴 클릭 한 번 해야 합니다.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import time
from collections import Counter

# 원하는 정책의 이름
element_name = "ONE15_sTest2"

# ONE에 있는 화면 구성 내용
original_list=['공격코드', '공격명', '행위', '차단방법', '위험도', '경보', '예외IP', 'Inbound', 'Outbound', 'TrustedIP', '공격인정횟수', '차단인정횟수', '공격인정시간', '차단시간', 'RAW', 'Flow', 'DNS타입', 'URL(Hexa)', 'URL(Ascii)', '대소문자비교', '옵셋값', '옵셋비교', '공격자축약', '대상자축약', '공격자축약(IPv6)', '대상자축약(IPv6)', '비고']

# 설정 버튼 클릭을 위한 함수 정의
def click_setting_button():
    try:
        # 설정 버튼 찾기 (parent_element 내에서 찾도록 하기)
        setting_button_xpath = f"{parent_xpath}//div[1]//button[@class='mat-mdc-menu-trigger circle_btn mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-unthemed mat-mdc-button-base']"
        setting_button = wait.until(EC.element_to_be_clickable((By.XPATH, setting_button_xpath)))
        
        # 버튼 클릭
        setting_button.click()
    
    except StaleElementReferenceException:
        print("요소가 더 이상 유효하지 않습니다. 다시 시도합니다.")
        click_setting_button()  # 재귀 호출하여 다시 시도

    except TimeoutException:
        print("설정 버튼을 찾는 데 실패했습니다.")

# DNS 차단 버튼 클릭을 위한 함수 정의
def click_DNS_button():
    try:
        # element = wait.until(lambda driver: driver.find_element(By.XPATH, "/html/body/rms-root/rms-main/div[1]/rms-policy-editing/sniper-stepper/div/div[2]/rms-editor-view/div/mat-tab-group/div/mat-tab-body[1]/div/sniper-detect-policy/div/aside/div[2]/sniper-tree2/mat-tree/mat-nested-tree-node/li/ul/mat-nested-tree-node[1]/li/ul/mat-tree-node[3]/li/button"))
        # driver.execute_script("arguments[0].click();", element)
        
        # DNS 차단 버튼 클릭하기
        DNS_xpath = "/html/body/rms-root/rms-main/div[1]/rms-policy-editing/sniper-stepper/div/div[2]/rms-editor-view/div/mat-tab-group/div/mat-tab-body[1]/div/sniper-detect-policy/div/aside/div[2]/sniper-tree2/mat-tree/mat-nested-tree-node/li/ul/mat-nested-tree-node[1]/li/ul/mat-tree-node[3]"
        DNS_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, DNS_xpath))
        )
        
        # 해당 요소로 스크롤
        driver.execute_script("arguments[0].scrollIntoView(true);", DNS_button)

        # JavaScript로 직접 클릭
        driver.execute_script("arguments[0].click();", DNS_button)
        DNS_button.click()
        
        # ActionChains를 사용해 요소의 위치로 이동 후 클릭
        # actions = ActionChains(driver)
        # actions.move_to_element(DNS_button).click().perform()
        '''
        DNS_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, DNS_xpath))
        )
        print(driver.find_element(By.XPATH, DNS_xpath).text)
        # 버튼 안의 텍스트 출력
        button_text = DNS_button.text
        print("버튼 안의 텍스트:", button_text)

        DNS_button.click()
        '''
    except StaleElementReferenceException:
        print("요소가 더 이상 유효하지 않습니다. 다시 시도합니다.")
        click_DNS_button()  # 재귀 호출하여 다시 시도

    except TimeoutException:
        print("설정 버튼을 찾는 데 실패했습니다.")
    

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

# 암묵적 대기 설정 (예: 10초)
driver.implicitly_wait(10)

try:
    print("[DNS 차단] 화면 구성 검사 시작합니다.")
    
    # 창 크기를 조정해 모든 요소를 표시
    # driver.set_window_size(3000, 2000)  # 화면에 맞게 높이를 조정
    
    # 로그인된 상태에서 작업 수행
    driver.get("https://10.0.5.94/dashboard")  # 로그인된 페이지로 이동
    
    # 대기 시간 설정
    wait = WebDriverWait(driver, 15)

    # 메뉴바 모든 버튼 불러오기
    menu_buttons = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.hd_icon_btn'))
    )

    # 상위 버튼(운영 관리) 클릭 
    menu_buttons[4].click()

    # 하위 버튼(운영 관리 -> 정책 관리) 클릭
    wait.until(
        EC.element_to_be_clickable(menu_buttons[5])
    ).click()
    
    # '사용중인 정책 보기' 옆의 휴지통 버튼을 클릭한다.
    driver.find_element(By.XPATH, "//button[@class='search_refresh_btn circle_btn mdc-button mdc-button--unelevated mat-mdc-unelevated-button mat-unthemed mat-mdc-button-base ng-star-inserted']").click()
    
    parent_xpath = f"//p[text()='{element_name}']/ancestor::h2/ancestor::div/ancestor::div[@id='policy_card']"
    # 부모 요소의 XPath 설정
    parent_xpath = f"//p[text()='{element_name}']/ancestor::h2/ancestor::div/ancestor::div[@id='policy_card']"
        
    # 설정 버튼 클릭 함수 실행
    click_setting_button()
    
    # [정책 편집] 클릭
    button_xpath = "/html/body/div[2]/div[2]/div/div/div/button[4]"
    button = wait.until(
        EC.element_to_be_clickable((By.XPATH, button_xpath))
    )
    button.click()
    
    # DNS 차단 버튼 클릭하기
    # click_DNS_button()
    
    # 화면 배율을 25%로 조정 ([DNS 차단] 버튼을 클릭하는 것보다 더 먼저 해야 모든 요소가 화면에 그려지고, 그걸 캐치할 수 있다.)
    driver.execute_script("document.body.style.zoom='25%'")
    
    '''
    # 25%로 줌 조정
    driver.execute_script("document.body.style.zoom='25%'")

    # 필요한 요소들이 로드될 때까지 기다림 (WebDriverWait 사용 가능)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/rms-root/rms-main/div[1]/rms-policy-editing/sniper-stepper/div/div[2]/rms-editor-view/div/mat-tab-group/div/mat-tab-body[1]/div/sniper-detect-policy/div/aside/div[2]/sniper-tree2/mat-tree/mat-nested-tree-node/li/ul/mat-nested-tree-node[1]/li/ul/mat-tree-node[3]")))

    # 줌을 원래대로 돌림 (100%)
    driver.execute_script("document.body.style.zoom='100%'")

    # 버튼 클릭
    element = driver.find_element(By.XPATH, "/html/body/rms-root/rms-main/div[1]/rms-policy-editing/sniper-stepper/div/div[2]/rms-editor-view/div/mat-tab-group/div/mat-tab-body[1]/div/sniper-detect-policy/div/aside/div[2]/sniper-tree2/mat-tree/mat-nested-tree-node/li/ul/mat-nested-tree-node[1]/li/ul/mat-tree-node[3]")
    element.click()

    # 클릭 후 다시 줌을 25%로 돌림
    driver.execute_script("document.body.style.zoom='25%'")
    '''
    # 10초 동안 대기
    time.sleep(10)
    
    # DNS 차단 버튼 클릭하기
    click_DNS_button()
    
    th_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'th')))
    # th_elements = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'th')))
    
    # 텍스트를 리스트에 저장
    th_texts = [th.text for th in th_elements]
    
    # 중간에 있는 공백 없애기
    cleaned_list = [s.replace(" ", "") for s in th_texts]
    
    # 화면 배율을 100%로 조정
    driver.execute_script("document.body.style.zoom='100%'")
    # print("모은 텍스트:", th_texts)
    
    # 리스트의 요소를 카운트
    counter1 = Counter(original_list)
    counter2 = Counter(cleaned_list)
    print(f"RMS 요소 개수 : {len(cleaned_list)}, ONE 요소 개수 : {len(original_list)}")
    
    
    # 두 리스트가 같다면
    if counter1 == counter2:
        print("두 리스트는 중복된 값까지 같습니다.")
    else:
        # 어떤 값이 추가되었거나, 부족한지 확인
        diff1 = counter1 - counter2  # list1에 있고 list2에는 없는 값들
        diff2 = counter2 - counter1  # list2에 있고 list1에는 없는 값들
        
        if diff1:
            for item, count in diff1.items():
                print(f"ONE에 [{item}]이(가) {count}개 더 있습니다.")
        if diff2:
            for item, count in diff2.items():
                print(f"RMS에 [{item}]이(가) {count}개 더 있습니다.")
                
    print("[DNS 차단] 화면 구성 검사가 끝났습니다.")
                
except Exception as e:
    print('  Failed to compile, exception is %s' % repr(e))
