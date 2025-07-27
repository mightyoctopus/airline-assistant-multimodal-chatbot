# Multimodal Airline Assistant Chatbot

An AI-powered multimodal chatbot that acts as a virtual assistant for airline-related queries and flight bookings. 
Built with **OpenAI's GPT-4.1 Mini**, **Claude 3.5 haiku**, and other multimodal models(TTS, transcribe model).

This app supports natural conversations with text to speech, image generation, real-time audio transcription, and automatic translation into multiple languages.

---

## Features

### Natural Language Chat
- Ask questions like "How much is a flight from Seoul to Paris?" or "Book me a ticket for tomorrow morning." (The ticket prices are from dummy data)
- Handles multiple types of user requests including booking, pricing, and company info.

### Speech-to-Text Input
- Users can speak instead of typing.
- Microphone input is transcribed using the gpt-4o-mini-transcribe model.

### Real Time Translation
- Supports translation of chatbot replies into multiple languages: Korean, English, Japanese, Spanish, French, German, Chinese, and Hindi.
- Language is selectable via a simple UI toggle.

### Image Response (Optional)
- For queries requiring visual outputs, like “Show me the destination view,” the chatbot can return AI-generated images.

### Persistent History
- Maintains a live chat history.
- Translated responses are displayed side-by-side with the original conversation.

---

## Tech Stack

- **Python 3.10+**
- **Gradio** – UI framework
- **OpenAI API** – Chat, Text-To-Speech, Speech-to-Text, and image generation
- **Anthropic API** - Claude 3.5 Haiku
- **Tool Functions**(tool calls) – Structured function calling for tasks like booking and pricing
- **Custom CoreChat Agent System** – Modular class based design for managing tools and logic

---

## 🗂️ Project Structure(Main Files)
- Core Chat Logic: 
  - core/core_chat.py 
- Multimodal Agents: 
  - core/agent.py
- Tool Calls:
  - core/tool_calls/booking.py 
  - core/tool_calls/company.py
  - core/tool_calls/ticket.py 
- LLM clients & LLM related modules: 
  - llm_clients/openai_client.py
  - llm_clients/claude_client.py
- UI: 
  - interfaces/gradio_ui.py
- Entry Point: 
  - main.py
