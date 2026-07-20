import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("MODEL", "gemini-2.5-flash")
MODEL_NAME_FOR_GENERATING_ANSWERS = os.getenv("MODEL_NAME_FOR_GENERATING_ANSWERS", "gemini-2.5-flash")