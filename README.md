# AI Diet and Meal Planner

A multi-agent AI system using FastAPI for meal planning based on available ingredients and dietary needs.

## Project Overview

This project creates an AI Diet & Meal Planner with multiple agents:
- **Inventory Agent**: Processes and checks available food items
- **Diet Agent**: Filters ingredients based on dietary needs (vegan, keto, etc.)
- **Planner Agent**: Creates complete, ready-to-cook recipes

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload --port 8000
```

## Progress

- [x] Stage 1: Set up the playground
- [ ] Stage 2: Build the inventory and diet assistants
- [ ] Stage 3: Agents orchestration
- [ ] Stage 4: Building final recipe planner
- [ ] Stage 5: Logging and containerizing for production
