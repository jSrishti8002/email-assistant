# Gemini client import
from google import genai # to establish contact btw gemini and python

# API key import
from config import GEMINI_API_KEY # to extract api key

# Gemini client creation
client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ask_gemini(prompt):
    try:
        # AI ko prompt bhejna
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )
        # AI ka response return karna
        return response.text
    
    except Exception as e:
        print("Error:", e)
        return "AI response could not be generated."