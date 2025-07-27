import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_CONFIG = {
    "api_key": os.getenv("OPENAI_API_KEY"),
    "chat_model": "gpt-4.1-mini",
    "image_model": "dall-e-3",
    "tts_model": "tts-1",
    "transcription_model": "gpt-4o-mini-transcribe",
}

CLAUDE_CONFIG = {
    "api_key": os.getenv("ANTHROPIC_API_KEY"),
    "chat_model": "claude-3-5-haiku-latest"
}
