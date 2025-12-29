from fastapi import FastAPI
from models import InventoryInput, InventoryResponse, DietInput, DietResponse, AskInput
from agents.inventory_agent import InventoryAgent
from agents.diet_agent import DietAgent
from agents.manager_agent import ManagerAgent

# Create the FastAPI app
app = FastAPI(title="AI Diet & Meal Planner")

# Initialize agents
inventory_agent = InventoryAgent()
diet_agent = DietAgent()
manager_agent = ManagerAgent()


@app.get("/")
async def root():
    return {"message": "Success!"}


@app.post("/inventory", response_model=InventoryResponse)
async def inventory_endpoint(input_data: InventoryInput):
    return inventory_agent.run(input_data.items)


@app.post("/diet", response_model=DietResponse)
async def diet_endpoint(input_data: DietInput):
    return diet_agent.run(input_data.items, input_data.diet)


@app.post("/ask")
async def ask_endpoint(input_data: AskInput):
    return manager_agent.run(input_data.items, input_data.diet)
