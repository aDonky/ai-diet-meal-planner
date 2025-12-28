import json
from typing import List
from services.llm_client import LLMClient
from models import DietResponse


class DietAgent:
    def __init__(self):
        self.llm = LLMClient()

    def run(self, items: List[str], diet: str) -> DietResponse:
        prompt = (
            f"You are a diet-aware kitchen assistant. Given these ingredients:\n"
            f"{json.dumps(items)}\n"
            f"And the dietary restriction: {diet}\n"
            "Return a JSON object with:\n"
            "  compatible_items: an array of ingredients from the list that are compatible with the diet,\n"
            "  suggested_recipe_ideas: an array of exactly 5 recipe ideas using those compatible ingredients.\n"
            "Respond ONLY with valid JSON."
        )
        
        result = self.llm.call_model_json(prompt)
        return DietResponse(**result)
