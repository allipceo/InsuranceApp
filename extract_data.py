import pandas as pd
import json
import re

# 엑셀 파일 경로
excel_file = 'ExamBank_Master_Data_V4.0.xlsx'
# 생성할 JSON 파일 경로
json_file = 'simple-data-20-10.json'
# 추출할 회차
target_round = 20
# 추출할 문제 개수
num_questions = 10

def parse_question_options(text):
    if not isinstance(text, str):
        return "", ["", "", "", ""], ""

    # 옵션 구분자를 기준으로 분리
    parts = re.split(r'(①|②|③|④)', text)
    
    # 질문은 첫 번째 부분
    question = parts[0].strip()
    
    options = ["", "", "", ""]
    # 옵션 파싱
    option_map = {'①': 0, '②': 1, '③': 2, '④': 3}
    for i in range(1, len(parts), 2):
        marker = parts[i]
        content = parts[i+1].strip()
        if marker in option_map:
            options[option_map[marker]] = content

    return question, options


try:
    # 엑셀 파일 읽기
    # 첫 번째 시트를 불러오고, 첫 번째 행을 헤더로 사용
    df = pd.read_excel(excel_file, sheet_name=0, header=0)

    # '회차' 열이 있는지 확인
    if '회차' not in df.columns:
        raise ValueError("엑셀 시트에 '회차' 열이 없습니다.")

    # 특정 회차 데이터 필터링
    # '회차' 열의 데이터 타입을 문자열로 변환하여 비교
    df_round = df[df['회차'].astype(str) == str(target_round)].head(num_questions)

    if df_round.empty:
        print(f"경고: {target_round}회차 데이터를 찾을 수 없습니다.")
        exit()

    questions = []
    for index, row in df_round.iterrows():
        row = row.fillna('')
        
        # '문제+보기' 컬럼 파싱
        question_text, options_list = parse_question_options(row['문제+보기'])
        
        # 정답 데이터 타입 변환 (필요시)
        correct_answer = row['정답']
        if isinstance(correct_answer, (int, float)):
            correct_answer = int(correct_answer)

        question = {
            "id": row['ID'],
            "question": question_text,
            "options": options_list,
            "correctAnswer": correct_answer,
            "explanation": row['키워드']
        }
        questions.append(question)

    # JSON 파일로 저장
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

    print(f"성공: {json_file} 파일이 생성되었습니다. ({len(questions)}개 문제)")

except FileNotFoundError:
    print(f"오류: '{excel_file}'을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}") 