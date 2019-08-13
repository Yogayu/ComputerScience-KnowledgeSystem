class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 2: 
            result = [[nums[0], nums[1]], [nums[1], nums[0]]]
            # print(result)
            return result
        result = []
        for num in nums:
            remain_nums = nums[:]
            remain_nums.remove(num)
            subs = self.permute(remain_nums)
            print(subs)
            print('---')
            all_subs = []
            for sub in subs:
                all_subs.append(sub.append(num))
            # print(all_subs)
            result = result + all_subs
        return result

def main():
    sol = Solution().permute([1, 2, 3])
    print(sol)

if __name__ == '__main__':
    main()
