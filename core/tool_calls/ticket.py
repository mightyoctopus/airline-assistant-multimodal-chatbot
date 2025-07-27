
class Ticket:
    def __init__(self, destination, price_data):
        self.destination = destination
        self.prices = price_data

    def get_ticket_price(self):
        print(f"Tool call for {self.destination} has been called!")
        for price in self.prices:
            if price["destination"].lower() == self.destination.lower():
                return price["price"]


get_ticket_price_func = {
    "name": "get_ticket_price",
    "description": """
        Get the ticket price info of the destination that customer wants to travel to.
        Call this function whenever you need to check the ticket price.
        For example, when a customer asks "How much is the ticket to the city?"
        or "What's the price of the ticket to {destination}?"
    """,
    "parameters": {
        "type": "object",
        "properties": {
            "destination": {
                "type": "string",
                "description": "The city that the customer wants to travel to."
            }
        },
        "required": ["destination"],
        "additionalProperties": False
    }
}