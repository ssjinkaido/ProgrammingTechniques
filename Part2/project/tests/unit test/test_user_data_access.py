import unittest
import datetime
from unittest.mock import MagicMock
from LegacyApp.ClientStatus import ClientStatus
from LegacyApp.UserDataAccess import UserDataAccess
from LegacyApp.UserService import get_credit_limit


class TestUserDataAccess(unittest.TestCase):
    def create_client_instance(self, id, name, status):
        client = MagicMock()
        client.id = id
        client.name = name
        client.status = status
        return client

    def create_user_with_client(
        self, client, date_of_birth, email_address, first_name, surname
    ):
        user = MagicMock()
        user.client = client
        user.email_address = email_address
        user.first_name = first_name
        user.surname = surname
        user.date_of_birth = date_of_birth
        user.credit_limit = -1
        user.has_credit_limit = None
        return user

    def create_user_database(self):
        instance_user_data_access = UserDataAccess()
        return instance_user_data_access

    def test_add_user(self):
        user_data_access = self.create_user_database()
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(user_data_access.add_user(user))
