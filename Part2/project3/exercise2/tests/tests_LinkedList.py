# test the LinkedList class
import unittest
from unittest.mock import patch
from api import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList(values=[5, 6, 7, 8, 9])

    def test_init(self):
        self.assertEqual(self.linked_list.head.data, 5)
        self.assertIsNotNone(self.linked_list.head)
        
    def test_length(self):
        self.assertEqual(len(self.linked_list),5)
    
    def test_empty(self):
        self.assertEqual(self.linked_list.is_empty(), False)

    def test_add_first(self):
        self.node = Node(10)
        self.linked_list.add_first(self.node)
        self.assertEqual(len(self.linked_list), 6)
        self.assertEqual(self.linked_list.head.next.data, 5)

    def test_add_last(self):
        self.node = Node(15)
        self.linked_list.add_last(self.node)
        self.assertEqual(len(self.linked_list), 6)

    def test_add_before(self):
        self.node = Node(12)
        self.linked_list.add_before(5, self.node)
        self.assertEqual(len(self.linked_list),6)
        self.assertEqual(self.linked_list.head.data, 12)
        self.assertEqual(self.linked_list.head.next.data, 5)

    def test_add_after(self):
        self.node = Node(13)
        self.linked_list.add_after(5, self.node)
        self.assertEqual(len(self.linked_list),6)
        self.assertEqual(self.linked_list.head.next.data, 13)
        self.assertEqual(self.linked_list.head.next.next.data, 6)
        

    def test_remove_node(self):
        self.linked_list.remove_node(5)
        self.assertEqual(len(self.linked_list),4)
        self.assertEqual(self.linked_list.head.data, 6)

    def test_iter(self):
        it1=iter(self.linked_list)
        self.assertEqual(next(it1).data,5)
        self.assertEqual(next(it1).data,6)
        self.assertEqual(next(it1).data,7)
        self.assertEqual(next(it1).data,8)
        self.assertEqual(next(it1).data,9)
        with self.assertRaises(StopIteration):
            next(it1).data
