import pandas as pd
import os

excel_file = 'data.xlsx'  # 엑셀 파일 경로
df = pd.read_excel(excel_file)  # 엑셀 파일 읽기

for index, row in df.iterrows():
    folder_name = str(row['파일명'])  # 폴더 이름 열의 이름을 적절히 변경하세요
    folder_path = os.path.join(r'C:\Users\USER\Desktop\새 폴더', folder_name)  # 폴더를 생성할 기본 경로를 지정하세요
    os.makedirs(folder_path, exist_ok=True)  # 폴더를 생성하고 이미 존재할 경우 오류를 방지합니다.
