from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI(title="AI Diet & Meal Planner")


@app.get("/")
async def root():
    return {"message": "Success!"}
