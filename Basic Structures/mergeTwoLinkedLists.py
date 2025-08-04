# -----------------------------
# MERGE TWO SORTED LISTS
# -----------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(list1, list2):
    """
    Merges two sorted linked lists and returns the head of the new list.
    """
    dummy = ListNode(-1)  # Placeholder node
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2

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

l1 = build_linked_list([1, 3, 4])
l2 = build_linked_list([1, 2, 5])
merged = merge_sorted_lists(l1, l2)
print("Merged List:", print_list(merged))
