# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        def dfs(node,currDepth, parent):
            if depth == currDepth:
                newNode = TreeNode(val)
                if node == parent.left:
                    parent.left = newNode
                    newNode.left = node
                else:
                    parent.right = newNode
                    newNode.right = node
            elif depth == currDepth-1 and node.left == None and node.right == None:
                node.left = TreeNode(val)
                node.right = TreeNode(val)
            elif node == None:
                return
            else:
                dfs(node.left, currDepth+1, node)
                dfs(node.right, currDepth+1, node)

        
        dfs(root, 1, None)
        
        return root