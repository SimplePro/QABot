from gensim.summarization import keywords
from nltk.tokenize import sent_tokenize
import nltk
import numpy as np
from numpy.linalg import norm
import wikipedia
np.seterr(divide='ignore', invalid='ignore')


# 코사인 유사도
def cosine_similarity(A, B):
    sim = (np.dot(A, B)) / (norm(A) * norm(B))
    return sim


class NaturalLanguageProcessing:
    def __init__(self, s):
        self.s = s
        self.summary = s  # 요약 정리된 글
        self.keywords_list = []  # 전체 키워드
        self.text_vec = []  # 본문 벡터라이저
        self.sentences = []  # 본문 속 문장
        self.sentences_vec = []  # 본문 속 문장별 벡터라이저
        self.emotion = 0.5  # 감정
        self.pos = []

    def reset(self, s):
        self.s = s

    # 글 요약
    def get_summary(self):
        # 전체 키워드
        self.keywords_list = list(keywords(self.s, lemmatize=False).split("\n"))

        # 본문 벡터라이저
        for key in self.keywords_list:
            self.text_vec.append(self.s.count(key))

        # 본문 속 문장 구분
        self.sentences = sent_tokenize(self.s)
        # 본문 속 문장별 벡터라이저
        self.sentences_vec = [[] for _ in range(len(self.sentences))]

        for i, sentence in enumerate(self.sentences):
            for keyword in self.keywords_list:
                self.sentences_vec[i].append(sentence.count(keyword))

        # 벡터라이저된 본문과 문장으로 코사인 유사도를 측정하고, 코사인 유사도 값이 일정값 이하면 불필요한 문장으로 간주하여 제거.
        for i, sentence_vec in enumerate(self.sentences_vec):
            cos_similarity = cosine_similarity(self.text_vec, sentence_vec)
            if cos_similarity >= 0.135:
                pass
            else:
                self.summary = self.summary.replace(self.sentences[i], "")

        # 순서별로 정리.
        summary_list = sent_tokenize(self.summary)
        summary = ""
        for i, v in enumerate(summary_list):
            summary += str(i+1) + ". " + v + "\n"

        self.summary = summary

        # 반환
        return self.summary

    # 키워드
    def get_keywords(self):
        self.keywords_list = list(keywords(self.s, lemmatize=False).split("\n"))
        return self.keywords_list

    # 명사 추출
    def get_pos(self):
        words = nltk.word_tokenize(self.s)
        pos = nltk.pos_tag(words)
        self.pos = [p[0] for p in pos if p[1] in ["NN", "NNP"]]
        return self.pos


if __name__ == '__main__':
    title = input("search: ")
    search = wikipedia.search(title)
    for i in search:
        print(i)
    index = int(input("What do you want? (Enter the desired order): ")) - 1
    text = wikipedia.summary(search[index])
    natural_language_processing = NaturalLanguageProcessing(s=text)
    print(natural_language_processing.get_summary())
    print(natural_language_processing.get_keywords())
    print(natural_language_processing.get_pos())
