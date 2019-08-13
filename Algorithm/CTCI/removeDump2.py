# 10-13
# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
#         i = 0
#         j = 1
#         while j < len(nums):
#             flag = 0
#             if nums[i] != nums[j]:
#                 flag += 1
#                 if flag < 2:
#                     if i+1 != j:
#                         nums[i+1] = nums[j]
#                 i += 1
#             j += 1
#         return i+1


# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0
#         i = 0
#         j = 1
#         while j < len(nums):
#             if i-1 > 0 and nums[i-1] != nums[j]:
#                 nums[i+1] = nums[j]
#                 i += 1
#             elif nums[i] != nums[j]:
#                 nums[i+1] = nums[j]
#                 i += 1
#             j += 1
#             print(i, j)
#             print(nums)
#         return i+1


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        j = 1
        while j < len(nums):
            unique = nums[i] != nums[j]
            if i > 0:
                twice = nums[i] == nums[j] and nums[i-1] != nums[j]
            else:
                twice = nums[i] == nums[j]
            
            if unique or twice:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1

def main():
    result = Solution().removeDuplicates([1, 1, 1, 2, 2, 3, 3, 4])
    print(result)

if __name__ == '__main__':
    main()
