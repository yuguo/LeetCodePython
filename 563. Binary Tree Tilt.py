class Solution(object):
    def findTilt(self, root):
        if root:
            return abs(self.calTotal(root.left) - self.calTotal(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
        else:
            return 0
        
    def calTotal(self, root):
        if root:
            return root.val + self.calTotal(root.left) + self.calTotal(root.right)
        else:
            return 0

 # 优化后的代码：只递归单次

class Solution(object):
    def findTilt(self, root):
        diff = [0]
        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                diff[0] += abs(left - right)
                return left + right + root.val
            else:
                return 0
        dfs(root)
        return diff[0]
