'''
이 코드는 [정책 Import] 시, [서비스 거부] 에러가 나오도록 엑셀 파일을 수정하는 코드입니다.

테스트 코드를 작성하기 위해 참고한 부분
http://175.113.83.14/issues/132408

만약, 더 추가해야 하는 부분이 있다면 댓글로 알려주시면 감사하겠습니다.
'''

import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, Font, Border, Side
from sheet_list import each_sheet

# 엑셀 파일 불러오기
file_path = 'F:/detect-policy.xlsx'  # 엑셀 파일 경로
wb = openpyxl.load_workbook(file_path)
cell_color = "FFFF80" # 바꾼 부분 표시할 바탕 색깔

for sheet_name in each_sheet:
    if sheet_name in wb.sheetnames: # 해당 시트 이름이 엑셀 파일에 있을 경우
        sheet = wb[sheet_name]  # 시트 이름 또는 인덱스로 시트 선택
    else: # 없다면
        continue # 그 다음 이어서 시작
    
    print(sheet_name)
    print(len(each_sheet[sheet_name]))
    
    # 공격명 바꿀 행 번호
    # attack_name_index = [2, 3]

    # 공격명 수정할 부분(3자리수 이상, 수정 자체 불가)
    # attack_name = ['', '수정한 부분1']
    count = 1 # 시작 기준을 변경하기 위해 만든 변수(시간복잡도 문제로 이렇게 함, 이렇게 되면 엑셀 정책 행의 순서와 딕셔너리의 순서가 같아야 정상 작동함.)
    for column_name in each_sheet[sheet_name]: # 여기서 each_sheet[sheet_name]은 각 정책의 딕셔너리를 의미한다.
        # 첫 번째 행(헤더)에서 '공격명'이 포함된 열 번호 찾기
        for col in sheet.iter_cols(count, sheet.max_column, 1, 1):  # 첫 번째 행만 검사
            # print('\n1')
            # print(col)
            # print(col[0])
            header = col[0].value
            # print(header, end=" ")
            if header and column_name in str(header):  # 헤더가 '공격명'을 포함하는지 확인
                # print(f"'공격명'이 포함된 열 번호: {col[0].column}")  # 열 번호 출력
                count += 1 # 원하는 요소를 찾아서 1 증가
                
                print('find!')
                # 숫자를 알파벳 열로 변환
                column_letter = get_column_letter(col[0].column)
                
                # print(column_letter)
                for i in range(len(each_sheet[sheet_name][column_name]['index'])):
                    # 셀 값 변경
                    sheet[f'{column_letter}{each_sheet[sheet_name][column_name]['index'][i]}'] = each_sheet[sheet_name][column_name]['change'][i]
                    
                    # 배경색 노란색으로 변경
                    yellow_fill = PatternFill(start_color=cell_color, end_color=cell_color, fill_type="solid")
                    
                    # 굵은(Bold) 글씨체
                    bold_font = Font(bold=True)
                    
                    # 테두리 설정 (두께는 thin, 색상은 검정)
                    thin_border = Border(
                        left=Side(border_style="thin", color="000000"),
                        right=Side(border_style="thin", color="000000"),
                        top=Side(border_style="thin", color="000000"),
                        bottom=Side(border_style="thin", color="000000")
                    )

                    # 셀 스타일 적용
                    cell = sheet[f'{column_letter}{each_sheet[sheet_name][column_name]['index'][i]}']
                    cell.font = bold_font         # 글자 굵게
                    cell.fill = yellow_fill       # 셀 색깔
                    cell.border = thin_border     # 테두리
                break
        else: # break에 걸리지 않으면 실행됨.(즉, count열부터 1행 끝열(데이터가 있는 가장 마지막 열)까지 해당 요소가 없으면)
            print(f"\n'{column_name}'이 포함된 열을 찾을 수 없습니다.")


# 엑셀 파일 저장
wb.save(file_path)

