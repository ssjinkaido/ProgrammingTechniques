import unittest
from LegacyApp.Client import Client
from LegacyApp.ClientStatus import ClientStatus


class TestClientIp(unittest.TestCase):
    def create_client_instance(self, id, name, status):
        instance_client = Client(id, name, status)
        return instance_client

    def test_client_vip_id(self):
        client_vip = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(client_vip.id, 1)

    def test_client_vip_name(self):
        client_vip = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(client_vip.name, "aaa")

    def test_client_vip_status(self):
        client_vip = self.create_client_instance(1, "aaa", ClientStatus.VIP)
        self.assertEqual(client_vip.status, ClientStatus.VIP)

    def test_client_ip_id(self):
        client_ip = self.create_client_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(client_ip.id, 1)

    def test_client_ip_name(self):
        client_ip = self.create_client_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(client_ip.name, "aaa")

    def test_client_ip_status(self):
        client_ip = self.create_client_instance(1, "aaa", ClientStatus.IP)
        self.assertEqual(client_ip.status, ClientStatus.IP)

    def test_client_normal_id(self):
        client_normal = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(client_normal.id, 1)

    def test_client_normal_name(self):
        client_normal = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(client_normal.name, "aaa")

    def test_client_normal_status(self):
        client_normal = self.create_client_instance(1, "aaa", ClientStatus.NORMAL)
        self.assertEqual(client_normal.status, ClientStatus.NORMAL)

    def test_client_undefined_id(self):
        client_undefined = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(client_undefined.id, 1)

    def test_client_undefined_name(self):
        client_undefined = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(client_undefined.name, "aaa")

    def test_client_undefined_status(self):
        client_undefined = self.create_client_instance(1, "aaa", ClientStatus.UNDEFINED)
        self.assertEqual(client_undefined.status, ClientStatus.UNDEFINED)
