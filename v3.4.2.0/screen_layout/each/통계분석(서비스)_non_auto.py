'''
이 코드는 RMS의 [통계분석(서비스)] 화면구성(카테고리)이 ONE의 화면구성과 같은지 확인하는 코드입니다.
[운영 관리] -> [정책 관리] -> [정책 편집] -> [탐지 정책 설정] -> [통계분석(서비스)] -> [화면구성]

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
original_list=['공격코드', '공격명', '방향', '프로토콜', '포트', '단위', '수동임계치', '자동임계치(최대)', '자동임계치(평균)', '자동임계치(최소)', '위험도', '경보', '메일', '행위', 'RAW', '임계치학습', '탐지방법', '비고']

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

# 통계분석(서비스) 버튼 클릭을 위한 함수 정의
def click_statistical_analysis_service_button():
    try:
        # 통계분석 버튼 클릭하기
        statistical_analysis_xpath = "/html/body/rms-root/rms-main/div[1]/rms-policy-editing/sniper-stepper/div/div[2]/rms-editor-view/div/mat-tab-group/div/mat-tab-body[1]/div/sniper-detect-policy/div/aside/div[2]/sniper-tree2/mat-tree/mat-nested-tree-node/li/ul/mat-nested-tree-node[1]/li/ul/mat-nested-tree-node[2]"
        statistical_analysis_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, statistical_analysis_xpath))
        )
        
        # 버튼 클릭
        statistical_analysis_button.click()

        '''
        try:
            xpath = "/html/body/rms-root/rms-main/div[1]/rms-policy-editing/sniper-stepper/div/div[2]/rms-editor-view/div/mat-tab-group/div/mat-tab-body[1]/div/sniper-detect-policy/div/aside/div[2]/sniper-tree2/mat-tree/mat-nested-tree-node/li/ul/mat-nested-tree-node[1]/li/ul/mat-nested-tree-node[2]/li/ul/mat-tree-node[1]"
            # 요소 찾기
            element = driver.find_element(By.XPATH, xpath)
        
            # aria-expanded 속성을 true로 설정하는 JavaScript 실행
            driver.execute_script("arguments[0].setAttribute('aria-expanded', 'true')", element)
        
            # print(f"{xpath}의 aria-expanded 속성을 true로 설정했습니다.")
        except Exception as e:
            print(f"오류 발생: {e}")

        '''
        
        ### 이 부분 이상..
        # time.sleep(10)
        # 통계분석(서비스) 버튼 클릭하기
        statistical_analysis_service_xpath = "/html/body/rms-root/rms-main/div[1]/rms-policy-editing/sniper-stepper/div/div[2]/rms-editor-view/div/mat-tab-group/div/mat-tab-body[1]/div/sniper-detect-policy/div/aside/div[2]/sniper-tree2/mat-tree/mat-nested-tree-node/li/ul/mat-nested-tree-node[1]/li/ul/mat-nested-tree-node[2]/li/ul/mat-tree-node[2]"
        statistical_analysis_service_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, statistical_analysis_service_xpath))
        )
        # print(driver.find_element(By.XPATH, statistical_analysis_service_xpath).text)
        # 버튼 안의 텍스트 출력
        # button_text = statistical_analysis_service_button.text
        # print("버튼 안의 텍스트:", button_text)

        # print(statistical_analysis_service_button)
        # 버튼 클릭
        statistical_analysis_service_button.click()
        # time.sleep(10)
    
    except StaleElementReferenceException:
        print("요소가 더 이상 유효하지 않습니다. 다시 시도합니다.")
        click_statistical_analysis_service_button()  # 재귀 호출하여 다시 시도

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
    print("[통계분석(서비스)] 화면 구성 검사 시작합니다.")
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
    
    # 통계분석(서비스) 버튼 클릭하기
    click_statistical_analysis_service_button()
    
    # 화면 배율을 25%로 조정([통계분석(서비스)] 버튼을 클릭하는 것보다 더 먼저 해야 모든 요소가 화면에 그려지고, 그걸 캐치할 수 있다.)
    driver.execute_script("document.body.style.zoom='25%'")
    
    # 10초 동안 대기
    time.sleep(10)
    
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
                
    print("[통계분석(서비스)] 화면 구성 검사가 끝났습니다.")
                
except Exception as e:
    print('  Failed to compile, exception is %s' % repr(e))
