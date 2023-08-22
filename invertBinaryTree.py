from typing import Optional
from treeNode import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            root_hold = root.left
            root.left = root.right
            root.right = root_hold
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root



soltuion = Solution()
tree1 = TreeNode(3)
tree2 = TreeNode(4)
tree3 = TreeNode(4, tree1, tree2)
result = soltuion.invertTree(tree3)
print(result)

