# yandex_apy.py
import requests, json, os
from dotenv import load_dotenv

load_dotenv()

directory_id = os.getenv('YANDEX_DIRECTORY_ID')
api_key = os.getenv('YANDEX_API_KEY')
api_url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
headers = {
    'Authorization': f'Api-Key {api_key}',
    'Content-Type': 'application/json'
}

data = {
  "modelUri": f"gpt://{directory_id}/yandexgpt/latest",
  "completionOptions": {
    "stream": False,
    "temperature": 0,
    "maxTokens": "200"
  },
  "messages": [
    {
      "role": "system",
      "text": "Исправь грамматические, орфографические и пунктуационные ошибки в тексте. Сохраняй исходный порядок слов."
    },
    {
      "role": "user",
      "text": "Нейросети помогают человеку работать быстрее и эффективнее но опосения что искуственный интелек заменит человека - пока преждевремены"
    }
  ]
}

response = requests.post(api_url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code} - {response.text}")