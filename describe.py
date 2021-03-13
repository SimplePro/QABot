# SuperSmartQABot 전체적인 로직
# ------------------
# - 상대가 질문을 하면 그에 대한 검색내용을 핵심키워드, 핵심문장, 분야와 함께 학습한다.
#
# - 학습데이터가 크기가 일정 크기를 넘어가면 오래된 데이터순으로 삭제한다. (사람의 성향은 바뀌기 때문에, 오래전 데이터를 반영할 필요가 없기 때문이다.)
#
# - 질문자의 관심분야를 학습하여, 관심분야 지표도 보여준다.
#
# - 질문을 받을 때마다 단어의 분야들을 학습하여. 질문자의 주 분야를 분석하고, 추후에 질문을 하면 단어들을 분야순위로 정렬하여 보여준다.
# 참고: https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0
#
# 예)
# 질문자 관심분야
# 1순위: Computer Science
# 2순위: Animal
# 3순위: Food
#
# 질문: Python
# 1. Python (programming language)
# 2. Python
# 3. Monty Python
# 4. PYTHON
# .
# .
# .

print("Hello, World!")
