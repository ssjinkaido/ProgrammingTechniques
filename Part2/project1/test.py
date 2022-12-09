class DoubleLinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next_node
            return item


class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.__data = data
        self.__prev_node = prev_node
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def prev_node(self):
        return self.__prev_node

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        self.__data = value

    @prev_node.setter
    def prev_node(self, value):
        self.__prev_node = value

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value

    def __del__(self):
        print("\nnode deleted")


# write your implementation here
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return DoubleLinkedListIterator(self.head)

    def __len__(self):
        length_list = 0
        while self.head is not None:
            length_list += 1
            self.head = self.head.next_node
        return length_list

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        if self.head is not None:
            self.head.prev_node = new_node
        self.head = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, "->", end=" ")
            current = current.next_node

    def delete_first_n_node(self, n):
        if self.head is None:
            return
        i = 0
        while i < n:
            if self.head is not None and self.head.next_node is not None:
                self.head = self.head.next_node
                self.head.prev_node = None
            i += 1

    def display_in_reverse_order(self):
        stack = []
        current = self.head
        while current is not None:
            stack.append(current)
            current = current.next_node
        while len(stack):
            print(stack.pop().data, "->", end=" ")
        print()

    def sort_ascending_order(self):
        if self.head == None:
            return
        else:
            current = self.head
            while current.next_node != None:
                index = current.next_node
                while index != None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next_node
                current = current.next_node


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.push(1)
    dll.push(10)
    dll.push(6)
    dll.push(8)
    dll.push(9)
    dll.push(4)
    print("Display ll using iter: \n")
    for i in dll:
        print(i, "->", end=" ")
    dll.delete_first_n_node(2)
    print("\n")
    print("After delete first node: ")
    dll.display()
    print("\n")
    print("\nDisplay in reverse order:")
    dll.display_in_reverse_order()
    dll.sort_ascending_order()
    print("\nDisplay in ascending order:")
    dll.display()
    # add your test here (you may call functions...)


