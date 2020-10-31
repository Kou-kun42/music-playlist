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

    def delete_from_head(self):
        # Checks if the list has something
        if self.head is not None:
            # Checks if list only has one item
            if self.head == self.tail:
                self.tail = None
            # Get rid of current head node
            self.head = self.head.next

    def delete_from_tail(self):
        # Checks if list has something
        if self.head is not None:
            # Make a node variable
            curr_node = self.head
            # Checks if list doesn't have only 1 item
            if self.head != self.tail:
                # Iterate through list until we find node that points to tail
                while curr_node.next != self.tail:
                    curr_node = curr_node.next
                # Get rid of pointer to tail node
                curr_node.next = None
            # Else if the list only has 1 node then set current to None
            else:
                curr_node = None

            # Set new tail
            self.tail = curr_node

            # If the list only had 1 item, set head to None as well
            if curr_node is None:
                self.head = curr_node

    def find(self, song):
        # Set node variable
        current_node = self.head
        # While current_node exists
        while current_node is not None:
            # Checks if node is the target song
            if current_node.song == song:
                return True
            else:
                current_node = current_node.next

        # Return False if not found
        return False

    def delete(self, song):
        node = self.head
        # Check if list exists
        if node is not None:
            # Check if there's more than 1 node
            if node.next is not None:
                # Check if head is target
                if node.song == song:
                    # Get rid of head
                    self.head = node.next
                else:
                    # Iterate through nodes
                    while node.next is not None and node.next.song != song:
                        node = node.next

                    if node.next is not None and node.next.song == song:
                        node.next = node.next.next
            # Else if there's only 1 node, check that for the song
            else:
                if node.song == song:
                    # get rid of head and tail
                    self.head = None
                    self.tail = None
