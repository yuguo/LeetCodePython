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
