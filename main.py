import openai
import os

# API 키를 설정합니다. 키를 프로젝트 폴더 안에 '.env' 파일에 넣어두고 읽어올 수 있습니다.
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API를 사용하기 위한 인증을 진행합니다.
openai.api_key = api_key

# 여러 질문을 리스트에 저장합니다.
questions = [
    "첫 번째 질문 내용",
    "두 번째 질문 내용",
    "세 번째 질문 내용",
]

# 각 질문에 대한 답변을 저장할 리스트를 생성합니다.
answers = []

# 각 질문에 대해 AI에게 답변을 요청합니다.
for question in questions:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"질문: {question}\n답변:",
        max_tokeㅋns=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # AI의 답변을 answers 리스트에 추가합니다.
    answer = response.choices[0].text.strip()
    answers.append(answer)

# 질문과 답변을 출력합니다.
for i, (question, answer) in enumerate(zip(questions, answers)):
    print(f"질문 {i + 1}: {question}")
    print(f"답변 {i + 1}: {answer}\n")
