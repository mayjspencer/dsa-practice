# -----------------------------
# DETECT CYCLE PRACTICE
# -----------------------------

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    Detects if the linked list has a cycle.
    Uses Floyd's Tortoise and Hare algorithm.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# -----------------------------
# TEST UTILITIES
# -----------------------------

def build_cyclic_list(values, pos):
    """
    Builds a linked list with a cycle.
    pos: index at which the tail connects (0-based), or -1 if no cycle
    """
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    cycle_node = None

    for i, val in enumerate(values[1:], start=1):
        curr.next = ListNode(val)
        curr = curr.next
        if i == pos:
            cycle_node = curr

    if pos != -1:
        curr.next = cycle_node  # create cycle

    return head

# -----------------------------
# TESTING
# -----------------------------

acyclic = build_cyclic_list([1, 2, 3, 4, 5], -1)
print("Cycle (should be False):", has_cycle(acyclic))

cyclic = build_cyclic_list([1, 2, 3, 4, 5], 2)
print("Cycle (should be True):", has_cycle(cyclic))
