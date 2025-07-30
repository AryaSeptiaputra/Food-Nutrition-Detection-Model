from fuzzywuzzy import fuzz

class FoodNERTool:
    def __init__(self, food_names, nlp):
        self.food_names = food_names
        self.nlp = nlp

    def run(self, text: str, threshold: int = 85) -> str:
        doc = self.nlp(text)
        found = set(ent.text.lower() for ent in doc.ents if ent.label_ == "FOOD")
        for food in self.food_names:
            if food.lower() in found:
                continue
            score = fuzz.partial_ratio(food.lower(), text.lower())
            if score >= threshold:
                found.add(food)
        return ", ".join(sorted(found)) if found else "No food item found."