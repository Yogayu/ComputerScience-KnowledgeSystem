# class Solution:
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
        
#         i = 0
#         j = 1
#         while j < len(nums): # j 应该比长度小
#             if nums[i] == nums[j]:
#                 j += 1
#             else:
#                 if i+1 != j:
#                     nums[i+1] = nums[j]
#                     i += 1
#                     j += 1
#             print(i,j)
#             print(nums)
#         return i+1
# def main():
#     result = Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4])
#     print(result)
# if __name__ == '__main__':
#     main()


# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return 0

#         i = 0
#         j = 1
#         while j < len(nums):  # j 应该比长度小
#             if nums[i] != nums[j]:
#                 if i+1 != j:
#                     nums[i+1] = nums[j]
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
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
            print(i, j)
            print(nums)
        return i+1

# 为什么不能判断i+1等于j的时候不交换？
# 是可以判断的，但是不论是否交换i都需要向前进一步，因为此时出现了不同值

'''
换个变量名，i记录慢的slow，j是快的fast
如果不加i+1!=j，不也是对的，而且更不容易出错吗？
关于这一点，和小伙伴一开始意见不合，因为他觉得这一步多此一举。一般情况已经包含。

但是我觉得这种思路没有错，只是一开始细节没注意到才会写错。
因为本来写算法就是这样的，一开始，考虑能适用一般情况的代码，这没有问题。
但是这个时候，不就应该想是不是有做了一些没有必要做的步骤？然后，去掉这些没有必要的步骤。
虽然这个题这样做的提升不大，但是不代表其他题的提升不大。主要是这种去掉不必要的操作的思路。
'''

def main():
    result = Solution().removeDuplicates([0,1,2,3])
    print(result)


if __name__ == '__main__':
    main()


# class Solution:
#     def removeDuplicates(self, nums):
#         if not nums:
#             return
#         slow = fast = 0
#         while fast <= len(nums) - 1:
#             if nums[fast] != nums[slow]:
#                 nums[slow+1] = nums[fast]
#                 slow += 1
#             fast += 1
#         return slow + 1

