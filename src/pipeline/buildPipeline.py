import spacy
import json
from src.tools.retriever import RetrieverTool
from src.tools.entityRecognation import FoodNERTool
from src.tools.templatePrompt import get_system_template, get_prompt_template
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
        self.language_model = LanguageModel()

    def pipeline_prompt_only(self, user_prompt: str):
        ner_result = self.food_ner.run(user_prompt, 85)
        food_names = [name.strip() for name in ner_result.split(",") if name.strip()]
        knowledge_result = self.retriever_tool.run(food_names)
        knowledge = knowledge_result or "Tidak ada informasi nutrisi yang ditemukan."
        food_names_joined = ", ".join(food_names) if food_names else "-"

        # Format prompt
        system_template = get_system_template().format(
            knowledge=knowledge
        )

        prompt_template = get_prompt_template().format(
            name_food=food_names_joined,
            question=user_prompt
        )

        print(system_template)
        print(prompt_template)

        # Generate dari language model
        return self.language_model.generate( prompt_template, system_template)
