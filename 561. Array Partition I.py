class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, s = 0, 0
        l = len(nums) - 1
        while i < l:
            if i % 2 == 0:
                s += min(nums[i], nums[i+1])
            i += 1
        return s
