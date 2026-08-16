# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        res = []

        queue.append(root)

        while queue:
            level = [] # track current level
            q_len = len(queue)
            for _ in range(q_len):
                curr = queue.popleft() # current node
                
                if curr: # if not null, add children for processing
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if level: # add each level to the result array
                res.append(level)

        return res


                
        