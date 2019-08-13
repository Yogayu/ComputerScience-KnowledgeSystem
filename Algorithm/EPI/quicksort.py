
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # 将小于部分从左到右排列
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j] < pivot:
                A[j],A[i] = A[i],A[j]
                break
    # 将大于部分从右到左排列
    for i in reversed(range(len(A))):
        if pivot > A[i]:
            break
        for j in reversed(range(len(i))):
            if A[j] > pivot:
                A[i],A[j] = A[j],A[i]
                break

# 优化：每次都重头开始找，没有必要
# we make a single pass and move all the elements less than the pivot to the beginning. 
def dutch_flag_partition_2(pivot_index, A):
    pivot = A[pivot_index]
    # 记录当前最小部分的右边位置，循环一轮即可
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i],A[smaller] = A[smaller],A[i]
            smaller += 1
    # 记录当前最大部分的左边位置，循环一轮即可
    larger = len(A)
    for i in reversed(range(len(A))):
        if A[i] < pivot: 
            break
        if A[i] > pivot:
            A[i],A[larger] = A[larger],A[i]
            larger -= 1

def qucikSort(unsorted_list, left, right):
    if left < right:
        prvoit = unsorted_list[(left + right) // 2]
        index = portition(unsorted_list, left, right, prvoit)
        qucikSort(unsorted_list, left, index-1)
        qucikSort(unsorted_list, index, right)


def portition(unsorted_list, left, right, prvoit):
    while left <= right:
        while unsorted_list[left] < prvoit:
            left += 1
        while unsorted_list[right] > prvoit:
            right -= 1
        if left <= right:
            unsorted_list[left], unsorted_list[right] = unsorted_list[right], unsorted_list[left]
            left += 1
            right -= 1
    return left

def dutch_flag_partition3(pivot_index, A):
    pivot = pivot_index
    # Keep the following invariants during partitioning:
    # botton group: A[:sma]IerJ.
    # niddle gtoup: lfsnal]er:equa7l.
    # unc]assifi ed. group: A[equal: Targer] .
    # top group: A[Targer: ] .
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as -Iong as there is an unclassified elenent while equal < larger:
    # A[equa7] is the inconing unclassjfied element, 
    if A[equal] < pivot:
        A[smaller], A[equal] = A[equal], A[smaller]
        smaller , equal = smaller + 1, equal + 1 
    elif A[equal] == pivot:
        equal += 1
    else: # A[equal] > pivot.
        larger -= 1
        A[equal], A[larger] = A[larger], A[equal]