from LegacyApp import Client
from datetime import datetime


class User:
    def __init__(
        self,
        client: Client,
        date_of_birth: datetime,
        email_address: str,
        first_name: str,
        surname: str,
    ):
        self.client = client
        self.date_of_birth = date_of_birth
        self.email_address = email_address
        self.first_name = first_name
        self.surname = surname
        self.has_credit_limit = None
        self.credit_limit = -1
