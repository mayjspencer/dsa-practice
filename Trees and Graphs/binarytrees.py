from collections import deque

# =========================
# Binary Tree Node
# =========================

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_level_order(values):
    if not values:
        return None

    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = BinaryTreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = BinaryTreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def preorder(node):
    if not node:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def postorder(node):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def size(node):
    if not node:
        return 0
    return 1 + size(node.left) + size(node.right)


# =========================
# Binary Search Tree Node
# =========================

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bst_insert(node, value):
    if not node:
        return BSTNode(value)
    if value < node.value:
        node.left = bst_insert(node.left, value)
    elif value > node.value:
        node.right = bst_insert(node.right, value)
    return node



def bst_search(node, target):
    if not node:
        return None
    if node.value == target:
        return node
    if target < node.value:
        return bst_search(node.left, target)
    else:
        return bst_search(node.right, target)

def bst_inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def bst_min(node):
    while node and node.left:
        node = node.left
    return node

def bst_max(node):
    while node and node.right:
        node = node.right
    return node


def bst_delete(node, key):
    if not node:
        return None
    if key < node.value:
        node.left = bst_delete(node.left, key)
    elif key > node.value:
        node.right = bst_delete(node.right, key)
    else:
        # Node with 0 or 1 child
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        # Node with 2 children: replace with inorder successor
        successor = bst_min(node.right)
        node.value = successor.value
        node.right = bst_delete(node.right, successor.value)
    return node


def is_valid_bst(node, low=float('-inf'), high=float('inf')):
    if not node:
        return True
    if not (low < node.value < high):
        return False
    return (is_valid_bst(node.left, low, node.value) and
            is_valid_bst(node.right, node.value, high))   


# =========================
# Tests
# =========================

def test_binary_tree():
    root = build_tree_level_order([1, 2, 3, None, 4, 5, None])
    assert preorder(root) == [1, 2, 4, 3, 5]
    assert inorder(root) == [2, 4, 1, 5, 3]
    assert postorder(root) == [4, 2, 5, 3, 1]
    assert height(root) == 3
    assert size(root) == 5
    print("✅ Binary Tree passed!")


def test_bst():
    values = [5, 3, 7, 2, 4, 6, 8]
    root = None
    for v in values:
        root = bst_insert(root, v)

    assert bst_inorder(root) == [2, 3, 4, 5, 6, 7, 8]
    assert bst_search(root, 4).value == 4
    assert bst_search(root, 10) is None
    assert bst_min(root).value == 2
    assert bst_max(root).value == 8

    root = bst_delete(root, 2)
    assert bst_inorder(root) == [3, 4, 5, 6, 7, 8]
    root = bst_delete(root, 3)
    assert bst_inorder(root) == [4, 5, 6, 7, 8]
    root = bst_delete(root, 7)
    assert bst_inorder(root) == [4, 5, 6, 8]
    assert is_valid_bst(root)

    print("✅ Binary Search Tree passed!")


if __name__ == "__main__":
    test_binary_tree()
    test_bst()
