import unittest
from LegacyApp.Client import ClientIP
from LegacyApp.ClientStatus import ClientStatus


class TestClientIp(unittest.TestCase):
    def create_instance(self, id, name, status):
        client_ip = ClientIP(id, name, status)
        return client_ip

    def test_client_ip_id(self):
        self.client_ip = self.create_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(self.client_ip.id, 1)

    def test_client_ip_name(self):
        self.client_ip = self.create_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(self.client_ip.name, "aaa")

    def test_client_ip_status(self):
        self.client_ip = self.create_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(self.client_ip.status, ClientStatus.IP)
