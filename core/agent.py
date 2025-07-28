from datetime import datetime
import os
from io import BytesIO
from PIL import Image
import base64

import prompts
import config.settings
from utils.utilities import get_current_time
from llm_clients.openai_client import OpenAIClient
from llm_clients.claude_client import ClaudeClient

class Agent:
    """
    Handles multimodal agentic models that are integrated with the main chat.
    """
    def __init__(self):
        self.openai = OpenAIClient()
        self.claude = ClaudeClient()

    ### Generate Image
    def invoke_artist(self, destination):
        image_response = self.openai.execute_openai_img_model(prompts.fetch_image_prompt(destination))
        # print("IMG RES: ", image_response)
        image_base64 = image_response.data[0].b64_json
        image = Image.open(BytesIO(base64.b64decode(image_base64)))
        return image

    ### TTS Text-To-Speech
    def invoke_talker(self, text_response):
        audio_response = self.openai.execute_openai_tts_model(text_response)

        filename = f"/tmp/tts_{get_current_time()}.mp3"
        with open(filename, "wb") as f:
            f.write(audio_response.content)

        return filename

    ### Audio to Text function -- user speech to text output
    def invoke_transcriber (self, audio_file):
        if not audio_file:
            return ""
        with open(audio_file, "rb") as audio:
            result = self.openai.execute_openai_transcribe_model(audio)
        ### Remove the temp (audio) file
        try:
            os.remove(audio_file)
        except Exception as e:
            print(f"Could not delete the temp file: {e}")

        return result


    def invoke_translator(self, sys_msg, human_msg, chatbot_msg, target_lang):
        llm_response = self.claude.execute_claude_translation_model(
            sys_msg, human_msg, chatbot_msg, target_lang
        )

        print("RESULT TRANS: ", llm_response.content[0].text)

        return llm_response.content[0].text