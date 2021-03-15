from gensim.summarization import keywords
import nltk
import numpy as np
import wikipedia
np.seterr(divide='ignore', invalid='ignore')


class NaturalLanguageProcessing:
    def __init__(self, s):
        self.s = s
        self.keywords_list = []  # 전체 키워드
        self.pos = []

    def reset(self, s):
        self.s = s

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
    print(natural_language_processing.get_keywords())
    print(natural_language_processing.get_pos())
