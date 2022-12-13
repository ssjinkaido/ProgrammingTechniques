import unittest
from LegacyApp.Client import Client
from LegacyApp.ClientStatus import ClientStatus


class TestClientIp(unittest.TestCase):
    def create_instance(self, id, name, status):
        client = Client(id, name, status)
        return client

    def test_client_vip_id(self):
        self.client_vip = self.create_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(self.client_vip.id, 1)

    def test_client_vip_name(self):
        self.client_vip = self.create_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(self.client_vip.name, "aaa")

    def test_client_vip_status(self):
        self.client_vip = self.create_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(self.client_vip.status, ClientStatus.VIP)

    def test_client_ip_id(self):
        self.client_ip = self.create_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(self.client_ip.id, 1)

    def test_client_ip_name(self):
        self.client_ip = self.create_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(self.client_ip.name, "aaa")

    def test_client_ip_status(self):
        self.client_ip = self.create_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(self.client_ip.status, ClientStatus.IP)

    def test_client_normal_id(self):
        self.client_normal = self.create_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(self.client_normal.id, 1)

    def test_client_normal_name(self):
        self.client_normal = self.create_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(self.client_normal.name, "aaa")

    def test_client_normal_status(self):
        self.client_normal = self.create_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(self.client_normal.status, ClientStatus.NORMAL)

    def test_client_undefined_id(self):
        self.client_undefined = self.create_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(self.client_undefined.id, 1)

    def test_client_undefined_name(self):
        self.client_undefined = self.create_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(self.client_undefined.name, "aaa")

    def test_client_undefined_status(self):
        self.client_undefined = self.create_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(self.client_undefined.status, ClientStatus.UNDEFINED)
