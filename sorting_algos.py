# https://www.codingninjas.com/studio/problems/selection-sort_624469?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
# Time complexity: O(N2), (where N = size of the array), for the best, worst, and average cases.

from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    '''
    ###Selection sort 
    Need to loops the outer loop runs from 0 - N-1, the inner loop is responsiable for selecting
    the smallest element (possiable answer). 
    If outer loop current element is smaller then the selected inner loop then swap them.

    >>> [5,4,3,2,1]
    >>> [5] [4,3,2,1] ==> [1], [4,3,2,5]
    >>> [1 4] [3,2,1] ==> [1 2],[3,4,5]
    >>> [1,2,3][4,5] ==> [1,2,3][4,5]
    >>> [1,2,3,4] [5] ==> [1,2,3,4][5]
    >>> [1,2,3,4,5] [] STOP

    '''

    n = len(arr)

    ###outer loop 
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j

        if min != i:
            arr[min], arr[i] = arr[i], arr[min]

    return arr

# https://www.codingninjas.com/studio/problems/insertion-sort_624381?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
from typing import List

### O(N^2) for worst and average case.
# Best Case Time Complexity:
# The best case occurs if the given array is already sorted. And if the given array is already sorted,
# the outer loop will only run and the inner loop will run for 0 times.
# So, our overall time complexity in the best case will boil down to O(N), where N = size of the array.

def insertionSort(arr: List[int], n: int) -> None:
    # Write your code here
    '''
    >>> [2, 13, 4, 1, 3, 6, 28]
    >>> [2, 13, 4, 1, 3, 6, 28]
    >>> [2, 4, 13, 1, 3, 6, 28]
    >>> [2, 4, 1, ]
    '''

    for i in range(1, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            val = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = val
            j -= 1



# https://www.codingninjas.com/studio/problems/merge-sort_5846?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
def merge(arr, l, r, mid):

    left = l
    right = mid+1
    tmp = []

    while(left <= mid and right <= r):

        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1
    
    while left <= mid:
        tmp.append(arr[left])
        left += 1
    
    while right <= r:
        tmp.append(arr[right])
        right += 1
    
    
    for i in range(l, r+1):
        arr[i] = tmp[i-l]


def mergeSort(arr: List[int], l: int, r: int):
    # Write Your Code Here

    if l>=r: return 

    mid = (l + r) // 2

    ###call the left side from l to mid 
    mergeSort(arr,l, mid)

    ###call the right side from mid+1 to r
    mergeSort(arr, mid+1, r)

    merge(arr, l, r , mid)

# https://www.codingninjas.com/studio/problems/bubble-sort_624380?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def bubbleSort(arr: List[int], n: int):
    # Your code goes here.

    for i in range(n-1,0,-1):
        do_swap = False
        for j in range(i):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                do_swap = True #(best case scenario)

        if not do_swap: break


from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.

    # for i in range(n-1,0,-1): ###convert this to recursion
    #     do_swap = False
    #     for j in range(i):

    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #             do_swap = True
    #     if not do_swap: break

    if n == 1: return

    do_swap = False
    for j in range(n-1):

        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            do_swap = True

    if not do_swap: return

    bubbleSort(arr, n-1)

# https://www.codingninjas.com/studio/problems/quick-sort_5844?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
# Worst Case Time complexity: O(n2) 
# Time Complexity for the best and average case: O(N*logN)

"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def partitionArray(input: List[int], start: int, end: int) -> int:
    # Write your code here
    # pass
    pivot = input[start]
    i = start
    j = end

    while i < j:

        while input[i] <= pivot and i<=end-1:
            i += 1

        while input[j] > pivot and j >=start+1:
            j -= 1

        ###swap elements less then pivot to left
        ###swap elements greater then pivot to right
        if i < j:
            input[i], input[j] = input[j], input[i]

    ####insert pivot in correct place.
    input[j], input[start] = input[start], input[j]

    return j

def quickSort(input: List[int], start: int, end: int):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    # print(input)
    # print(start)
    # print(end)
    # return
    if start >= end: return

    partition_index = partitionArray(input, start, end)

    quickSort(input, start, partition_index-1)
    quickSort(input, partition_index+1, end)