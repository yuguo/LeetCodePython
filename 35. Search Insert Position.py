class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        l = len(nums) 
        while i < l:
            if target <= nums[i]:
                return i
            i += 1
        return l
