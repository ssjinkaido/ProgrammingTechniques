import unittest
from LegacyApp.ClientRepository import ClientRepository
from LegacyApp.ClientRepository import Client


class TestClientRepository(unittest.TestCase):
    def create_instance(self):
        instance_client_repo = ClientRepository()
        return instance_client_repo

    def test_get_by_id_correct_five(self):
        instance_client_repo = self.create_instance()
        self.assertIsInstance(instance_client_repo.get_by_id(5), Client)

    def test_get_by_id_correct_nine(self):
        instance_client_repo = self.create_instance()
        self.assertIsInstance(instance_client_repo.get_by_id(9), Client)

    def test_get_by_id_fail(self):
        instance_client_repo = self.create_instance()
        with self.assertRaises(Exception):
            instance_client_repo.get_by_id(12)
