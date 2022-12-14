import unittest
from unittest.mock import MagicMock
import datetime
from LegacyApp.ClientStatus import ClientStatus


class TestDBAccess(unittest.TestCase):
    def create_client_instance(self, id, name, status):
        instance_client = MagicMock()
        instance_client.id = id
        instance_client.name = name
        instance_client.status = status
        return instance_client

    def create_user_instance_with_client(
        self,
        client,
        date_of_birth,
        email_address,
        first_name,
        surname,
        credit_limit,
        has_credit_limit,
    ):
        instance_user = MagicMock()
        instance_user.client = client
        instance_user.email_address = email_address
        instance_user.first_name = first_name
        instance_user.surname = surname
        instance_user.date_of_birth = date_of_birth
        instance_user.credit_limit = credit_limit
        instance_user.has_credit_limit = has_credit_limit
        return instance_user

    def create_columns(self):
        return [
            "client_id",
            "date_of_birth",
            "email_address",
            "first name",
            "surname",
            "has_credit_limit",
            "credit_limit",
        ]

    def create_db_entry_instance(self, key, user):
        instance_db_entry = MagicMock()
        instance_db_entry.key = key
        instance_db_entry.columns = self.create_columns()
        instance_db_entry.values = {}
        values = [
            user.client.id,
            user.date_of_birth,
            user.email_address,
            user.first_name,
            user.surname,
            user.has_credit_limit,
            user.credit_limit,
        ]
        for i in range(len(instance_db_entry.columns)):
            instance_db_entry.values[instance_db_entry.columns[i]] = values[i]

        return instance_db_entry

    def create_db_table_instance(self):
        instance_db_table = MagicMock()
        instance_db_table.name = "users"
        instance_db_table.columns = self.create_columns()

        instance_db_table.nb_columns = len(instance_db_table.columns)
        instance_db_table.data_types = [int, datetime.date, str, str, str, bool, int]
        instance_db_table.data = {}
        return instance_db_table

    def create_mock_db_access(self):
        instance_db_access = MagicMock()
        instance_db_access.tables = {}
        return instance_db_access

    def add_entry(self, key, db_entry, instance_db_table):
        instance_db_table.data[key] = db_entry

    def add_table(self, name, db_table, instance_db_access):
        instance_db_access.tables[name] = db_table

    def test_db_entry_get_key_one(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_instance_with_client(
            client,
            datetime.date(2000, 12, 4),
            "aaa@gmail.com",
            "Jack",
            "Roy",
            3000,
            True,
        )
        db_entry = self.create_db_entry_instance(1, user)
        self.assertEqual(db_entry.key, 1)

    def test_db_entry_get_key_two(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_instance_with_client(
            client,
            datetime.date(1980, 12, 4),
            "aaa@gmail.com",
            "John",
            "Smith",
            3000,
            True,
        )
        db_entry = self.create_db_entry_instance(2, user)
        self.assertEqual(db_entry.key, 2)

    def test_db_entry_get_value_by_column(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_instance_with_client(
            client,
            datetime.date(1995, 12, 4),
            "bbb@gmail.com",
            "Becken",
            "Smith",
            1500,
            True,
        )
        db_entry = self.create_db_entry_instance(1, user)
        self.assertEqual(db_entry.values["first name"], "Becken")

    def test_db_table_get_entry(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        user = self.create_user_instance_with_client(
            client,
            datetime.date(1999, 12, 4),
            "aaa@gmail.com",
            "Hailey",
            "Smith",
            1500,
            True,
        )
        db_entry_one = self.create_db_entry_instance(1, user)
        db_table = self.create_db_table_instance()
        self.add_entry(1, db_entry_one, db_table)
        self.assertEqual(db_table.data[1], db_entry_one)

    def test_db_table_is_entry_exists_success(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.IP)
        user = self.create_user_instance_with_client(
            client,
            datetime.date(1975, 4, 16),
            "mayfloyd@gmail.com",
            "Mayweather",
            "Floyd",
            3000,
            True,
        )
        db_entry_one = self.create_db_entry_instance(1, user)
        db_table = self.create_db_table_instance()
        self.add_entry(1, db_entry_one, db_table)
        result = 1 in db_table.data
        self.assertTrue(result)

    def test_db_table_is_entry_exists_fail(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        user = self.create_user_instance_with_client(
            client,
            datetime.date(1989, 3, 3),
            "aaa@gmail.com",
            "Taylor",
            "Swift",
            1500,
            True,
        )
        db_entry_one = self.create_db_entry_instance(1, user)
        db_table = self.create_db_table_instance()
        self.add_entry(1, db_entry_one, db_table)
        result = 2 in db_table.data
        self.assertFalse(result)

    def test_db_table_generate_key_one(self):
        client = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        user = self.create_user_instance_with_client(
            client,
            datetime.date(1903, 10, 4),
            "alanwalker@gmail.com",
            "Alan",
            "Walker",
            -1,
            False,
        )
        db_entry_one = self.create_db_entry_instance(1, user)
        db_table = self.create_db_table_instance()
        self.add_entry(1, db_entry_one, db_table)
        self.assertEqual(max(db_table.data) + 1, 2)

    def test_db_access_is_table_true(self):
        db_table = self.create_db_table_instance()
        db_access = self.create_mock_db_access()
        self.add_table("users", db_table, db_access)
        result = "users" in db_access.tables
        self.assertTrue(result)

    def test_db_access_is_table_false(self):
        db_table = self.create_db_table_instance()
        db_access = self.create_mock_db_access()
        self.add_table("user", db_table, db_access)
        result = "users" in db_access.tables
        self.assertFalse(result)

    def test_db_access_get_table_success(self):
        db_table = self.create_db_table_instance()
        db_access = self.create_mock_db_access()
        self.add_table("users", db_table, db_access)
        self.assertEqual(db_access.tables["users"], db_table)

    def test_db_access_get_table_fail(self):
        db_table = self.create_db_table_instance()
        db_access = self.create_mock_db_access()
        self.add_table("users", db_table, db_access)
        with self.assertRaises(Exception):
            db_access.tables["user"]
