'''
이 코드는 엑셀 파일에 들어가야 하는 시트와 컬럼들을 정리해둔 코드입니다.

엑셀 파일 Export하여 참고한 ONE 버전 : v3.1.2
'''

# 엑셀 시트 이름
sheet_names = ['서비스거부', '정보수집', '프로토콜취약점', '서비스공격', '통계분석(프로토콜)', '통계분석(서비스)', 'MMM', 'DNS 차단', 'Ratelimit(Dynamic)', 'DDos 패턴추출', \
              'SSS (TCP)', 'SSS (UDP)', '예외Key', '패턴블럭(배포룰)', '패턴블럭(사용자정의)', 'WebCGI 공격(배포룰)', 'WebCGI 공격(사용자정의)', 'RegEx(배포룰)', 'RegEx(사용자정의)', \
              '예외IP', 'DDos 예외IP', '정책템플릿']

# 내보낼 엑셀 시트 이름(시간복잡도 문제로 집합으로 만들었다.)
export_sheet_names = {'서비스거부', '정보수집', '프로토콜취약점', '서비스공격', '통계분석(프로토콜)', '통계분석(서비스)', 'MMM', 'DNS 차단', 'Ratelimit(Dynamic)', 'DDos 패턴추출', \
                    'SSS (TCP)', 'SSS (UDP)', '예외Key', '패턴블럭(배포룰)', '패턴블럭(사용자정의)', 'WebCGI 공격(배포룰)', 'WebCGI 공격(사용자정의)', 'RegEx(배포룰)', 'RegEx(사용자정의)', \
                    '예외IP', 'DDos 예외IP', '정책템플릿'}

# 각 엑셀 시트에 있는 컬럼들
each_sheet = {
    '유효성 에러':{
        '서비스거부' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '정보수집' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '프로토콜취약점' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '서비스공격' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '오버플로우' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '통계분석(프로토콜)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '통계분석(서비스)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'MMM' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '우선순위' : {
                'index' : [],
                'change' : []
            }, 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '레이어' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'Length Control' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '패킷헤더' : {
                'index' : [],
                'change' : []
            }, 
            '마스크' : {
                'index' : [],
                'change' : []
            }, 
            'Builder' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DNS 차단' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            },
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            'DNS 타입' : {
                'index' : [],
                'change' : []
            }, 
            'URL (Ascii)' : {
                'index' : [],
                'change' : []
            }, 
            'URL (Hexa)' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'Ratelimit(Dynamic)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            'RateLimit방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            },
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '허용 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DDos 패턴추출' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '임계치' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'SSS (TCP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '비연결 패킷 차단' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임시 등록 시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : []
            }, 
            '비연결 패킷 허용 임계치' : {
                'index' : [],
                'change' : []
            }, 
            'Syn-Cookie 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'SSS (UDP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            },
            '학습모드' : {
                'index' : [],
                'change' : []
            },
            '예외 포트 사용' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : []
            },
            '비인증 차단시간' : {
                'index' : [],
                'change' : []
            },
            '인증 유지 시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 QoS' : {
                'index' : [],
                'change' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '예외Key' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '예외키' : {
                'index' : [],
                'change' : []
            }
        },
        '패턴블럭(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '패턴블럭(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'WebCGI 공격(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'WebCGI 공격(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'RegEx(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'RegEx(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'RegEx패턴' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Source Port' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Port' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DDos 예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '정책템플릿' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '템플릿명' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }
        }
    },
    '중복 에러':{
        '서비스거부' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '정보수집' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '프로토콜취약점' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '서비스공격' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '오버플로우' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '통계분석(프로토콜)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '통계분석(서비스)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'MMM' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '우선순위' : {
                'index' : [],
                'change' : []
            }, 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '레이어' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'Length Control' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '패킷헤더' : {
                'index' : [],
                'change' : []
            }, 
            '마스크' : {
                'index' : [],
                'change' : []
            }, 
            'Builder' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DNS 차단' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            },
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            'DNS 타입' : {
                'index' : [],
                'change' : []
            }, 
            'URL (Ascii)' : {
                'index' : [],
                'change' : []
            }, 
            'URL (Hexa)' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'Ratelimit(Dynamic)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            'RateLimit방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            },
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '허용 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DDos 패턴추출' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '임계치' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'SSS (TCP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '비연결 패킷 차단' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임시 등록 시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : []
            }, 
            '비연결 패킷 허용 임계치' : {
                'index' : [],
                'change' : []
            }, 
            'Syn-Cookie 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'SSS (UDP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : []
            }, 
            '비인증 차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 QoS' : {
                'index' : [],
                'change' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '예외Key' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '예외키' : {
                'index' : [],
                'change' : []
            }
        },
        '패턴블럭(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '패턴블럭(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'WebCGI 공격(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'WebCGI 공격(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'RegEx(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'RegEx(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'RegEx패턴' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Source Port' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Port' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DDos 예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '정책템플릿' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '템플릿명' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }
        }
    },
    '정상':{
        '서비스거부' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '정보수집' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '프로토콜취약점' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '서비스공격' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '오버플로우' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '통계분석(프로토콜)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '통계분석(서비스)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'MMM' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '우선순위' : {
                'index' : [],
                'change' : []
            }, 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '레이어' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'Length Control' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '패킷헤더' : {
                'index' : [],
                'change' : []
            }, 
            '마스크' : {
                'index' : [],
                'change' : []
            }, 
            'Builder' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DNS 차단' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            },
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            'DNS 타입' : {
                'index' : [],
                'change' : []
            }, 
            'URL (Ascii)' : {
                'index' : [],
                'change' : []
            }, 
            'URL (Hexa)' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'Ratelimit(Dynamic)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            'RateLimit방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            },
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '허용 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DDos 패턴추출' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '임계치' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'SSS (TCP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '비연결 패킷 차단' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임시 등록 시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : []
            }, 
            '비연결 패킷 허용 임계치' : {
                'index' : [],
                'change' : []
            }, 
            'Syn-Cookie 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'SSS (UDP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : []
            }, 
            '비인증 차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : []
            }, 
            '인증 QoS' : {
                'index' : [],
                'change' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '예외Key' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '예외키' : {
                'index' : [],
                'change' : []
            }
        },
        '패턴블럭(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '패턴블럭(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'WebCGI 공격(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'WebCGI 공격(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'RegEx(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'RegEx(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : []
            },
            '위험도' : {
                'index' : [],
                'change' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : []
            }, 
            'RegEx패턴' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Source Port' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Port' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        'DDos 예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : []
            }
        },
        '정책템플릿' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : []
            },
            '템플릿명' : {
                'index' : [],
                'change' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : []
            }
        }
    }
}

'''
# 엑셀 표에 정리하기 편하게끔 출력하기
for name in sheet_names:
    print(name, len(list(each_sheet['유효성 에러'][name].keys())), '\n', ', '.join(each_sheet['유효성 에러'][name].keys()), '\n')
'''