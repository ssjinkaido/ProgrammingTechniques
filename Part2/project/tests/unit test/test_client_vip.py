import unittest
from LegacyApp.Client import ClientVIP
from LegacyApp.ClientStatus import ClientStatus


class TestClientVip(unittest.TestCase):
    def create_instance(self, id, name, status):
        client_vip = ClientVIP(id, name, status)
        return client_vip

    def test_client_vip_id(self):
        self.client_vip = self.create_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(self.client_vip.id, 1)

    def test_client_vip_name(self):
        self.client_vip = self.create_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(self.client_vip.name, "aaa")

    def test_client_vip_status(self):
        self.client_vip = self.create_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(self.client_vip.status, ClientStatus.VIP)
