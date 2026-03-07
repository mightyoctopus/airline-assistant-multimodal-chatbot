# Multimodal Airline Assistant Chatbot

An AI-powered multimodal assistant for airline customer service and flight-related queries.

The system integrates conversational LLM reasoning with speech input, text-to-speech output, image generation, and multilingual translation to provide an interactive travel assistant experience.

---

## System Architecture
![Multi Modal Airline Customer Service Chatbot](assets/Airline%20Chatbot.jpg)

## Demo Video
https://drive.google.com/file/d/1qrb1FjtkxlTXUutg3jFG2vDpQpxyBXA_/view?usp=sharing  

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
- **Gradio** — interactive UI framework
- **OpenAI API**
  - GPT-4.1 Mini (LLM reasoning)
  - gpt-4o-mini-transcribe (speech recognition)
  - DALL·E / image generation
  - Text-to-Speech
- **Anthropic API**
  - Claude 3.5 Haiku (translation)
- **Tool Calling**
  - structured function calls for booking, pricing, and company information
- **Custom CoreChat Agent System**
  - modular architecture for tool routing and LLM orchestration

---

## Project Structure
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
