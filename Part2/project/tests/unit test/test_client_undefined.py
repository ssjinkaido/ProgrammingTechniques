import unittest
from LegacyApp.Client import ClientUndefined
from LegacyApp.ClientStatus import ClientStatus


class TestClientUndefined(unittest.TestCase):
    def create_instance(self, id, name, status):
        client_undefined = ClientUndefined(id, name, status)
        return client_undefined

    def test_client_undefined_id(self):
        self.client_undefined = self.create_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(self.client_undefined.id, 1)

    def test_client_undefined_name(self):
        self.client_undefined = self.create_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(self.client_undefined.name, "aaa")

    def test_client_undefined_status(self):
        self.client_undefined = self.create_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(self.client_undefined.status, ClientStatus.UNDEFINED)
