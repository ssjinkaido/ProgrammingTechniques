import unittest
import datetime
from unittest.mock import MagicMock
from LegacyApp.ClientStatus import ClientStatus
from LegacyApp.UserService import (
    validate_name,
    validate_email,
    validate_age,
    validate_input,
    validate_user,
    get_credit_limit,
    UserService,
)


class TestUserService(unittest.TestCase):
    def create_client_instance(self, id, name, status):
        instance_client = MagicMock()
        instance_client.id = id
        instance_client.name = name
        instance_client.status = status
        return instance_client

    def create_user_instance_with_client(
        self, client, date_of_birth, email_address, first_name, surname
    ):
        instance_user = MagicMock()
        instance_user.client = client
        instance_user.email_address = email_address
        instance_user.first_name = first_name
        instance_user.surname = surname
        instance_user.date_of_birth = date_of_birth
        instance_user.credit_limit = -1
        instance_user.has_credit_limit = None
        return instance_user

    def create_user_service_instance(self):
        instance_user_service = UserService()
        return instance_user_service

    def test_validate_name(self):
        self.assertTrue(validate_name("aaa", "bbb"))

    def test_invalidate_name_one(self):
        self.assertFalse(validate_name("aaa", ""))

    def test_invalidate_name_two(self):
        self.assertFalse(validate_name("", "bbb"))

    def test_validate_email(self):
        self.assertTrue(validate_email("aaa@gmail.com"))

    def test_invalidate_email(self):
        self.assertFalse(validate_email("aaa@gmailcom"))

    def test_validate_age(self):
        self.assertTrue(validate_age(datetime.date(1990, 12, 4)))

    def test_invalidate_age(self):
        self.assertFalse(validate_age(datetime.date(2003, 9, 8)))

    def test_validate_input(self):
        self.assertTrue(
            validate_input("aaa", "bbb", "aaa@gmail.com", datetime.date(2000, 3, 3))
        )

    def test_invalidate_input(self):
        self.assertFalse(
            validate_input("", "bbb", "aaa@gmail.com", datetime.date(2000, 3, 3))
        )

    def test_user_ip_credit_limit(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(user.has_credit_limit)
        self.assertEqual(user.credit_limit, 3000)

    def test_user_vip_credit_limit(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertFalse(user.has_credit_limit)
        self.assertEqual(user.credit_limit, -1)

    def test_user_normal_credit_limit(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(user.has_credit_limit)
        self.assertEqual(user.credit_limit, 1500)

    def test_user_undefined_credit_limit(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(user.has_credit_limit)
        self.assertEqual(user.credit_limit, 1500)

    def test_validate_vip_user(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(validate_user(user))

    def test_validate_ip_user(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(validate_user(user))

    def test_validate_normal_user(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(validate_user(user))

    def test_validate_undefined_user(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        user = self.create_user_instance_with_client(
            client, datetime.date(1969, 12, 4), "aaa@gmail.com", "John", "Smith"
        )
        get_credit_limit(user)
        self.assertTrue(validate_user(user))

    def test_add_user_one(self):
        user_service = self.create_user_service_instance()
        result = user_service.add_user(
            "John", "Smith", "aaa@gmail.com", datetime.date(1969, 12, 4), 3
        )
        self.assertEqual(result, True)

    def test_add_user_two(self):
        user_service = self.create_user_service_instance()
        result = user_service.add_user(
            "Mary", "Avicii", "mary@gmail.com", datetime.date(2005, 12, 4), 1
        )
        self.assertEqual(result, False)
