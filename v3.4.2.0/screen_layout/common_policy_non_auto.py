'''
이 코드는 RMS의 [공통정책] 화면구성(카테고리)이 ONE의 화면구성과 같은지 확인하는 코드입니다.
[운영 관리] -> [정책 관리] -> [정책 편집] -> [탐지 정책 설정] -> [공통정책] -> [화면구성]

RMS 장비 : https://10.0.5.94
ONE 장비 : 10.0.5.21 (v3.1.2)

각 메뉴를 클릭해가며 확인하는 코드입니다.
위에서부터 순서대로 클릭하며 실행시켜주세요.

※ 주의 사항
모든 컬럼 항목이 나오도록 화면 비율을 조정한 뒤 실행시킬 것.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from collections import Counter

# ONE의 항목 이름
common_policy = dict()
common_policy['프로토콜취약점'] = ['공격코드', '공격명', '행위', '차단방법', '위험도', '경보', '메일', '예외IP', 'Inbound', 'Outbound', 'TrustedIP', '공격인정횟수', '차단인정횟수', '공격인정시간', '차단시간', 'RAW', '공격자축약', '대상자축약', '공격자축약(IPv6)', '대상자축약(IPv6)', '임계치학습', '비고']
common_policy['Ratelimit(Dynamic)'] = ['공격코드', '공격명', '행위', 'RateLimit방법', '위험도', '경보', '메일', '예외IP', 'Inbound', 'Outbound', 'TrustedIP', '공격인정횟수', '허용임계치', '공격인정시간', '차단시간', 'RAW', '임계치학습', '비고']
common_policy['DDoS 패턴추출'] = ['공격코드', '공격명', '행위', '프로토콜', '임계치', '위험도', '경보', 'RAW', '예외키', '비고']
common_policy['SSS(TCP)'] = ['공격코드', '공격명', '행위', '비연결패킷차단', '프로토콜', '포트', '위험도', '경보', 'RAW', '예외IP', 'cps임계치', '임시등록시간', '인증유지시간', '학습모드', '예외포트사용', '예외포트', '비연결패킷허용임계치', 'Syn-Cookie임계치', '임계치학습', '비고']
common_policy['SSS(UDP)'] = ['공격코드', '공격명', '행위', '프로토콜', '포트', '위험도', '경보', 'RAW', '예외IP', '학습모드', '예외포트사용', '예외포트', '비인증차단시간', '인증유지시간', '인증QoS', 'cps임계치', '임계치학습', '비고']
common_policy['DNS 차단'] = ['공격코드', '공격명', '행위', '차단방법', '위험도', '경보', '예외IP', 'Inbound', 'Outbound', 'TrustedIP', '공격인정횟수', '차단인정횟수', '공격인정시간', '차단시간', 'RAW', 'Flow', 'DNS타입', 'URL(Hexa)', 'URL(Ascii)', '대소문자비교', '옵셋값', '옵셋비교', '공격자축약', '대상자축약', '공격자축약(IPv6)', '대상자축약(IPv6)', '비고']
common_policy['통계분석(프로토콜)'] = ['공격코드', '공격명', '방향', '프로토콜', '단위', '수동임계치', '자동임계치(최대)', '자동임계치(평균)', '자동임계치(최소)', '위험도', '경보', '메일', '행위', 'RAW', '임계치학습', '탐지방법', '비고']
common_policy['통계분석(서비스)'] = ['공격코드', '공격명', '방향', '프로토콜', '포트', '단위', '수동임계치', '자동임계치(최대)', '자동임계치(평균)', '자동임계치(최소)', '위험도', '경보', '메일', '행위', 'RAW', '임계치학습', '탐지방법', '비고']

# 3.1.X 이상 버전에만 있는 걸로 알고 있음.
common_policy['MMM'] = ['우선순위', '공격코드', '공격명', '행위', '레이어', '위험도', 'Inbound', 'Outbound', 'TrustedIP', 'RAW', 'LengthControl', '패킷헤더', '마스크', '비고']
# print(len(common_policy['MMM']))

# Chrome 옵션 설정 (로그인 스크립트와 동일한 사용자 데이터 디렉토리 사용)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")  # 여기에서 포트 번호 사용
chrome_options.add_argument('--ignore-certificate-errors')  # 신뢰할 수 없는 사이트 문구 무시 옵션 추가
chrome_options.add_argument('--log-level=3')  # 오류만 표시, 경고 및 정보 로그 숨김

# ChromeDriver 경로 설정
driver_path = 'C:\\Users\\WINS\\Downloads\\chromedriver\\chromedriver-win64\\chromedriver.exe'

# Chrome 서비스 시작
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 대기 시간 설정
wait = WebDriverWait(driver, 10)

# 딕셔너리의 키 값을 하나씩 반복하기
for key in common_policy.keys():
    print(f'[{key}] 화면 구성 검사 시작합니다.')
    time.sleep(5)
    th_elements = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'th')))
    # th_elements = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'th')))
    
    # 텍스트를 리스트에 저장
    th_texts = [th.text for th in th_elements]
    
    # 중간에 있는 공백 없애기
    cleaned_list = [s.replace(" ", "") for s in th_texts]
    
    # 리스트의 요소를 카운트
    counter1 = Counter(common_policy[key])
    counter2 = Counter(cleaned_list)
    print(f"RMS 요소 개수 : {len(cleaned_list)}, ONE 요소 개수 : {len(common_policy[key])}")
    
    
    # 두 리스트가 같다면
    if counter1 == counter2:
        print("PASS")
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
    
    print(f'[{key}] 화면 구성 검사가 끝났습니다.\n')
    