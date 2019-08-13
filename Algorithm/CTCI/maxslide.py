from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base case
        result=[]
        if not nums or k <= 0 or len(nums)==0:
            return result
        # 双端队列
        d=deque([])
        for i in range(len(nums)):
            if d and i-d[0] >= k:
                    d.popleft()
            while d:
                if nums[i]<=nums[d[-1]]:
                    break
                else:
                    d.pop()
            d.append(i)

            if i >= k-1:
                result.append(nums[d[0]])
        return result