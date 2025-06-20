import pandas as pd
import json

# 엑셀 파일 경로
excel_file = 'ExamBank_Master_Data_V4.0.xlsx'
# 생성할 JSON 파일 경로
json_file = 'simple-data-21-10.json'
# 추출할 회차
target_round = 21
# 추출할 문제 개수
num_questions = 10

try:
    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file, sheet_name=0, header=0)

    # '회차' 열이 있는지 확인
    if '회차' not in df.columns:
        raise ValueError("엑셀 시트에 '회차' 열이 없습니다.")

    # 20회차 1~10번 문제만 추출
    df_round = df[df['회차'].astype(str) == str(target_round)].head(num_questions)

    if df_round.empty:
        print(f"경고: {target_round}회차 데이터를 찾을 수 없습니다.")
        exit()

    questions = []
    for idx, row in df_round.iterrows():
        row = row.fillna('')
        question = {
            "id": row['IBEX_ID'] if 'IBEX_ID' in row else row['ID'],
            "question": row['문제+보기'],
            "answer": int(row['정답']),
            "answer_text": row['키워드']
        }
        questions.append(question)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

    print(f"성공: {json_file} 파일이 생성되었습니다. ({len(questions)}개 문제)")

except FileNotFoundError:
    print(f"오류: '{excel_file}'을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}") 