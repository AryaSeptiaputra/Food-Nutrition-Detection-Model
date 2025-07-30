import json
from fuzzywuzzy import fuzz

class RetrieverTool:
    def __init__(self, knowledge_path: str, use_fuzzy: bool = False, threshold: int = 85):
        with open(knowledge_path, 'r', encoding='utf-8') as file:
            self.knowledge_data = json.load(file)
        self.use_fuzzy = use_fuzzy
        self.threshold = threshold

    def run(self, food_names):
        result = {}
        for input_food in food_names:
            input_food_lower = input_food.lower()
            best_match = None
            best_score = 0
            for entry in self.knowledge_data:
                name = entry.get("name", "").lower()
                if not name:
                    continue
                if self.use_fuzzy:
                    score = fuzz.ratio(input_food_lower, name)
                    if score > self.threshold and score > best_score:
                        best_score = score
                        best_match = entry
                else:
                    if input_food_lower == name:
                        best_match = entry
                        break
            if best_match:
                result[best_match["name"]] = best_match["text"]
        if result:
            return json.dumps(result, ensure_ascii=False, indent=2)
        else:
            return "No matching knowledge found."
