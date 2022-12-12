import unittest
from LegacyApp.Client import ClientNormal
from LegacyApp.ClientStatus import ClientStatus


class TestClientNormal(unittest.TestCase):
    def create_instance(self, id, name, status):
        client_normal = ClientNormal(id, name, status)
        return client_normal

    def test_client_normal_id(self):
        self.client_normal = self.create_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(self.client_normal.id, 1)

    def test_client_normal_name(self):
        self.client_normal = self.create_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(self.client_normal.name, "aaa")

    def test_client_normal_status(self):
        self.client_normal = self.create_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(self.client_normal.status, ClientStatus.NORMAL)
