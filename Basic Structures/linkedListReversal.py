# -----------------------------
# REVERSE LINKED LIST PRACTICE
# -----------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_iterative(head):
    """
    Reverse the linked list using an iterative approach.
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # store the next node
        curr.next = prev       # reverse the pointer
        prev = curr            # move prev and curr forward
        curr = next_node
    return prev

def reverse_recursive(head):
    """
    Reverse the linked list using a recursive approach.
    """
    if head is None or head.next is None:
        return head

    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

# -----------------------------
# TEST UTILITIES
# -----------------------------

def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    return ' -> '.join(values)

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# -----------------------------
# TESTING
# -----------------------------

head1 = build_linked_list([1, 2, 3, 4, 5])
reversed1 = reverse_iterative(head1)
print("Iterative:", print_list(reversed1))

head2 = build_linked_list([1, 2, 3, 4, 5])
reversed2 = reverse_recursive(head2)
print("Recursive:", print_list(reversed2))
