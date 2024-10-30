'''
이 코드는 [정책 Import] 시, [서비스 거부] 에러가 나오도록 엑셀 파일을 수정하는 코드입니다.

테스트 코드를 작성하기 위해 참고한 부분
http://175.113.83.14/issues/132408

만약, 더 추가해야 하는 부분이 있다면 댓글로 알려주시면 감사하겠습니다.

※ 에러 정리해둔 엑셀 파일 작성 시, 주의 사항
- 정책 이름, 'Finish', 'All Finish'는 사용 불가
'''
"""
import shutil
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, Font, Border, Side
from sheet_list import each_sheet

# 엑셀 파일 불러오기
file_path = 'F:/detect-policy.xlsx'  # 엑셀 파일 경로
wb = openpyxl.load_workbook(file_path)
cell_colors = ["FFFF80", "F9D28B", "BBEBBC"]  # 바꾼 부분 표시할 바탕 색깔
file_names = ["유효성 에러 파일", "중복 에러 파일", "정상 파일"]
index_key = ['B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'A']

for file_index, (kind_of_attack, kind_of_attack_list) in enumerate(each_sheet.items()):
    # 파일 이름
    txt_file_name = f"F:/{file_names[file_index]}.txt"
    # txt 파일 열기
    txt_file = open(txt_file_name, 'w', encoding='utf-8-sig')
    
    for sheet_index, (sheet_name, value) in enumerate(kind_of_attack_list.items()):
        txt_file.write(f'{sheet_name}\n')
        
        if sheet_name in wb.sheetnames:  # 해당 시트 이름이 엑셀 파일에 있을 경우
            original_sheet = wb[sheet_name]  # 원본 시트 선택
            new_sheet = wb.copy_worksheet(original_sheet)  # 시트 복사
            
            # 복사된 시트의 이름 변경 (원하는 경우)
            new_sheet.title = sheet_name

        else:  # 시트가 없다면
            continue  # 그 다음 이어서 시작
        
        print(sheet_name)
        print(len(each_sheet[kind_of_attack][sheet_name]))
        
        count = 1  # 시작 기준을 변경하기 위한 변수
        for column_name in each_sheet[kind_of_attack][sheet_name]:  # 각 정책의 딕셔너리
            # 첫 번째 행에서 '공격명'이 포함된 열 번호 찾기
            for col in new_sheet.iter_cols(count, new_sheet.max_column, 1, 1):
                header = col[0].value
                if header and column_name in str(header):  # 헤더가 '공격명'을 포함하는지 확인
                    count += 1  # 원하는 요소를 찾아서 1 증가
                    
                    print('find!')
                    # 숫자를 알파벳 열로 변환
                    column_letter = get_column_letter(col[0].column)
                    
                    for i in range(len(each_sheet[kind_of_attack][sheet_name][column_name]['index'])):
                        # 셀 값 변경
                        new_sheet[f'{column_letter}{each_sheet[kind_of_attack][sheet_name][column_name]["index"][i]}'] = each_sheet[kind_of_attack][sheet_name][column_name]['change'][i]
                        
                        # 배경색 변경
                        yellow_fill = PatternFill(start_color=cell_colors[file_index], end_color=cell_colors[file_index], fill_type="solid")
                        
                        # 굵은(Bold) 글씨체
                        bold_font = Font(bold=True)
                        
                        # 테두리 설정
                        thin_border = Border(
                            left=Side(border_style="thin", color="000000"),
                            right=Side(border_style="thin", color="000000"),
                            top=Side(border_style="thin", color="000000"),
                            bottom=Side(border_style="thin", color="000000")
                        )

                        # 셀 스타일 적용
                        cell = new_sheet[f'{column_letter}{each_sheet[kind_of_attack][sheet_name][column_name]["index"][i]}']
                        cell.font = bold_font  # 글자 굵게
                        cell.fill = yellow_fill  # 셀 색깔
                        cell.border = thin_border  # 테두리
                        
                        # 파일에 쓰기
                        txt_file.write(f'인덱스 키 : {new_sheet[f"{index_key[sheet_index]}{each_sheet[kind_of_attack][sheet_name][column_name]["index"][i]}"].value}\n')
                    break
            else:
                print(f"\n'{column_name}'이 포함된 열을 찾을 수 없습니다.")
        
        txt_file.write('\n')

    # 다른 이름으로 저장하기
    new_file_path = f'F:/{file_names[file_index]}.xlsx'  # 새 파일 이름
    wb.save(new_file_path)  # 수정된 내용을 다른 이름으로 저장
    txt_file.close()
"""


import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, Font, Border, Side
from sheet_list import export_sheet_names, each_sheet

