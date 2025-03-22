"""
Node is a basic building block of many data structures
A node has a value and pointer to the next node
With node, we can implement many data structures like singly and doubly linked list, stack, queue, deque
"""

class Node:
    def __init__(self, value):
        # Node stores a value and pointer to the next node
        self.value = value
        self.next = None
    
def print_node(node : Node):
    # It will print the initial node
    # until it encounters the null for the next pointer
    while node != None:
        print(node.value, end=' -> ')
        node = node.next
    print("NULL")


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # let's connect these nodes to each other
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print_node(node1)

