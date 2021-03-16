import wikipedia
from NaturalLanguage.topic_module import get_topic

title = input("search: ")
search = wikipedia.search(title)
for i in search:
    print(i)
index = int(input("What do you want? (Enter the desired order): ")) - 1

text = wikipedia.summary(search[index])
print(text)
topic = get_topic(text)
related_topic = [i[0] for i in topic[:3]]
print("related_topic: ", ", ".join(related_topic))
