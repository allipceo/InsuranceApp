// 23회 보험중개사 시험 샘플 문제 (5문제)
const examData = {
  "23": {
    "title": "제23회 보험중개사 자격시험",
    "questions": [
      {
        "id": "IBEX_23_001_T1_S01_001",
        "question": "보험업법상 보험중개사의 업무범위에 대한 설명으로 옳은 것은?",
        "options": [
          "보험계약의 체결을 중개하는 업무만 할 수 있다",
          "보험계약의 체결 중개 및 보험계약의 관리업무를 할 수 있다", 
          "보험금 지급업무를 직접 처리할 수 있다",
          "보험상품을 직접 개발할 수 있다"
        ],
        "answer": 2,
        "explanation": "보험업법 제176조에 따라 보험중개사는 보험계약의 체결 중개 및 보험계약의 관리업무를 할 수 있습니다."
      },
      {
        "id": "IBEX_23_002_T1_S01_002", 
        "question": "보험중개사의 등록요건에 해당하지 않는 것은?",
        "options": [
          "보험중개사 자격시험에 합격한 자",
          "금고 이상의 형을 받고 5년이 경과하지 아니한 자",
          "보험관련 업무경력이 2년 이상인 자",
          "보험중개사 교육과정을 이수한 자"
        ],
        "answer": 2,
        "explanation": "보험중개사 등록요건에 보험관련 업무경력 조건은 없습니다. 금고 이상의 형을 받고 5년이 경과하지 아니한 자는 등록이 제한됩니다."
      },
      {
        "id": "IBEX_23_003_T1_S02_003",
        "question": "보험업법상 보험회사의 의무사항으로 옳지 않은 것은?",
        "options": [
          "보험약관의 신고의무",
          "보험료율의 신고의무", 
          "임원변경의 신고의무",
          "영업방법서의 신고의무"
        ],
        "answer": 4,
        "explanation": "보험업법상 보험회사는 보험약관, 보험료율, 임원변경 등을 신고해야 하지만, 영업방법서의 신고의무는 없습니다."
      },
      {
        "id": "IBEX_23_004_T1_S03_004",
        "question": "상법상 보험계약의 성질에 대한 설명으로 옳은 것은?",
        "options": [
          "편면계약이다",
          "낙성계약이다",
          "요물계약이다", 
          "무상계약이다"
        ],
        "answer": 2,
        "explanation": "상법상 보험계약은 보험자와 보험계약자의 의사표시가 합치되면 성립하는 낙성계약입니다."
      },
      {
        "id": "IBEX_23_005_T1_S04_005",
        "question": "민법상 계약의 해제에 관한 설명으로 옳지 않은 것은?",
        "options": [
          "해제권은 상대방에 대한 의사표시로 행사한다",
          "해제는 소급적 효력을 가진다",
          "해제권의 행사는 철회할 수 있다",
          "해제로 인하여 손해배상청구권이 소멸한다"
        ],
        "answer": 4,
        "explanation": "민법상 계약의 해제로 인하여 손해배상청구권은 소멸하지 않습니다. 해제권 행사 후에도 손해배상을 청구할 수 있습니다."
      }
    ]
  }
};

// 정답 확인 함수
function checkAnswer(questionId, selectedAnswer) {
  const question = examData["23"].questions.find(q => q.id === questionId);
  return selectedAnswer === question.answer;
}

// 해설 가져오기 함수  
function getExplanation(questionId) {
  const question = examData["23"].questions.find(q => q.id === questionId);
  return question.explanation;
} 