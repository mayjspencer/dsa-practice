# -----------------------------
# FIND MIDDLE NODE PRACTICE
# -----------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle_node(head):
    """
    Returns the middle node of the linked list.
    If even number of nodes, return the second middle.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

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

head1 = build_linked_list([1, 2, 3])
print("List:", print_list(head1))
middle1 = find_middle_node(head1)
print("Middle:", middle1.val)

head2 = build_linked_list([1, 2, 3, 4])
print("List:", print_list(head2))
middle2 = find_middle_node(head2)
print("Middle:", middle2.val)

head3 = build_linked_list([1, 2, 3, 4, 5, 6])
print("List:", print_list(head3))
middle3 = find_middle_node(head3)
print("Middle:", middle3.val)
