class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, song):
        # Make new node from song
        node = Node(song)

        # If list is empty then set node as head
        if self.head is None:
            self.head = node

        # If list has a tail, set its next to node
        if self.tail is not None:
            self.tail.next = node

        # Set the tail as the node to append
        self.tail = node
