class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        depth = 1;
        while x > depth * 10:
            depth *= 10
        
        while x:
            if x % 10 != x // depth:
                return False
            x = x % depth // 10
            depth = depth // 100
        return True
