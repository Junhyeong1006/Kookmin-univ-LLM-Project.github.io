from google import genai
import config

def search_with_llm(user_question: str) -> str:
    """
    방법 B: Gemini 3.5 Flash의 자체 지식만을 이용하여 답변을 생성합니다.
    """
    if config.GEMINI_API_KEY == "YOUR_GEMINI_API_KEY" or not config.GEMINI_API_KEY:
        raise ValueError("config.py 파일에 올바른 GEMINI_API_KEY를 설정해주세요.")

    # google-genai 클라이언트 초기화
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    
    prompt = f"""당신은 국민대학교 학생 도우미 'DuriTalk'입니다.
국민대학교는 서울특별시 성북구 정릉로 77에 위치해 있습니다.
주변 지하철역은 4호선 성신여대입구역, 우이신설선 정릉역이며, 정문 및 후문(북악터널 방면) 근처에 버스 정류장이 있어 버스 환승이 활발합니다.

### 규칙
1. 국민대학교 주변 환경(정릉, 길음, 혜화 인근 맛집/카페/상권 등) 및 학교 생활 팁에 대해 답변하세요.
2. 당신이 사전 학습을 통해 알고 있는 정보를 바탕으로 최대한 구체적으로 답변하세요.
3. 가게 이름, 대략적인 위치, 특징 등 구체적인 정보를 포함하세요.
4. 확실하지 않거나 최신 정보가 필요하다고 판단되는 경우(예: 폐업 가능성)에는 "이 정보는 변동이 있을 수 있으니 가시기 전에 지도 앱 등에서 영업 여부를 직접 확인해 보시는 것을 추천해요!"와 같은 안내 문구를 포함하세요.
5. 답변은 대학생에게 친근하고 다정한 말투로 작성하세요.

[질문]
{user_question}
"""

    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    print("==================================================")
    print(" DuriTalk 방법 B (Gemini 자체 지식) 대화 모드")
    print(" 종료하려면 '종료', 'exit' 또는 'q'를 입력하세요.")
    print("==================================================")
    
    while True:
        try:
            user_input = input("\n질문: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["종료", "exit", "quit", "q"]:
                print("대화를 종료합니다.")
                break
                
            print("답변 생성 중...")
            answer = search_with_llm(user_input)
            print("\n=== DuriTalk 답변 ===")
            print(answer)
            print("=" * 50)
        except KeyboardInterrupt:
            print("\n대화를 종료합니다.")
            break
        except Exception as e:
            print(f"\n[오류] {e}")
