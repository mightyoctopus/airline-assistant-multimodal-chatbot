from openai import OpenAI
from config.settings import OPENAI_CONFIG

class OpenAIClient:

    def __init__(self):
        self.openai_client = OpenAI(api_key=OPENAI_CONFIG["api_key"])
        self.openai_chat_model = OPENAI_CONFIG["chat_model"]
        self.openai_image_model = OPENAI_CONFIG["image_model"]
        self.openai_tts_model = OPENAI_CONFIG["tts_model"]
        self.openai_transcription_model =OPENAI_CONFIG["transcription_model"]

    def execute_openai_chat_model(self, conversation):
        """
        OpenAI Chat model used for regular chats
        """
        return self.openai_client.chat.completions.create(
            model=self.openai_chat_model,
            messages=conversation,
            temperature=0
        )

    def execute_openai_func_call_model(self, conversation, tools):
        """
        OpenAI Chat model used for function calling (tool calls)
        """
        return self.openai_client.chat.completions.create(
            model=self.openai_chat_model,
            messages=conversation,
            tools=tools,
            temperature=0
        )

    def execute_openai_img_model(self, prompt):
        return self.openai_client.images.generate(
            model = self.openai_image_model,
            prompt = prompt,
            size = "1024x1024",
            n=1,
            response_format="b64_json"
        )

    def execute_openai_tts_model(self, text_response):
        return self.openai_client.audio.speech.create(
            model=self.openai_tts_model,
            voice="nova",
            input=text_response
        )

    def execute_openai_transcribe_model(self, audio_file):
        return self.openai_client.audio.transcriptions.create(
            model=self.openai_transcription_model,
            file=audio_file,
            response_format="text"
        )

