class Solution(object):
    def longestPalindrome(self, s):
        singleSet = set()
        for char in s:
            if char in singleSet:
                singleSet.remove(char)
            else:
                singleSet.add(char)
        if not singleSet:
            return len(s)
        else:
            return len(s) - len(singleSet) + 1
