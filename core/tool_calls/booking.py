
class Booking:
    def __init__(self, booking_data: dict):
        self.booking = booking_data

    def book_flight(self):
        print(f"Tool call for {self.booking} a flight has been called!")
        booking_info = {
            "name": self.booking["name"],
            "departure": self.booking["departure"],
            "destination": self.booking["destination"],
            "date": self.booking["date"],
            "num_ppl": self.booking["num_ppl"]
        }
        return booking_info


### book_flight schema
get_book_flight_func = {
    "name": "book_flight",
    "description": """
        Help a customer with the booking process, collecting customer name,
        departure & destination, flight date, and the number of people for onboarding.
        This tool call must be invoked whenever the customer asks about the booking process or
        wants to book a flight.

        For example, "May I book a flight?", "Would you help me with the booking process?",
        or "I want to book an air flight".

        When the flight booking process is completed, re-confirm the booking details 
        for example, "Your flight from Incheon to Singapore on 2025-10-08 for 2 persons under the name {name} 
        has been successfully booked." You must include the phrase: "successfully booked" in the confirmation 
        message.
    """,
    "parameters": {
        "type": "object",
        "properties": {
            "booking": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Customer name"
                    },
                    "departure": {
                        "type": "string",
                        "description": "Departure city/airport",
                    },
                    "destination": {
                        "type": "string",
                        "description": "Destination city/airport"
                    },
                    "date": {
                        "type": "string",
                        "description": "Flight date in YYYY-MM-DD"
                    },
                    "num_ppl": {
                        "type": "string",
                        "description": "Number of customers in the group"
                    },
                },
                "required": ["name", "departure", "destination", "date", "num_ppl"],
                "additionalProperties": False
            }
        },
        "required": ["booking"],
        "additionalProperties": False
    }
}