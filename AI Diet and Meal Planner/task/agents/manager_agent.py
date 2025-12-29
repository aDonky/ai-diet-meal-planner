from typing import List, Dict, Any
from agents.inventory_agent import InventoryAgent
from agents.diet_agent import DietAgent


class ManagerAgent:
    def __init__(self):
        self.inventory_agent = InventoryAgent()
        self.diet_agent = DietAgent()

    def run(self, items: List[str], diet: str) -> Dict[str, Any]:
        # Step 1: get usable items from inventory
        inventory_result = self.inventory_agent.run(items)
        usable_items = inventory_result.usable_items
        
        # Step 2: filter by diet
        diet_result = self.diet_agent.run(usable_items, diet)
        
        # return the combined result
        return {
            "usable_items": usable_items,
            "diet_filtered": diet_result.compatible_items,  # fixed!
            "suggestions": diet_result.suggested_recipe_ideas
        }
