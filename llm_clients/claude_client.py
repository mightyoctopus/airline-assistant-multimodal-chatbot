from anthropic import Anthropic
from anthropic.types import MessageParam
from config.settings import CLAUDE_CONFIG

class ClaudeClient:

    def __init__(self):
        self.claude_client = Anthropic(api_key=CLAUDE_CONFIG["api_key"])
        self.claude_chat_model = CLAUDE_CONFIG["chat_model"]

    def execute_claude_translation_model(self, sys_msg, human_msg, chatbot_msg, target_lang):
        return self.claude_client.messages.create(
            model=self.claude_chat_model,
            temperature=0.5,
            max_tokens=1000,
            system=sys_msg,
            messages=[
                MessageParam(
                    role="user",
                    content=f"""
                        Translate it to {target_lang} for
                        the following conversation:
                        user: {human_msg}
                        assistant: {chatbot_msg}
        
                        into a list format. 
                        For example, 
                        [[{human_msg} translated, {chatbot_msg} translated]]
                    """.strip()
                )
            ]
        )