
class Company:

    def __init__(self, company_info):
        self.company_info = company_info

    def get_company_info(self):
        print("Tool call for company info has been called!")
        company_name = self.company_info["company_name"]
        location = self.company_info["location"]
        phone = self.company_info["phone"]

        return company_name, location, phone


get_company_info_func = {
    "name": "get_company_info",
    "description": """
        Get the company information whenever the customer asks about either 
        company name, location, or contact(phone) info. 
        For example, when a customer asks "What's the name of the company?"
        or "What's the contact information? I need to talk on the phone",
        You can check on this function to retrieve the correct company information.
    """,
    "parameters": {
        "type": "object",
        "properties": {},
        "additionalProperties": False
    }
}

