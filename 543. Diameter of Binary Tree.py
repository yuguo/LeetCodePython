class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.currMax = 0
        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                currMax = max(left + right, self.currMax)
                return max(left, right) + 1
            else:
                return 0
            
        dfs(root)
        return self.currMax
