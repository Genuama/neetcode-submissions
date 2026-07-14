# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #breadth first search
        #first check for an empty case and return
        #perform bfs and swap the left and right nodes in the process


        if not root:
            return 

        queue = deque([root])

        while queue:
            current_node = queue.popleft()

            current_node.left, current_node.right =  current_node.right ,current_node.left

            #add the children of the queue for further processing
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return root
       
      
       