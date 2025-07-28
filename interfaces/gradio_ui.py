import gradio as gr
import json

from core.core_chat import CoreChat
from core.agent import Agent
import prompts

class GradioUI:

    def __init__(self):
        self.translated_text_history = []
        self.target_lang = "Korean"
        self.core_chat = CoreChat()
        self.agent = Agent()

        with gr.Blocks(css="footer {visibility: hidden}") as self.ui:
            title = gr.HTML("<h1 style='text-align:center'>Multi Modal Airline Assistant Chatbot</h1>")
            with gr.Row():
                chatbot = gr.Chatbot(height=500)
                translation_panel = gr.Chatbot(height=500, label=f"{self.target_lang}-Translated")
                image_output = gr.Image(height=500)
            with gr.Row():
                msg = gr.Textbox(label="Chat with our AI Assistant:", placeholder="Type here...")
                lang_selection = gr.Radio(
                    choices=["Korean", "English", "Spanish", "Japanese", "French", "German", "Chinese", "Hindi"],
                    value="Korean",
                    label="Select Translation Language",
                    min_width=30
                )
            with gr.Row():
                audio_in = gr.Audio(
                    sources=["microphone"],
                    format="mp3",
                    type="filepath"
                )
                audio_out = gr.Audio(
                    label="Assistant Voice(auto-play)",
                    type="filepath",
                    autoplay=True
                )
                clear = gr.Button("Reset The Chat")

            msg.submit(
                fn= self.user,
                inputs= [msg, chatbot],
                outputs= [msg, chatbot],
                queue=False
            ).then(
                fn= self.bot,
                inputs= [chatbot],
                outputs=[chatbot, translation_panel, image_output, audio_out]
            )
            clear.click(lambda: ([], [], None), None, [chatbot, translation_panel, image_output, audio_out], queue=False)

            lang_selection.change(
                fn=self.update_translated_lang,
                inputs=lang_selection,
                outputs=translation_panel
            )

            audio_in.change(
                fn=self.agent.invoke_transcriber,
                inputs=audio_in,
                outputs=msg
            )


    def update_translated_lang(self, choice):
        """
        Updates and refreshes the translation box label at the top with the selected langauge.
        :param choice: The language choice the user has made.
        :return: A Gradio update object that modifies the label of the translation chatbot component
        """
        self.target_lang = choice
        return gr.update(label=f"{self.target_lang}-Translated")


    def user(self, user_input, history):
        return "", history + [[user_input, None]]


    def bot(self, history):
        user_input = history[-1][0]
        bot_message, image, tts_audio_path = self.core_chat.chat(user_input, history[:-1])
        history[-1][1] = bot_message

        translated_text = self.agent.invoke_translator(
            prompts.lang_trans_sys_msg,
            user_input,
            bot_message,
            self.target_lang
        )

        try:
            translated_list = json.loads(translated_text)
            ### Pull the nested list out to be a normal list
            ### to append the flat list into the translated_text_history variable(list)
            flat_translated_list = translated_list[0]
        except (json.JSONDecodeError, IndexError):
            flat_translated_list = ["", "Translation failed"]

        self.translated_text_history.append(flat_translated_list)

        ### When image is generated, returns the image as well.
        if image:
            return history, self.translated_text_history, image, tts_audio_path
        else:
            ## When no image is found, disable the visibility on the image block
            return history, self.translated_text_history, gr.update(visible=None), tts_audio_path



