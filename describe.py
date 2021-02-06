# SuperSmartQABot 전체적인 로직
# ------------------
# 1. 학습은 json 파일로 학습함
# - question, keywords, key_sentences, answer, used_date 등등 저장함.

# 2. 질문을 받음
# - 질문에 대한 대답을 이미 알고 있다면, 대답
# - 질문에 대한 대답을 알고 있지 않다면, 검색한 후에 학습하고, 대답

# SuperSmartQABot 기술
# -------------
# 1. shout  find
# - 일일히 찾아보는 것이 아님.
# - Shouter 역할이 신호를 보내면, 데이터(객체)가 반응을 하여 데이터를 반환하는 기술이다.
# - 직접 손수 만들어야 함.
# - https://github.com/SimplePro/SuperSmartQABot/blob/main/Shout%20Find.pdf

# 2. 글의 종류 확인
# - 글의 형태로 글의 종류를 확인하는 기술
# - 알고리즘이나 인공지능으로 만들 것임.

print("Hello, World!")
