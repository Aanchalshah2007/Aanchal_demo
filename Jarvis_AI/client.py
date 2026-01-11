from dotenv import load_dotenv


import os
from google import genai
load_dotenv()

def ai_response(prompt: str) -> str:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
