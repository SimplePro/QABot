from gensim.summarization import keywords
from nltk.tokenize import sent_tokenize
import numpy as np
from numpy.linalg import norm
np.seterr(divide='ignore', invalid='ignore')


# 코사인 유사도
def cosine_similarity(A, B):
    sim = (np.dot(A, B)) / (norm(A) * norm(B))
    return sim


class NaturalLanguageSummary:
    def __init__(self, s):
        self.s = s
        self.summary = s  # 요약 정리된 글
        self.keywords_list = []  # 전체 키워드
        self.text_vec = []  # 본문 벡터라이저
        self.sentences = []  # 본문 속 문장
        self.sentences_vec = []  # 본문 속 문장별 벡터라이저

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
            if cos_similarity >= 0.2:
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

    def get_keywords(self):
        self.keywords_list = list(keywords(self.s, lemmatize=False).split("\n"))
        return self.keywords_list


if __name__ == '__main__':
    text = """The first few times I tried kimchi it was not, I must admit, my favorite food. Then I met my Korean-American partner, Gregory, moved in with his mom — a superb cook — and within a few months I was wholly converted.
    
    These days my mouth waters at the slightest whiff of pungent, fermented cabbage and I’ll eat it with everything from fried rice to dumplings, summer rolls, or, ahem, straight out of the jar. I still have a lot to learn from Mom when it comes to kimchi-making (there are over a hundred different kinds!) but the recipe for mak kimchi, or simple kimchi, has been a great place to start.
    
    
    How To Make Easy Kimchi: Watch the Video
    WATCH
    How To Make Easy Kimchi at Home
    X
    Baechu, or napa cabbage, kimchi is made by lacto-fermentation, the same process that creates sauerkraut and traditional dill pickles. In the first stage, the cabbage is soaked in a salty brine that kills off harmful bacteria. In the second stage, the remaining Lactobacillus bacteria (the good guys!) convert sugars into lactic acid, which preserves the vegetables and gives them that wonderful, tangy flavor. (If you want to learn more about fermentation, I highly recommend The Art of Fermentation by Sandor Katz.)
    
    Post Image
    (Image credit: Emily Han)
    Product Image: KYONANO Chopsticks
    KYONANO Chopsticks
    $11
    AMAZON
    BUY NOW
    
    While questioning my Korean family and friends about kimchi, I have received all kinds of opinions. Some cooks swear by a little bit of sugar, others completely shun sweeteners. There are people who include carrots and there are people who wrinkle their noses at the idea. I’m a vegetarian and my mother-in-law happily makes fish- and shrimp-free kimchi for me, but I’m sure some would consider it blasphemy to leave out the seafood. (I like adding a bit of kelp powder for umami flavor.)
    
    This can be confusing, but I think it’s actually a good thing. It means that you and your family can make kimchi your own. Rely on your own sense of smell and taste and you’ll end up with a fine batch. Two words of caution from my mother-in-law, however: too much garlic can make the kimchi bitter, and too much ginger can make it sticky. As for the gochugaru, or red pepper powder, adjust the amount to your liking. Kimchi can be mild or fiery, it’s your choice.
    
    Gallery Image
    1 / 10
    
    
    Mak kimchi, or simple kimchi, is made with cut cabbage, radish, and scallions and a seasoned paste of red pepper, garlic, ginger, sugar, and fish sauce, salted shrimp, or kelp powder. (Image credit: Apartment Therapy)
    PRINT
     RECIPE
    COMMENTS
    35 RATINGS
    How to Make Cabbage Kimchi
    YIELD
    Makes 1 quart
    
    PREP TIME
    30 minutes to 45 minutes
    
    SHOW NUTRITION 
    INGREDIENTS
    1 medium head napa cabbage (about 2 pounds)
    1/4 cup iodine-free sea salt or kosher salt (see Recipe Notes)
    Water, preferably distilled or filtered
    1 tablespoon grated garlic (5 to 6 cloves)
    1 teaspoon grated peeled fresh ginger
    1 teaspoon granulated sugar
    2 tablepoons fish sauce or salted shrimp paste, or 3 tablespoons water
    1 to 5 tablespoons Korean red pepper flakes (gochugaru)
    8 ounces Korean radish or daikon radish, peeled and cut into matchsticks
    4 medium scallions, trimmed and cut into 1-inch pieces
    GET INGREDIENTS
    Powered by Chicory
    EQUIPMENT
    Cutting board and knife
    Large bowl
    Gloves (optional but highly recommended)
    Plate and something to weigh the kimchi down, like a jar or can of beans
    Colander
    Clean 1-quart jar with canning lid or plastic lid
    Bowl or plate to place under jar during fermentation
    INSTRUCTIONS
    Cut the cabbage. Cut the cabbage lengthwise through the stem into quarters. Cut the cores from each piece. Cut each quarter crosswise into 2-inch-wide strips.
    Salt the cabbage. Place the cabbage in a large bowl and sprinkle with the salt. Using your hands, massage the salt into the cabbage until it starts to soften a bit. Add enough water to cover the cabbage. Put a plate on top of the cabbage and weigh it down with something heavy, like a jar or can of beans. Let stand for 1 to 2 hours.
    Rinse and drain the cabbage. Rinse the cabbage under cold water 3 times. Set aside to drain in a colander for 15 to 20 minutes. Meanwhile, make the spice paste.
    Make the spice paste. Rinse and dry the bowl you used for salting. Add the garlic, ginger, sugar, and fish sauce, shrimp paste, or water and stir into a smooth paste. Stir in the gochugaru, using 1 tablespoon for mild and up to 5 tablespoons for spicy (I like about 3 1/2 tablespoons); set aside until the cabbage is ready.
    Combine the vegetables and spice paste. Gently squeeze any remaining water from the cabbage and add it to the spice paste. Add the radish and scallions.
    Mix thoroughly. Using your hands, gently work the paste into the vegetables until they are thoroughly coated. The gloves are optional here but highly recommended to protect your hands from stings, stains, and smells!
    Pack the kimchi into the jar. Pack the kimchi into a 1-quart jar. Press down on the kimchi until the brine (the liquid that comes out) rises to cover the vegetables, leaving at least 1 inch of space at the top. Seal the jar.
    Let it ferment for 1 to 5 days. Place a bowl or plate under the jar to help catch any overflow. Let the jar stand at cool room temperature, out of direct sunlight, for 1 to 5 days. You may see bubbles inside the jar and brine may seep out of the lid.
    Check it daily and refrigerate when ready. Check the kimchi once a day, opening the jar and pressing down on the vegetables with a clean finger or spoon to keep them submerged under the brine. (This also releases gases produced during fermentation.) Taste a little at this point, too! When the kimchi tastes ripe enough for your liking, transfer the jar to the refrigerator. You may eat it right away, but it's best after another week or two.
    RECIPE NOTES
    Salt: Use salt that is free of iodine and anti-caking agents, which can inhibit fermentation.
    
    Water: Chlorinated water can inhibit fermentation, so use spring, distilled, or filtered water if you can.
    
    Seafood flavor and vegetarian alternatives: Seafood gives kimchi an umami flavor. Different regions and families may use fish sauce, salted shrimp paste, oysters, and other seafood. Use about 2 tablespoons of fish sauce, salted shrimp paste, or a combination of the two. For vegetarian kimchi, I like using 3/4 teaspoon kelp powder mixed with 3 tablespoons water, or simply 3 tablespoons of water.
    
    Storage: Kimchi can be refrigerated for up to a few months. Use clean utensils each time to extract the kimchi from the jar."""

    natural_language_summary = NaturalLanguageSummary(s=text)
    print(natural_language_summary.get_summary())
    print(natural_language_summary.get_keywords())