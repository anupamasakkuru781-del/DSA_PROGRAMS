class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # insert at position
    def insert_at_position(self, pos, data):
        if pos == 0:
            self.insert_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:
                return

        new_node.next = temp.next
        temp.next = new_node

    # delete beginning
    def delete_begin(self):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    # delete end (FIXED)
    def delete_end(self):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            return

        prev = None
        temp = self.head

        while temp.next != self.head:
            prev = temp
            temp = temp.next

        prev.next = self.head   # remove last node

    # delete by value (FIXED)
    def delete_value(self, key):
        if self.head is None:
            return

        # if head node contains key
        if self.head.data == key:
            self.delete_begin()
            return

        temp = self.head
        while temp.next != self.head:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next

    # search
    def search(self, key):
        if self.head is None:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    # update value by position
    def update(self, pos, value):
        temp = self.head

        for _ in range(pos):
            temp = temp.next
            if temp == self.head:
                return

        temp.data = value

    # display
    def display(self):
        if self.head is None:
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


# Testing
cll = CircularLinkedList()

cll.insert_begin(20)
cll.insert_begin(10)
cll.insert_end(30)
cll.insert_end(40)
cll.display()
cll.insert_at_position(1, 15)
cll.display()
cll.delete_begin()
cll.display()
cll.delete_end()
cll.display()
cll.delete_value(15)
cll.display()
print(cll.search(20))
cll.update(1, 25)
cll.display()