# 오류 사항 저장해둔 엑셀 파일 불러오기
error_file_path = 'F:/정책 Import_Export.xlsx'
error_wb = openpyxl.load_workbook(error_file_path)

# 특정 행의 마지막 열을 찾는 함수
def get_last_column_in_row(sheet, row):
    for col in range(1, sheet.max_column + 1):
        if sheet.cell(row=row, column=col).value is None:  # 값이 None인 경우
            return col - 1  # 마지막 유효한 열 반환
    return sheet.max_column  # 모든 열에 값이 있는 경우

# 모든 시트에 대해 반복
for kind_of_accack_sheet in error_wb.sheetnames:
    sheet = error_wb[kind_of_accack_sheet]  # 현재 시트 가져오기
    # A열 데이터를 'All Finish'를 만날 때까지 반복
    row = 1 # 행(1, 2, 3)
    # print(sheet.max_row)
    
    # 각 정책 찾기
    while True:
        column = 1 # 열(A, B, C)
        policy_name_cell_value = sheet.cell(row=row, column=1).value
        
        # 모든 정책 확인 시 반복 끝내기
        if policy_name_cell_value == 'All Finish':  # 'All Finish' 문자열을 만난 경우
            break
        
        # 정책 이름이 export_sheet_names에 포함되어 있는 경우
        if policy_name_cell_value in export_sheet_names:
            row += 1  # 다음 행으로 이동
            last_col = get_last_column_in_row(sheet, row)  # 현재 행에서 마지막 열 찾기

            # A열부터 현재 행의 마지막 열까지 반복
            for col in range(1, last_col + 1):
                each_policy_cell_value = sheet.cell(row=row, column=col).value  # 현재 정책 셀 값
                # print(each_policy_cell_value)  # 정책 셀 값 출력

                index = 2  # 인덱스 초기화 (여기서 인덱스는 항목의 순서를 나타냄)
                each_value_row = row + 1  # 다음 행을 지정 (현재 정책 항목의 바로 아래 행부터 시작)

                while True:  # 각 항목을 반복
                    each_value = sheet.cell(row=each_value_row, column=col).value  # 현재 행의 해당 열 값 읽기

                    if each_value == 'Finish':  # 'Finish' 문자열을 만난 경우 루프 종료
                        # print(1)
                        break

                    if each_value == 'None':  # 'None' 문자열을 None으로 변환
                        each_value = None
                    print(each_policy_cell_value)
                    # 각 시트의 데이터 구조에 정책 값 추가
                    each_sheet[kind_of_accack_sheet][policy_name_cell_value][each_policy_cell_value]['index'].append(index)
                    each_sheet[kind_of_accack_sheet][policy_name_cell_value][each_policy_cell_value]['change'].append(each_value)

                    print(f'policy_name : {each_policy_cell_value}, index : {index}, value : {each_value}')  # 인덱스와 값 출력
                    
                    index += 1  # 인덱스 증가
                    each_value_row += 1  # 다음 행으로 이동
                    
                    ''' 이렇게 하면 기준 row가 계속 바껴서 안 된다. 주석 처리!
                    # 다음 검사할 행은 현재 정책 항목이 끝난 후에 있음.
                    if each_value_row > row:  # 각 정책이 시작되는 행을 넘어간 경우
                        row = each_value_row  # 현재 행 업데이트
                    '''

                    if index > 20:  # 인덱스가 20을 초과하면 루프 종료
                        break

                
                # print(f"{row}행 {col}열: {each_policy_cell_value}")
        
        row += 1  # 다음 행으로 이동 
        
        # print(sheet.max_row)
        # 행 번호가 유효한 범위를 초과하는지 체크
        if (row > sheet.max_row):  # max_row로 현재 시트의 최대 행 수 확인
            print("최대 행을 초과했습니다. 루프를 종료합니다.")
            break
        
print(each_sheet)
    
