class Solution(object):
    def diameterOfBinaryTree(self, root):
        currMax = [0]
        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                currMax[0] = max(left + right, currMax[0])
                return max(left, right) + 1
            else:
                return 0
            
        dfs(root)
        return currMax[0]
