'''
@author: youxinyu
@date: 2018-9-1
'''

class Heap():

    def __init__(self, capacity):
        self.items = []
        self.size = 0
        self.capacity = capacity
    
    def getParentIndex(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0:
            return parent_index
        return None
    
    def getLeftIndex(self, index):
        left_index = index * 2 + 1
        if left_index < self.size:
            return left_index
        return None

    def getRightIndex(self, index):
        right_index = index * 2 + 2
        if right_index < self.size:
            return right_index
        return None

    def getLeft(self, index):
        left_index = self.getLeftIndex(index)
        if left_index:
            return self.items[left_index]
        return None

    def getRight(self, index):
        right_index = self.getRightIndex(index)
        if right_index:
            return self.items[right_index]
        return None

    def getParent(self, index):
        parent_index = self.getParentIndex(index)
        if parent_index:
            return self.items[parent_index]
        return None
    
    def checkCapacity(self):
        if self.size > self.capacity:
            self.capacity = self.capacity * 2

    def peek(self):
        if len(self) > 0:
            return self.items[0]
        return None
    
    def poll(self):
        if self.size < 1:
            return None
        self.items[0] = self.items[self.size-1]
        self.items.pop()
        self.size -= 1
        self.heapfiyDown()

    def swap(self, higher_index, samller_index):
        self.items[higher_index], self.items[samller_index] = self.items[samller_index], self.items[higher_index]

    def heapfiyDown(self):
        index = 0
        while index < self.size:
            left_index = self.getLeftIndex(index)
            right_index = self.getRightIndex(index)

            if left_index == None and right_index == None:
                return

            if left_index != None:
                samller_index = left_index
            if right_index != None:
                right = self.items[right_index]
                left = self.items[left_index]
                if right < left:
                    samller_index = right_index
            
            if self.items[index] > self.items[samller_index]:
                self.swap(samller_index, index)
                index = samller_index
            else:
                return
    
    def heapfiyUp(self):
        index = self.size
        while index > 0:
            parent_index = self.getParentIndex(index)
            if parent_index != None:
                parent = self.items[parent_index]
                if parent > self.items[index]:
                    self.swap(parent_index, index)
                    index = parent_index
                else:
                    return

    def add(self, data):
        self.checkCapacity()
        self.items.append(data)
        self.heapfiyUp() 
        self.size += 1

    def __len__(self):
        return len(self.items)

    def __str__(self):
        result = 'The heap:\n'
        for item in self.items:
            result = result + str(item) + ' '
        return result

def main():
    minHeap = Heap(10)
    
    minHeap.add(6)
    print(minHeap)
    
    minHeap.add(1)
    print(minHeap)
    
    minHeap.add(10)
    print(minHeap.peek())
    print(minHeap)
    
    minHeap.poll()
    print(minHeap)
    
    minHeap.add(-2)
    print(minHeap)

    minHeap.poll()
    print(minHeap)
    minHeap.add(5)
    minHeap.add(5)
    print(minHeap)


if __name__ == '__main__':
    main()
