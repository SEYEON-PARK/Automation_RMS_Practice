'''
이 코드는 엑셀 파일에 들어가야 하는 시트와 컬럼들을 정리해둔 코드입니다.
각 컬럼들에는 [] 시, 에러가 나도록 만드는 항목만 들어가 있습니다.
(유효성/중복 나눌지 고민 필요함.)

엑셀 파일 Export하여 참고한 ONE 버전 : v3.1.2
해당 버전이 아닌 다른 버전에서 [] 시, 수정해야 하는 값이 있을 수 있음.
Ex) v3.1.2에서는 '공격인정횟수'가 40부터여야 하는데 다른 버전에서는 '공격인정횟수'가 20부터여도 되는 경우도 있음.

전제 조건)
템플릿ID가 65534는 없다.
템플릿ID가 1은 있다.
'''
# 엑셀 시트 이름
sheet_name = ['서비스거부', '정보수집', '프로토콜취약점', '서비스공격', '통계분석(프로토콜)', '통계분석(서비스)', 'MMM', 'DNS 차단', 'Ratelimit(Dynamic)', 'DDos 패턴추출', \
              'SSS (TCP)', 'SSS (UDP)', '예외Key', '패턴블럭(배포룰)', '패턴블럭(사용자정의)', 'WebCGI 공격(배포룰)', 'WebCGI 공격(사용자정의)', 'RegEx(배포룰)', 'RegEx(사용자정의)', \
              '예외IP', 'DDos 예외IP', '정책템플릿']

