class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for i in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

# -----------------------------
# TEST UTILITIES
# -----------------------------

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    return ' -> '.join(values)

# -----------------------------
# TESTING
# -----------------------------

head = build_linked_list([1, 2, 3, 4, 5])
print("Original:", print_list(head))
result = remove_nth_from_end(head, 2)
print("After removal:", print_list(result))
