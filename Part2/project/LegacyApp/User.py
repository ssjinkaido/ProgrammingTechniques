from __future__ import annotations
import datetime
from .Client import IClient
from typing import TypeVar


class User:
    def __init__(
        self: User,
        client: IClient,
        date_of_birth: datetime.date,
        email_address: str,
        first_name: str,
        surname: str,
    ):
        self.client = client
        self.date_of_birth = date_of_birth
        self.email_address = email_address
        self.first_name = first_name
        self.surname = surname
        self.has_credit_limit = False
        self.credit_limit = -1
