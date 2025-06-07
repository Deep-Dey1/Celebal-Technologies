# Define the Node class first
class Node:
    def __init__(self, data):
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node


# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Method to add a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Add the new node at the end

    # Method to print the list
    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to delete the nth node (1-based index)
    def delete_nth_node(self, n):
        if not self.head:  # Check if the list is empty
            raise IndexError("Cannot delete from an empty list.")
        
        # Special case if the node to be deleted is the head
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        count = 1
        
        # Traverse the list to find the (n-1)th node
        while current and count < n - 1:
            current = current.next
            count += 1
        
        # If current is None or the next node is None, it means the index is out of range
        if not current or not current.next:
            raise IndexError(f"Index {n} is out of range.")
        
        # Delete the nth node by skipping it
        current.next = current.next.next


# Test the LinkedList class
if __name__ == "__main__":
    # Create a LinkedList
    ll = LinkedList()

    # Add nodes to the list
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)

    # Print the original list
    print("Original Linked List:")
    ll.print_list()

    # Delete 3rd node
    try:
        ll.delete_nth_node(3)  # Delete the node at index 3 (1-based index)
        print("\nList after deleting 3rd node:")
        ll.print_list()
    except IndexError as e:
        print(f"Error: {e}")

    # Delete the 1st node
    try:
        ll.delete_nth_node(1)  # Delete the first node
        print("\nList after deleting 1st node:")
        ll.print_list()
    except IndexError as e:
        print(f"Error: {e}")

    # Try deleting a node from an invalid position (index out of range)
    try:
        ll.delete_nth_node(10)  # Should raise an IndexError since the index is out of range
    except IndexError as e:
        print(f"Error: {e}")