''' 이 부분이 최종 보던 코드!
# RMS에서 [정책 Export]한 엑셀 파일 불러오기
file_path = 'F:/detect-policy.xlsx'  # 엑셀 파일 경로
wb = openpyxl.load_workbook(file_path)
cell_colors = ["FFFF80", "F9D28B", "BBEBBC"] # 바꾼 부분 표시할 바탕 색깔(각각 유효성 에러, 중복 에러, 정상 파일에 대한 색깔이다.)
file_names = ["유효성 에러 파일", "중복 에러 파일", "정상 파일"]
# index_key = ['B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'C', 'C', 'A'] # txt 파일 출력을 위해 있는 변수, 각 시트의 순서대로 인덱스 키로 나올 만한 부분을 저장한다.
# len(index_key)

for file_index, (kind_of_attack, kind_of_attack_list) in enumerate(each_sheet.items()):
    # 파일 이름
    # txt_file_name = f"F:/{file_names[file_index]}.txt"
    # txt 파일 열기
    # txt_file = open(txt_file_name, 'w', encoding='utf-8-sig')
    for sheet_index, (sheet_name, value) in enumerate(kind_of_attack_list.items()):
        # txt_file.write(f'{sheet_name}\n')
        if sheet_name in wb.sheetnames: # 해당 시트 이름이 엑셀 파일에 있을 경우
            sheet = wb[sheet_name]  # 시트 이름 또는 인덱스로 시트 선택
        else: # 없다면
            continue # 그 다음 이어서 시작
        
        print(sheet_name)
        print(len(each_sheet[kind_of_attack][sheet_name]))
        # print("시트 열 길이 : ", sheet.max_column)
        # 공격명 바꿀 행 번호
        # attack_name_index = [2, 3]

        # 공격명 수정할 부분(3자리수 이상, 수정 자체 불가)
        # attack_name = ['', '수정한 부분1']
        count = 1 # 시작 기준을 변경하기 위해 만든 변수(시간복잡도 문제로 이렇게 함, 이렇게 되면 엑셀 정책 행의 순서와 딕셔너리의 순서가 같아야 정상 작동함.)
        for column_name in each_sheet[kind_of_attack][sheet_name]: # 여기서 each_sheet[kind_of_attack][sheet_name]은 각 정책의 딕셔너리를 의미한다.
            # 첫 번째 행(헤더)에서 '공격명'이 포함된 열 번호 찾기
            for col in sheet.iter_cols(count, sheet.max_column, 1, 1):  # 첫 번째 행만 검사
                # print('\n1')
                # print(col)
                # print(col[0])
                header = col[0].value
                # print(header, end=" ")
                
                # SSS(TCP), SSS(UDP)의 '예외 포트'는 비어있을 수 없음.
                if header == '예외 포트':
                    column_letter = get_column_letter(col[0].column)
                    for i in range(2, 8):
                        sheet[f'{column_letter}{i}'] = ''
                
                if header and column_name in str(header):  # 헤더가 '공격명'을 포함하는지 확인
                    # print(f"'공격명'이 포함된 열 번호: {col[0].column}")  # 열 번호 출력
                    count += 1 # 원하는 요소를 찾아서 1 증가
                    
                    # print('find!')
                    # 숫자를 알파벳 열로 변환
                    column_letter = get_column_letter(col[0].column)
                    
                    # print(column_letter)
                    for i in range(len(each_sheet[kind_of_attack][sheet_name][column_name]['index'])):
                        # 셀 값 변경
                        sheet[f'{column_letter}{each_sheet[kind_of_attack][sheet_name][column_name]['index'][i]}'] = each_sheet[kind_of_attack][sheet_name][column_name]['change'][i]
                        
                        # 배경색 노란색으로 변경
                        yellow_fill = PatternFill(start_color=cell_colors[file_index], end_color=cell_colors[file_index], fill_type="solid")
                        
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
                        cell = sheet[f'{column_letter}{each_sheet[kind_of_attack][sheet_name][column_name]['index'][i]}']
                        cell.font = bold_font         # 글자 굵게
                        cell.fill = yellow_fill       # 셀 색깔
                        cell.border = thin_border     # 테두리
                        
                        # 파일에 쓰기
                        # txt_file.write(f'인덱스 키 : {sheet[f'{index_key[sheet_index]}{each_sheet[kind_of_attack][sheet_name][column_name]['index'][i]}'].value}\n')  # 각 줄 뒤에 줄바꿈 문자 추가
                        # txt_file.write(f'인덱스 키 : {sheet[f'{index_key[sheet_index]}{each_sheet[kind_of_attack][sheet_name][column_name]['index'][i]}'].value}, 에러 메시지 : {each_sheet[kind_of_attack][sheet_name][column_name]['error_message'][i]}\n')  # 각 줄 뒤에 줄바꿈 문자 추가      
                    break
            else: # break에 걸리지 않으면 실행됨.(즉, count열부터 1행 끝열(데이터가 있는 가장 마지막 열)까지 해당 요소가 없으면)
                print(f"\n'{column_name}'이 포함된 열을 찾을 수 없습니다.")
        
        # txt_file.write('\n')


    # 엑셀 파일 저장
    # wb.save(file_path)

    # 다른 이름으로 저장하기
    new_file_path = f'F:/{file_names[file_index]}.xlsx'  # 새 파일 이름(원하는 경로로 지정)
    wb.save(new_file_path)  # 수정된 내용을 다른 이름으로 저장
    # txt_file.close()
'''

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