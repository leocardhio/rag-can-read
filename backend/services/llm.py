from fastapi import HTTPException
from config import get_settings
import requests
import json

class LLMService():
  def __init__(self):
    self.llm_model_name = get_settings().llm_model_name
    self.llm_base_url = get_settings().llm_base_url
    self.llm_api_key = get_settings().llm_api_key
    
  def _generate_headers(self):
    headers = {
      "Content-Type": "application/json",
    }
    
    if self.llm_api_key:
      headers["Authorization"] = f"Bearer {self.llm_api_key}"
      
    return headers
  
  def __process_response(self, response):
    raw_response = ""
    for line in response.iter_lines():
      if line:
        line_data = json.loads(line.decode('utf-8'))
        raw_response += line_data.get('response', '')
        
    return raw_response

  async def generate(self, prompt: str) -> str:
    try:
      response = requests.post(
        url=f"{self.llm_base_url}/api/generate",
        headers=self._generate_headers(),
        json={
          "model": self.llm_model_name,
          "prompt": prompt,
          "stream": True
        },
        stream=True
      )
      
      response.raise_for_status()
          
      return self.__process_response(response)
    except requests.RequestException as e:
      print(f"Error generating response from LLM: {e}")
      raise HTTPException(status_code=500, detail="Failed to generate response from LLM")