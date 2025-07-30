import spacy
import json
from src.tools.retriever import RetrieverTool
from src.tools.entityRecognation import FoodNERTool
from src.tools.templatePrompt import get_prompt_template
from src.tools.languageModel import LanguageModel

class BuildPipeline:
    def __init__(self):
        self.nlp = spacy.load("xx_ent_wiki_sm")
        with open(r"C:\Intrenship\Torhe Indonesia\Food Nutrition Detection\data\processed\food_knowledge_indonesian.json", "r", encoding="utf-8") as f:
            knowledge_data = json.load(f)
        self.food_names = [item["name"] for item in knowledge_data]

        self.food_ner = FoodNERTool(food_names=self.food_names, nlp=self.nlp)
        self.retriever_tool = RetrieverTool(
            knowledge_path=r"C:\Intrenship\Torhe Indonesia\Food Nutrition Detection\data\processed\food_knowledge_indonesian.json",
            use_fuzzy=True,
            threshold=85
        )
        self.prompt_template = get_prompt_template()
        self.language_model = LanguageModel()

    def pipeline_prompt_only(self, user_prompt: str):
        ner_result = self.food_ner.run(user_prompt, 85)
        food_names = [name.strip() for name in ner_result.split(",") if name.strip()]
        knowledge_result = self.retriever_tool.run(food_names)
        knowledge = knowledge_result or "No relevant information found."
        food_names_str = ", ".join(food_names) if food_names else "-"
        formatted_prompt = self.prompt_template.format(
            question=user_prompt,
            name_food=food_names_str,
            knowledge=knowledge
        )
        return self.language_model.generate(formatted_prompt)