import pandas as pd

try:
    # 엑셀 파일의 첫 번째 시트, 첫 번째 행을 읽어 컬럼명만 확인
    df = pd.read_excel('ExamBank_Master_Data_V4.0.xlsx', sheet_name=0, header=0)
    print("엑셀 파일의 컬럼명:", df.columns.tolist())
except Exception as e:
    print(f"오류 발생: {e}") 