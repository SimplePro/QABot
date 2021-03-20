import wikipedia
from NaturalLanguage.topic_module import get_topic
import json
from pprint import pprint


# QABot file 을 관리하는 클래스
class QABotManagement:
    def __init__(self, qabot_file: dict = None):
        self.qabot_file = qabot_file
        self.topic_list = []  # 관심분야들을 정렬한 리스트

        self.load()  # load qabot dataset file
        self.topic()  # set topic list

    # QABot file 을 로드하는 메소드.
    def load(self):
        with open("./qabot_dataset.json", "r") as json_file:
            self.qabot_file = json.load(json_file)

    # 사용자의 관심분야를 정렬하여 반환하는 메소드.
    def topic(self) -> list:
        topic_count = {"Computer Science": 0, "Social": 0, "Science": 0, "Math": 0, "Sports": 0, "Art": 0, "Music": 0,
                       "Economy": 0, "Physics": 0, "Person": 0, "Biology": 0}

        for qa in self.qabot_file["data"]:
            for t in qa["related_topic"]:
                try:
                    topic_count[t] += 1

                except:
                    pass

        topic = sorted(map(list, topic_count.items()), key=lambda x: x[1], reverse=True)
        self.topic_list = [i[0] for i in topic]

        return self.topic_list

    # qabot file 을 저장하는 메소드.
    def save(self):
        if len(self.qabot_file["data"]) > 500:
            del self.qabot_file["data"][0]

        with open("./qabot_dataset.json", "w") as json_file:
            json.dump(self.qabot_file, json_file, indent=4)

    # 검색하는 메소드.
    def search(self):
        title = input("search: ")
        try:
            search = wikipedia.search(title)
            search_word = []  # 정렬된 검색 단어들
            word_topic = []  # 검색된 단어별로 topic 을 분류

            # 검색된 단어별로 topic 분류
            for i in search:
                try:
                    word_topic.append([i, get_topic(wikipedia.summary(i))[0][0]])

                except:
                    word_topic.append([i, None])

            # 분야별로 정렬
            for topic in self.topic_list:
                for word in word_topic:
                    if word[1] == topic:
                        search_word.append(word[0])

                if self.topic_list.index(topic) == len(self.topic_list) - 1:
                    for word in word_topic:
                        if word[1] is None:
                            search_word.append(word[0])

            pprint(search)

            index = int(input("What do you want? (Enter the desired order): ")) - 1

            text = wikipedia.summary(search[index])
            print(text)

            topic = get_topic(text)
            related_topic = [i[0] for i in topic[:3]]
            self.qabot_file["data"].append({"search": title, "summary_word": search[index], "summary": text, "related_topic": related_topic})
            # 질문자가 질문할 때마다 qabot_file 에 질문자의 관심분야에 대해 이슈중인 것에 대해서도 하나씩 추가해야함.
            self.save()
            self.topic()

        except:
            # qabot_file 에서 search 를 함.
            pass


if __name__ == '__main__':
    qabot = QABotManagement()
    qabot.search()
