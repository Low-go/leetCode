from typing import Optional
from treeNode import TreeNode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter = 0
        temp1 = 0
        temp2 = 0

        if not root:
            return 0
        elif root.left is None and root.right is None:
            return 0
        elif root.left or root.right:
            counter += 1

        temp1 += self.maxDepth(root.left)
        temp2 += self.maxDepth(root.right)

        counter += max(temp1, temp2) + 1
        return counter