# 각 엑셀 시트에 있는 컬럼들
each_sheet = {
    '유효성 에러':{
        '서비스거부' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [2, 3],
                'change' : [65534, '문자열'],
                'error_message' : ['"notExistTemplate", "template vId 65534 is not exist"', "문자열 에러(넘버여야만 함.)"]
            },
            '공격코드' : {
                'index' : [4],
                'change' : [None],
                'error_message' : ['"isRequire": "code is required."']
            }, 
            '공격명' : {
                'index' : [5],
                'change' : ['great'],
                'error_message' : [	'"uneditable": "name is uneditable."']
            }, 
            '행위' : {
                'index' : [6],
                'change' : [3],
                'error_message' : ['"isEnum": "action must be a valid enum value."']
            },
            '차단방법' : {
                'index' : [7],
                'change' : ["문자열 수정"],
                'error_message' : ['"isEnum": "action must be a valid enum value."']
            }, 
            '위험도' : {
                'index' : [8],
                'change' : [1],
                'error_message' : ['"isEnum": "risk must be a valid enum value."']
            }, 
            '경보' : {
                'index' : [9],
                'change' : ['아무거나'],
                'error_message' : ['"type": "alert must be BOOLEAN."']
            }, 
            '메일' : {
                'index' : [10],
                'change' : ['아무거나'],
                'error_message' : ['"type": "alert must be BOOLEAN."']
            }, 
            'Inbound' : {
                'index' : [11, 14, 15],
                'change' : ['아무거나', 'true', None, None],
                'error_message' : ['"isEnum": "risk must be a valid enum value."', '"relations": "outbound,trusted is required", "nullable":"outbound is not allow null."', '', '']
            }, 
            'Outbound' : {
                'index' : [12, 14, 15],
                'change' : ['아무거나', None, 'true', None],
                'error_message' : ['"isEnum": "risk must be a valid enum value."', '', '"relations": "outbound,trusted is required", "nullable":"outbound is not allow null."', '']
            }, 
            'Trusted IP' : {
                'index' : [13, 14, 15],
                'change' : ['아무거나', None, None, 'true'],
                'error_message' : ['"isEnum": "risk must be a valid enum value."', '', '', '"relations": "outbound,trusted is required", "nullable":"outbound is not allow null."']
            }, 
            'RAW' : {
                'index' : [15],
                'change' : [2],
                'error_message' : ['"isEnum": "raw must be a valid enum value."']
            }, 
            '공격인정횟수' : {
                'index' : [16, 17],
                'change' : [0, 10000001],
                'error_message' : ['"min": "nlimit must equal or greater than 1."', '"max": "nlimit must equal or less than 10000000."']
            }, 
            '차단인정횟수' : {
                'index' : [18, 19],
                'change' : [0, 10000001],
                'error_message' : ['"min": "nlimit must equal or greater than 1."', '"max": "nlimit must equal or less than 10000000."']
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
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
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '프로토콜취약점' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '서비스공격' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '오버플로우' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '통계분석(프로토콜)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '통계분석(서비스)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'MMM' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '우선순위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '레이어' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Length Control' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패킷헤더' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '마스크' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Builder' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DNS 차단' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'DNS 타입' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'URL (Ascii)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'URL (Hexa)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'Ratelimit(Dynamic)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'RateLimit방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '허용 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DDos 패턴추출' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'SSS (TCP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '비연결 패킷 차단' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임시 등록 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비연결 패킷 허용 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Syn-Cookie 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'SSS (UDP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '학습모드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '예외 포트 사용' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '비인증 차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '인증 유지 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 QoS' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '예외Key' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외키' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '패턴블럭(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '패턴블럭(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'WebCGI 공격(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'WebCGI 공격(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'RegEx(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'RegEx(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RegEx패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Port' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Port' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DDos 예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '정책템플릿' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        }
    },
    '중복 에러':{
        '서비스거부' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '정보수집' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '프로토콜취약점' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '서비스공격' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '오버플로우' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '통계분석(프로토콜)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '통계분석(서비스)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'MMM' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '우선순위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '레이어' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Length Control' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패킷헤더' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '마스크' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Builder' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DNS 차단' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'DNS 타입' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'URL (Ascii)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'URL (Hexa)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'Ratelimit(Dynamic)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'RateLimit방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '허용 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DDos 패턴추출' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'SSS (TCP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '비연결 패킷 차단' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임시 등록 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비연결 패킷 허용 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Syn-Cookie 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'SSS (UDP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비인증 차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 QoS' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '예외Key' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외키' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '패턴블럭(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '패턴블럭(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'WebCGI 공격(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'WebCGI 공격(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'RegEx(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'RegEx(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RegEx패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Port' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Port' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DDos 예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '정책템플릿' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        }
    },
    '정상':{
        '서비스거부' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '정보수집' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '프로토콜취약점' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '서비스공격' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '오버플로우' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '통계분석(프로토콜)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '통계분석(서비스)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '탐지방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '단위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '수동 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최소)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(평균)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '자동 임계치(최대)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'MMM' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '우선순위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '레이어' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Length Control' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패킷헤더' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '마스크' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Builder' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DNS 차단' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'DNS 타입' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'URL (Ascii)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'URL (Hexa)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'Ratelimit(Dynamic)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'RateLimit방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '허용 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DDos 패턴추출' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'SSS (TCP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '비연결 패킷 차단' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임시 등록 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비연결 패킷 허용 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Syn-Cookie 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'SSS (UDP)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '학습모드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트 사용' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외 포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비인증 차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 유지 시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '인증 QoS' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'cps 임계치' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '예외Key' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '예외키' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '패턴블럭(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '패턴블럭(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '포트' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Flow' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋값' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '옵셋비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '임계치학습' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'WebCGI 공격(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'WebCGI 공격(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '차단방법' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '유형' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대소문자 비교' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'RegEx(배포룰)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'RegEx(사용자정의)' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '행위' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '위험도' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '경보' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '메일' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Inbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Outbound' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Trusted IP' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RAW' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'RegEx패턴' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정횟수' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격인정시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '차단시간' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자축약' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '공격자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '대상자 축약(IPv6)' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '프로토콜' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Port' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Port' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        'DDos 예외IP' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '항목' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '공격코드' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'IP버전' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            'Source Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Source Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Network' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            'Destination Prefix' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '비고' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        },
        '정책템플릿' : {
            # 만약, 엑셀 시트 행의 순서가 바뀐다면 이 부분도 바꿔줘야 한다.
            # 각 'index' 요소 1개가 'change' 요소 1개로 매칭되어야 한다. 
            '템플릿ID' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            },
            '템플릿명' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }, 
            '방향' : {
                'index' : [],
                'change' : [],
                'error_message' : []
            }
        }
    }
}