'''
@author: youxinyu
@date: 2018-8-27
'''


def bubbleSort(unsorted_list):
    swap_range = len(unsorted_list) - 1
    is_Sorted = False
    while not is_Sorted:
        is_Sorted = True
        for i in range(swap_range):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                is_Sorted = False
        # After each sort turn, the last one will not changed
        swap_range -= 1
    return unsorted_list


def mergeSort(unsorted_list):
    length = len(unsorted_list)
    if length > 1:
        middle = int(length/2)
        left_list = unsorted_list[0:middle]
        right_list = unsorted_list[middle:length]

        left_list = mergeSort(left_list)
        right_list = mergeSort(right_list)
        return merge(left_list, right_list)
    else:
        return unsorted_list


def merge(left_list, right_list):
    temple_sorted_list = []
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] > right_list[0]:
            temple_sorted_list.append(right_list[0])
            right_list.pop(0)
        else:
            temple_sorted_list.append(left_list[0])
            left_list.pop(0)

        temple_sorted_list.extend(left_list + right_list)

    return temple_sorted_list


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


def main():
    unsorted_list = [39, 2, 32, 1, 9, 0, 34, 2, 18, 20, 87, 57, 10]
    # sortedList = bubbleSort(unsorted_list)
    # print(sortedList)
    # print(mergeSort(unsorted_list))

    qucikSort(unsorted_list, 0, len(unsorted_list)-1)
    print(unsorted_list)


if __name__ == '__main__':
    main()
