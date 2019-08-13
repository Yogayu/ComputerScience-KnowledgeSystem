
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        s, e = 0, len(nums) - 1
        
        while s <= e:
            if nums[s] == val:
                nums[s], nums[e] = nums[e], nums[s]
                e -= 1
            else:
                s += 1
        return e + 1