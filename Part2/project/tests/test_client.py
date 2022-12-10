from LegacyApp import Client
from LegacyApp import ClientStatus
import unittest


class TestClient(unittest.TestCase):
    def add_client(self):
        client = Client(1, "aaa", ClientStatus.UNDEFINED)
        return client

    def test_client_name(self):
        client = self.add_client()
        self.assertEqual(client.name, "aaa")

    def test_client_id(self):
        client = self.add_client()
        self.assertEqual(client.id, 1)

    def test_client_status(self):
        client = self.add_client()
        self.assertEqual(client.status, ClientStatus.UNDEFINED)
