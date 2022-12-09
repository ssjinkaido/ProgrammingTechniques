# test the Node class
import unittest
import sys

sys.path.append("../")
from unittest.mock import patch


from api import Node


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(5, None)

    def test_init(self):
        self.assertEqual(self.node.data, 5)
        self.assertEqual(self.node.next, None)

    def test_init_next_is_not_none(self):
        node = Node(42)
        self.assertIsNone(node.next)  

    def test_init_next_is_not_none(self):
        node = Node(42, Node(0))
        self.assertIsNotNone(node.next)  

    def test_repr(self):
        node = Node(42)
        self.assertEqual(repr(node), '(42)')

    def test_immutable(self):
        value = 42
        node = Node(value)
        with self.assertRaises(AttributeError):
            node.data = 0
        self.assertEqual(node.data, value)
