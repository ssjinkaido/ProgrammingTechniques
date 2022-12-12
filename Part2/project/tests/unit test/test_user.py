import unittest
import datetime
from unittest.mock import MagicMock
from LegacyApp.ClientStatus import ClientStatus


class TestUser(unittest.TestCase):
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
        return user

    def test_user_with_clientip_first_name(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.first_name, "John")

    def test_user_with_clientip_surname(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.surname, "Smith")

    def test_user_with_clientip_email_address(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.email_address, "aaa@gmail.com")

    def test_user_with_clientip_date_of_birth(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.date_of_birth, datetime.date(1969, 12, 4))

    def test_user_with_clientvip_first_name(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.first_name, "John")

    def test_user_with_clientvip_surname(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.surname, "Smith")

    def test_user_with_clientvip_email_address(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.email_address, "aaa@gmail.com")

    def test_user_with_clientvip_date_of_birth(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.date_of_birth, datetime.date(1969, 12, 4))

    def test_user_with_client_normal_first_name(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.first_name, "John")

    def test_user_with_client_normal_surname(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.surname, "Smith")

    def test_user_with_client_normal_email_address(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.email_address, "aaa@gmail.com")

    def test_user_with_client_normal_date_of_birth(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.date_of_birth, datetime.date(1969, 12, 4))

    def test_user_with_client_undefined_first_name(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.first_name, "John")

    def test_user_with_client_undefined_surname(self):

        client = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.surname, "Smith")

    def test_user_with_client_undefined_email_address(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.email_address, "aaa@gmail.com")

    def test_user_with_client_undefined_date_of_birth(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        user = self.create_user_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        self.assertEqual(user.date_of_birth, datetime.date(1969, 12, 4))
