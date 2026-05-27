from google import genai

client = genai.Client(api_key="")

def classify_query(query):
    prompt = f"""
    질문을 분류하라.

    rag = 국민대학교 학교 교칙
    search = 국민대학교에 관련 돼 있지만 학칙과는 무관한것
    fail = 국민대학교 무관

    반드시 search, rag, fail 중 하나만 출력.

    질문: {query}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip().lower()


# 테스트
result = classify_query("질문입력")
print(result)