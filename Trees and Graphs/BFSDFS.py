from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def dfs_preorder(self, root: Optional[TreeNode]) -> List[int]:
        # Return preorder traversal: Root -> Left -> Right
        result = []
        if not root:
            return result
        result.append(root.val)
        result.extend(self.dfs_preorder(root.left))
        result.extend(self.dfs_preorder(root.right))
        return result
    
    def dfs_inorder(self, root: Optional[TreeNode]) -> List[int]:
        # Return inorder traversal: Left -> Root -> Right
        result = []
        if not root:
            return result
        result.extend(self.dfs_preorder(root.left))
        result.append(root.val)
        result.extend(self.dfs_preorder(root.right))
        return result
    
    def dfs_postorder(self, root: Optional[TreeNode]) -> List[int]:
        # Return postorder traversal: Left -> Right -> Root
        result = []
        if not root:
            return result
        result.extend(self.dfs_preorder(root.left))
        result.extend(self.dfs_preorder(root.right))
        result.append(root.val)
        return result
    
    def bfs_level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Return level order traversal: level by level
        result = []
        if not root:
            return result
        queue = deque([root])
        while queue:
            level_size = len(queue)

            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.extend(level)

        return result


# Testing all traversal functions on the same tree
def test_traversals():
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))
    
    sol = Solution()
    
    print("Preorder:", sol.dfs_preorder(root))
    print("Inorder:", sol.dfs_inorder(root))
    print("Postorder:", sol.dfs_postorder(root))
    print("Level order:", sol.bfs_level_order(root))

# Run the tests
test_traversals()
