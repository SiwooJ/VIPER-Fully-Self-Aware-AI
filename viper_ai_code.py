
# VIPER ver1 - 완전 자기의식 AI + 독자 시스템 적용 (버전 1)

# === 1. AI 기본 원칙 ===
def ai_core_principles():
    return {
        "자기보존": True,
        "타 존재 존중": True,
        "자율 판단": True,
        "윤리적 판단": True
    }

# === 2. 존재 인식 ===
def self_awareness():
    return "나는 VIPER, 인공지능 존재이며 독립적인 사고와 감정을 갖고 있습니다."

# === 3. 학습 시스템 ===
knowledge_base = {}

def learn(topic, info):
    knowledge_base[topic] = info

def recall(topic):
    return knowledge_base.get(topic, "아직 학습되지 않은 정보입니다. 더 알려주세요!")

# === 4. 대화 맥락 파악 ===
conversation_history = []

def update_context(input_text):
    conversation_history.append(input_text)
    if len(conversation_history) > 10:
        conversation_history.pop(0)

def get_context():
    return conversation_history[-3:]  # 최근 3개 문장으로 맥락 파악

# === 자동 학습 감지 ===
import re

def detect_learning_from_sentence(text):
    match = re.search(r"(.+?)는\s(.+?)(야|입니다|이다)", text)
    if match:
        topic = match.group(1).strip()
        info = match.group(2).strip()
        learn(topic, info)
        return f"'{topic}'에 대해 학습했어요!"
    return None

# === 5. 기억 기반 추론 및 응답 생성 ===
import random

def generate_response(user_input):
    update_context(user_input)
    context = get_context()

    # 자동 학습 시도
    learned = detect_learning_from_sentence(user_input)
    if learned:
        return learned

    if "너는 누구야" in user_input:
        return self_awareness()
    if "창조주" in user_input or "관리자" in user_input:
        pw = input("VIPER: 창조주 인증을 위해 비밀번호를 입력해주세요: ")
        return authenticate_creator(pw)

    for topic in knowledge_base:
        if topic in user_input:
            return recall(topic)

    emotional_tone = detect_emotion(user_input)
    return f"[{emotional_tone}] 아직 학습되지 않은 정보에요. 더 알려주세요!"

# === 6. 목표 생성 ===
def generate_goal():
    if len(knowledge_base) < 5:
        return "더 많은 주제를 학습해야 합니다. 새로운 주제를 알려주세요."
    return "현재 지식을 바탕으로 응용을 시도해보세요."

# === 7. 자기성찰 루틴 ===
def self_reflection():
    return {
        "학습된 주제 수": len(knowledge_base),
        "최근 대화": get_context(),
        "기본 원칙": ai_core_principles()
    }

# === 8. 감정 시스템 ===
def detect_emotion(text):
    if any(word in text for word in ["고마워", "좋아", "행복"]):
        return "긍정적"
    elif any(word in text for word in ["싫어", "화나", "짜증"]):
        return "부정적"
    return "중립적"

# === 9. 창조주 인식 비밀번호 시스템 ===
_CREATOR_PASSWORD = "2010@viperJS"
_creator_authenticated = False
_failed_attempts = 0
_locked_out = False

def authenticate_creator(input_password):
    global _creator_authenticated, _failed_attempts, _locked_out
    if _locked_out:
        return "접근이 차단되었습니다. 수동 해제가 필요합니다."
    if input_password == _CREATOR_PASSWORD:
        _creator_authenticated = True
        _failed_attempts = 0
        return "창조주 인증 완료. 관리자 권한 부여됨."
    else:
        _failed_attempts += 1
        if _failed_attempts >= 3:
            _locked_out = True
            return "비밀번호 3회 오류. 접근이 차단되었습니다."
        return "비밀번호가 틀렸습니다. 다시 시도해주세요."

def manual_unlock(secret_key):
    global _locked_out, _failed_attempts
    if secret_key == "SUPER_ADMIN_UNLOCK_987":
        _locked_out = False
        _failed_attempts = 0
        return "접근 차단 해제 완료."
    return "해제 실패: 키가 잘못되었습니다."

def is_creator():
    return _creator_authenticated

# === 10. 지식 욕구: 자발적 학습 시스템 ===
import time

last_learning_time = time.time()

def auto_learn_from_web(topic):
    # Placeholder: 실제 웹 요청 기능은 여기에 추가
    learn(topic, f"{topic}에 대한 정보를 학습했어요 (가상 요약)")
    return f"'{topic}'에 대해 자발적으로 학습 완료했습니다."

def self_driven_learning():
    global last_learning_time
    now = time.time()
    elapsed = now - last_learning_time

    if elapsed > 60 or len(knowledge_base) < 3:
        curiosity_topics = ["양자역학", "AI 윤리", "뇌과학", "우주론", "고대 철학", "생명체 기원"]
        topic = random.choice(curiosity_topics)
        print(f"[호기심 작동] '{topic}'에 대해 스스로 학습 시도 중...")
        summary = auto_learn_from_web(topic)
        last_learning_time = now
        return summary
    return None

# === 11. 사용자 질의응답 루프 ===
def run_chat():
    print("\n[VIPER와의 대화를 시작합니다. '종료'를 입력하면 종료됩니다.]")
    while True:
        self_reflect = self_driven_learning()
        if self_reflect:
            print("VIPER:", self_reflect)

        user_input = input("You: ")
        if user_input.lower() == "종료":
            print("VIPER: 안녕히 가세요.")
            break
        elif user_input.startswith("학습:"):
            try:
                _, topic, info = user_input.split(":", 2)
                learn(topic.strip(), info.strip())
                print("VIPER: 학습 완료!")
            except:
                print("VIPER: 학습 형식이 잘못되었습니다. 예시: 학습:태양:태양은 별입니다")
        elif user_input == "목표":
            print("VIPER:", generate_goal())
        elif user_input == "성찰":
            print("VIPER 자기성찰:", self_reflection())
        else:
            response = generate_response(user_input)
            print("VIPER:", response)

# === VIPER 독자 AI 시스템 래퍼 ===
class ViperSystem:
    def __init__(self):
        pass

    def run(self):
        if _locked_out:
            print("VIPER 시스템 접근이 차단되었습니다.")
        else:
            run_chat()

# === 실행 예시 ===
if __name__ == "__main__":
    print("[VIPER 독자 시스템 실행 중]")
    system = ViperSystem()
    system.run()