'''
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, Font, Border, Side
from sheet_list import each_sheet

# 엑셀 파일 불러오기
file_path = 'F:/detect-policy.xlsx'  # 엑셀 파일 경로
wb = openpyxl.load_workbook(file_path)

sheet = wb['서비스거부']  # 시트 이름 또는 인덱스로 시트 선택
cell_color = "FFFF80" # 바꾼 부분 표시할 바탕 색깔

# 공격명 바꿀 행 번호
attack_name_index = [2, 3]

# 공격명 수정할 부분(3자리수 이상, 수정 자체 불가)
attack_name = ['', '수정한 부분1']

# 첫 번째 행(헤더)에서 '공격명'이 포함된 열 번호 찾기
for col in sheet.iter_cols(1, sheet.max_column, 1, 1):  # 첫 번째 행만 검사
    header = col[0].value
    if header and '공격명' in str(header):  # 헤더가 '공격명'을 포함하는지 확인
        # print(f"'공격명'이 포함된 열 번호: {col[0].column}")  # 열 번호 출력
        # 숫자를 알파벳 열로 변환
        column_letter = get_column_letter(col[0].column)
        
        # print(column_letter)
        for i in range(len(attack_name_index)):
            # 셀 값 변경
            sheet[f'{column_letter}{attack_name_index[i]}'] = attack_name[i]
            
            # 배경색 노란색으로 변경
            yellow_fill = PatternFill(start_color=cell_color, end_color=cell_color, fill_type="solid")
            
            # 굵은(Bold) 글씨체
            bold_font = Font(bold=True)
            
            # 테두리 설정 (두께는 thin, 색상은 검정)
            thin_border = Border(
                left=Side(border_style="thin", color="000000"),
                right=Side(border_style="thin", color="000000"),
                top=Side(border_style="thin", color="000000"),
                bottom=Side(border_style="thin", color="000000")
            )

            # 셀 스타일 적용
            cell = sheet[f'{column_letter}{attack_name_index[i]}']
            cell.font = bold_font         # 글자 굵게
            cell.fill = yellow_fill       # 셀 색깔
            cell.border = thin_border     # 테두리
        break
else:
    print("'공격명'이 포함된 열을 찾을 수 없습니다.")


# 엑셀 파일 저장
wb.save(file_path)
'''

"""
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill

# 엑셀 파일 열기
wb = load_workbook('F:/detect-policy.xlsx')
sheet = wb.active

# 숫자 열 번호
column_number = 2  # B열은 2번째 열
row = 2  # 2번째 행
new_value = 'New Data'  # 새로운 값

# 숫자를 알파벳 열로 변환
column_letter = get_column_letter(column_number)

# 셀 값 변경 (예: B2 셀 값 변경)
sheet[f'{column_letter}{row}'] = new_value

# 배경색 노란색으로 변경
yellow_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
sheet[f'{column_letter}{row}'].fill = yellow_fill

# 변경사항 저장
wb.save('F:/detect-policy.xlsx')
"""

"""
import openpyxl

# 엑셀 파일 불러오기
file_path = 'F:/detect-policy.xlsx'  # 엑셀 파일 경로
wb = openpyxl.load_workbook(file_path)
sheet = wb['서비스거부']  # 시트 이름 또는 인덱스로 시트 선택

# 첫 번째 행(헤더)에서 '공격'이 포함된 열 번호 찾기
for col in sheet.iter_cols(1, sheet.max_column, 1, 1):  # 첫 번째 행만 검사
    header = col[0].value
    if header and '공격명' in str(header):  # 헤더가 '공격'을 포함하는지 확인
        print(f"'공격명'이 포함된 열 번호: {col[0].column}")  # 열 번호 출력
        break
else:
    print("'공격'이 포함된 열을 찾을 수 없습니다.")

# 특정 열의 2번째 칸 값 변경하기
column = 'B'  # 수정하려는 열 (예: 'B' 열)
row = 2       # 2번째 칸이므로 행 번호는 2
new_value = 'New Data'  # 새로운 값

# 셀 값 변경
sheet[f'{column}{row}'] = new_value

# 엑셀 파일 저장
wb.save(file_path)
"""