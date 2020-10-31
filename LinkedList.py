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

    def prepend(self, song):
        # Make new node from the song
        node = Node(song)

        # If the head is not empty then set song's next to it
        if self.head is not None:
            node.next = self.head
        # If head is empty then set tail to the new node
        else:
            self.tail = node

        # Set the head to the new node
        self.head = node

    def print_songs(self):
        # Set variable to keep track of the current node
        current_node = self.head

        # While the current node is not empty, print name of song
        while current_node is not None:
            print(current_node.song)
            current_node = current_node.next
