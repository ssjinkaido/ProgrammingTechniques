from __future__ import annotations
from typing import List, TypeVar, Optional, Union, Iterator, Iterable, Generic


class LinkedList(Iterable):
    
    __T = TypeVar("__T")

    class __Node(Generic[__T]):
        # the optional part can also be written as: None|LinkedList.__Node
        def __init__(self, data: LinkedList.__T, next: Optional[LinkedList.__Node] = None) -> None:
            self.__data = data
            self.__next = next

        @property 
        def data(self) -> LinkedList.__T:
            return self.__data
        
        @property
        def next(self) -> LinkedList.__Node | None:
            return self.__next
        
        @next.setter
        def next(self, _next):
            self.__next = _next
        
        def __repr__(self) -> str:
            return repr(self.data)

    def __init__(self, nodes: Optional[List[LinkedList.__T]] = None) -> None:
        self.__head = None
        if nodes:
            node = self.__Node(data=nodes.pop(0))
            self.__head = node
            for elem in nodes:
                node.next = self.__Node(elem)
                node = node.next

    def __repr__(self) -> str:
        node = self.__head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        # nodes.append("None")
        print_str = " -> ".join(str(i) for i in nodes) + " -> " + "None"
        return print_str

    def __iter__(self) -> Iterator[LinkedList.__Node]:
        node = self.__head
        while node:
            yield node
            node = node.next

    def is_empty(self) -> bool:
        return self.__head is None
    
    def add_first(self, data: LinkedList.__T) -> LinkedList:
        self.__head = self.__Node(data, self.__head)
        return self

    def add_last(self, data: LinkedList.__T) -> LinkedList:
        if self.__head is None:
            return self.add_first(data)
            
        current_node = self.__head
        if current_node:
            while current_node.next:
                current_node = current_node.next
            current_node.next = self.__Node(data)
        
        return self
    
    def add_before(self, target_node_data: LinkedList.__T, new_node_data: LinkedList.__T) -> LinkedList:
        if self.is_empty():
            raise Exception("List is empty")

        if self.__head:
            if self.__head.data == target_node_data:
                return self.add_first(new_node_data)

        prev_node = self.__head
        for node in self:
            if node.data == target_node_data:
                if prev_node:
                    prev_node.next = self.__Node(new_node_data, node)
                    return self
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def add_after(self, target_node_data: LinkedList.__T, new_node_data: LinkedList.__T) -> LinkedList:
        if self.is_empty():
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                node.next = self.__Node(new_node_data, node.next)
                return self

        raise Exception(f"Node with data {target_node_data} not found")

    def remove_node(self, target_node_data: LinkedList.__T) -> LinkedList:
        if self.is_empty():
            raise Exception("List is empty")

        if self.__head:
            if self.__head.data == target_node_data:
                self.head = self.__head.next
            return self

        previous_node = self.__head
        for node in self:
            if node.data == target_node_data:
                if previous_node:
                    previous_node.next = node.next
                    return self
            previous_node = node

        raise Exception(f"Node with data {target_node_data} not found")


if __name__ == "__main__":
    def build_list() -> LinkedList:
        lklist = LinkedList(["b", "d", "f"])
        lklist.add_first("a")
        lklist.add_last("g")
        lklist.add_before("d", "c")
        lklist.add_after("d", "e")
        return lklist
    
    def remove_one_over_two(lklist: LinkedList):
        lklist.remove_node("a")
        lklist.remove_node("c")
        lklist.remove_node("e")
        lklist.remove_node("g")
        
    lklist = build_list()
    print(lklist)
    remove_one_over_two(lklist)
    print(lklist)
