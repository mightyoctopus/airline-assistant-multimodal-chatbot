import json

from llm_clients.openai_client import OpenAIClient
from core.tool_calls.booking import Booking, get_book_flight_func
from core.tool_calls.company import Company, get_company_info_func
from core.tool_calls.ticket import Ticket, get_ticket_price_func
from core.agent import Agent
from dummy_data import price_data, company_data
import prompts


class CoreChat:
    def __init__(self):
        self.agent = Agent()
        self.openai = OpenAIClient()
        self.tools = [
        {"type": "function", "function": get_ticket_price_func},
        {"type": "function", "function": get_company_info_func},
        {"type": "function", "function": get_book_flight_func}
        ]

        ### Booking Data
        # Holding the latest booking details which haven't been confirmed yet
        self.last_booking_info = None
        # Confirmed bookings will be stored into booking_list
        self.booking_list = []


    ###=================== Handle Tool Calls ===========================###

    def handle_tool_call(self, message):
        """
        Process function calling message from OpenAI's response
        in order to generate a response in json.
        """
        # print("MESSAGE: ", message)

        tool_call = message.tool_calls[0]
        name = tool_call.function.name
        arguments = json.loads(message.tool_calls[0].function.arguments)
        # print("ARGUMENTS: ", arguments)
        tool_calls_id = message.tool_calls[0].id

        if name == "get_ticket_price":
            destination = arguments["destination"]
            ticket = Ticket(destination, price_data)
            price = ticket.get_ticket_price()
            content = json.dumps(
                {"destination": destination, "price": price}
            )

            response = {
                "role": "tool",
                "tool_call_id": tool_calls_id,
                "content": content
            }

            image = self.agent.invoke_artist(destination)

            return response, image

        elif name == "get_company_info":
            company_info = Company(company_data)
            company_name, location, phone = company_info.get_company_info()
            content = json.dumps(
                {
                    "company_name": company_name,
                    "location": location,
                    "phone": phone
                }
            )

        elif name == "book_flight":
            booking_data = arguments["booking"]
            booking = Booking(booking_data)
            self.last_booking_info = booking.book_flight()

            content = json.dumps(self.last_booking_info)
            # print("CONTENT JSON DUMPED: ", content)

        else:
            content = json.dumps({"error": "Unknown tool call"})

        response = {
            "role": "tool",
            "tool_call_id": tool_calls_id,
            "content": content
        }

        ### None given as the sec returned value to be consistent
        ### with the return value of the first if statement:
        ### name == "get_ticket_price"
        return response, None


    ###====================== Main Chat =========================###
    def chat(self, user_input, history):
        conversation = [
            {"role": "system", "content": prompts.main_system_message},
        ]

        for human_msg, assistant_msg in history:
            conversation.append({"role": "user", "content": human_msg})
            conversation.append({"role": "assistant", "content": assistant_msg})
        conversation.append({"role": "user", "content": user_input})

        llm_response = self.openai.execute_openai_func_call_model(conversation, self.tools)

        if llm_response.choices[0].finish_reason == "tool_calls":
            print("LLM RES: ", llm_response.choices[0])
            tool_call_message = llm_response.choices[0].message
            tool_call_response, image = self.handle_tool_call(tool_call_message)

            conversation.append(tool_call_message)
            conversation.append(tool_call_response)

            llm_response = self.openai.execute_openai_chat_model(conversation)

            reply = llm_response.choices[0].message.content
            ### Raw audio bytes which is passed to the Audio method in Gradio UI
            tts_audio_path = self.agent.invoke_talker(reply)

            print("BOOKING INFO UPDATED: ", self.last_booking_info)
            ### Booking confirmation -- look for confirmation phrase
            if self.last_booking_info and any(word in reply.lower() for word in ["booked" or "reserved"]):
                self.booking_list.append(self.last_booking_info)
                print("Booking confirmed and added: ", self.booking_list)
                self.last_booking_info = None

            return reply, image, tts_audio_path

        reply = llm_response.choices[0].message.content

        tts_audio_path = self.agent.invoke_talker(reply)
        return reply, None, tts_audio_path