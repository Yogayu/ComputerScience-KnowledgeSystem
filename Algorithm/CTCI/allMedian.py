'''
@author: youxinyu
@date: 2018-9-3
'''

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, data):
        heapq.heappush(self.heap, data)
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def peek(self):
        return self.heap[0]
    
    def __len__(self):
        return len(self.heap)

    def __str__(self):
        result = 'The heap:\n'
        for item in self.heap:
            result = result + str(item) + ' '
        return result

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self,data):
        heapq.heappush(self.heap, -data)
    
    def pop(self):
        return -(heapq.heappop(self.heap))

    def peek(self):
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        result = 'The heap:\n'
        for item in self.heap:
            result = result + str(-item) + ' '
        return result


class getContinuousMedian:
    def __init__(self, input_list):
        self.list = input_list
        self.max_heap = MaxHeap()
        self.min_heap = MinHeap()
    
    def getMedians(self):
        medians = []
        for number in self.list:
            self._addToHeap(number)
            self._reblance()
            medians.append(self._getMedian())
        return medians

    def _addToHeap(self, number):
        if len(self.min_heap) < 1 or self.min_heap.peek() <= number:
            self.min_heap.push(number)
        else:
            self.max_heap.push(number)

    def _reblance(self):
        min_heap_size = len(self.min_heap)
        max_heap_size = len(self.max_heap)

        lager_heap = self.min_heap if min_heap_size > max_heap_size else self.max_heap
        smaller_heap = self.max_heap if min_heap_size > max_heap_size else self.min_heap

        if len(lager_heap) - len(smaller_heap) > 1:
            smaller_heap.push(lager_heap.pop())

    def _getMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap.peek() + self.max_heap.peek()) / 2.0
        median = self.min_heap.peek() if len(self.min_heap) > len(self.max_heap) else self.max_heap.peek()
        return median

def testGetMedians():
    medians = getContinuousMedian(
        [5, 2, 4, 1, 9, 10, 3, 8, -2, 6, 7, 1]).getMedians()
    print(medians)

def testHeap():
    print('Min heap test')

    min_heap = MinHeap()
    min_heap.push(6)
    min_heap.push(12)
    min_heap.push(14)
    min_heap.push(5)
    min_heap.push(9)
    
    print(min_heap)
    min_heap.pop()
    print(min_heap)
    print(len(min_heap))
    print('Max heap test')

    max_heap = MaxHeap()
    max_heap.push(6)
    max_heap.push(12)
    max_heap.push(14)
    max_heap.push(5)
    max_heap.push(9)

    print(max_heap)
    max_heap.pop()
    print(max_heap)
    print(len(max_heap))


def main():
    testGetMedians()

if __name__ == '__main__':
    main()




from collections import deque
class Solution:
    
    queue = deque()
    def updateQueue(self, nums,current,k):
        if len(self.queue)==k:
            self.queue.popleft()
        while self.queue and current > self.queue[0]:
            self.queue.popleft()
        self.queue.append(current)
    
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # init 
        result = []
        for i in range(k):
            self.updateQueue(nums,nums[i],k)
        result.append(self.queue[0])
        # 第一个元素一定是最大的元素
        for i in range(k,len(nums)):
            self.updateQueue(nums,nums[i],k)
            result.append(self.queue[0])
        return result
            
        
        