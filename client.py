import os
import requests
from typing import Dict, Any

AGENT_ID = "6ufgw07yfwldddps"

class FinePrintDetective:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("AGENT_AI_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set AGENT_AI_KEY environment variable.")
        self.base_url = "https://api.agent.ai/v1/run"
        
    def scan_tos(self, text: str) -> Dict[str, Any]:
        """
        Send Terms of Service text to The Fine Print Detective agent.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "agent_id": AGENT_ID,
            "inputs": {
                "terms_of_service_text": text
            }
        }
        
        response = requests.post(self.base_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
