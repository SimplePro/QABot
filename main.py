from NaturalLanguage.natural_language import NaturalLanguageProcessing
import wikipedia

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
