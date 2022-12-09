class Node:
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    def __repr__(self):
        return '(' + repr(self._data) + ')'
    
    @property
    def data(self):
        return self._data
    
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values is not None:
            node = None
            for elem in values:
                if node is None:
                    self.head = Node(elem)
                    node = self.head
                else:
                    node.next = Node(elem)
                    node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(repr(node))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __len__(self):
        result = 0
        node = self.head
        while node is not None:
            result = result + 1
            node = node.next
        return result

    def is_empty(self):
        return self.head is None

    def __node_to_node(self, node, next=None):
        if isinstance(node, Node):
            node.next = next
            return node
        return Node(node, next)
    
    def add_first(self, node):
        self.head = self.__node_to_node(node, self.head)

    def add_last(self, node):
        if self.is_empty():
            self.head = self.__node_to_node(node)
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = self.__node_to_node(node)
    
    def add_before(self, target_node_data, new_node):
        if self.is_empty():
            raise ValueError("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = self.__node_to_node(new_node, node)
                return
            prev_node = node

        raise ValueError(f"Node with data {target_node_data} not found")

    def add_after(self, target_node_data, new_node):
        if self.is_empty():
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                node.next = self.__node_to_node(new_node, node.next)
                return

        raise ValueError(f"Node with data {target_node_data} not found")

    def remove_node(self, target_node_data):
        if self.is_empty():
            raise ValueError("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise ValueError(f"Node with data {target_node_data} not found")

