import os
import json
import httpx
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.1-8b-instant"

    def call_model_json(self, prompt: str) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant that always responds with valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        
        response = httpx.post(self.api_url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        
        # Parse the JSON from the response
        # Sometimes the model wraps JSON in markdown code blocks
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
        
        return json.loads(content.strip())
