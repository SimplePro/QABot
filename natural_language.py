from gensim.summarization import keywords
from gensim.summarization.summarizer import summarize


class NaturalLanguageProcessing:
    def __init__(self, s):
        if s is None:
            raise Exception("s must not be None.")
        self.s = s
        self.summary = ""
        self.keywords = []

    def summarizations(self):
        self.summary = summarize(self.s, ratio=0.1)
        print(self.summary)
        return self.summary

    def extract_keywords(self):
        self.keywords = list(keywords(self.s, words=10).split("\n"))
        print(self.keywords)
        return self.keywords


natural_language_processing = NaturalLanguageProcessing("As you can see, the two keywords(or keyphrases) are exactly what I would like to obtain for a paragraph like the given one. The text is exactly about keywords extraction and that is what I obtained. We now can build the graph of the text so that we can see how our words are related to each other? Then we can use this code.")
natural_language_processing.summarizations()
natural_language_processing.extract_keywords()