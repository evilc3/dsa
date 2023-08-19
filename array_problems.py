from os import *
from sys import *
from collections import *
from math import *

# https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    ans = float("-inf")
    for i in arr:
        ans = max(ans, i)

    return ans

# https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    
    # if n == 2:
    #     return a 
    
    # mini = float("inf")
    # maxi = float("-inf")

    # for i in a:
    #     mini = min(mini, i)
    #     maxi = max(maxi, i)
    
    # ###ignore the mini and maxi 

    # ans_mini = float("inf")
    # ans_maxi = float("-inf")

    # for i in a:
    #     if i == mini or i == maxi: continue 
    #     ans_mini = min(ans_mini, i)
    #     ans_maxi = max(ans_maxi, i)
    
    # return [ans_maxi, ans_mini]

    small = second_small = float("inf")
    large = second_large = float("-inf")

    ### second variable has to be always behing first.
    for i in a:
        if i < small: 
            second_small = small 
            small = i 
        
        if i < second_small and i != small:
            second_small = i 
        
        if i > large:
            second_large = large
            large = i 
        
        if i > second_large and i != large:
            second_large = i

    return [second_large, second_small]

# https://www.codingninjas.com/studio/problems/remove-duplicates-from-sorted-array_1102307?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def removeDuplicates(arr,n):
    # Write your code here.
    
    num_unique_elements = 1
    prev = arr[0]

    for i in arr[1:]:
        if i != prev:
            prev = i 
            num_unique_elements += 1
    
    return num_unique_elements
        

from os import *
from sys import *
from collections import *
from math import *

# https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    # 3 1 6 5 10 7 6 6 1 7 
    # 1 6 5 10 7 6 6 1 7 3 
    # return  arr[1:] + [arr[0]]

    var = arr[0]

    for i in range(n-1):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    arr[n-1] = var

    return arr


# https://www.codingninjas.com/studio/problems/rotate-array_1230543?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

## TC: O(N)
## SC: O(N)

# ###O(N-K)
# for i in range(k, n):
#     tmp.append(arr[i])

# ###O(K)
# for i in range(k):
#     tmp.append(arr[i])

# for i in tmp:
#     print(i, end=" ")

## TC: O(N*K)
## SC: O(1)

# for i in range(k):

#     val = arr[0]

#     for j in range(n-1):

#         arr[j], arr[j+1] = arr[j+1], arr[j]

#     arr[n-1] = val

# print(arr)

# for i in arr:
#     print(i, end=" ")

# Approach 2: Using ” Reversal Algorithm “
# Step 1: Reverse the last k elements of the array

# Step 2: Reverse the first n-k elements of the array.

# Step 3: Reverse the whole array.

# For Eg , arr[]={1,2,3,4,5,6,7} , k=2

# step 1 output : {1,2,3,4,5,6,7} ==>  {1,2,3,4,5,7,6}
# step 2 output : {1,2,3,4,5,7,6} ==>  {5,4,3,2,1,7,6}
# step 3 output : {5,4,3,2,1,7,6} ==>  {6,7,1,2,3,4,5}

### For reversing in left 
### example : arr[]={1,2,3,4,5,6,7} , k=2
### correct output: 3 4 5 6 7 1 2
def reverse(arr, start, end):

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        end -= 1
        start += 1

    return arr

# print(arr)

# ###step 1 reverse last k elements
# arr = reverse(arr, k, n-1)

# # print(arr)

# ##step 2 reverse first n-k
# arr = reverse(arr, 0, k-1)

# # print(arr)

# # ### step 3  reverse the entire array
# arr = reverse(arr, 0, n-1)

# # print(arr)

# for i in arr:
#     print(i, end=" ")


# For Rotating Elements to right
# Step 1: Reverse the last k elements of the array

# Step 2: Reverse the first n-k elements of the array.

# Step 3: Reverse the whole array.

# For Eg , arr[]={1,2,3,4,5,6,7} , k=2
## examples : 6 7 1 2 3 4 5

arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 2

print(arr)

arr = reverse(arr, n-k, n-1)

print(arr)

arr = reverse(arr, 0, n-k-1)

print(arr)

arr = reverse(arr, 0, n-1)

print(arr)

### Move 0's to the end by array by maintaining the order of the non-negative numbers.
# https://www.codingninjas.com/studio/problems/ninja-and-the-zero-s_6581958?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.

    ### using two pointer method. 

    for j in range(n):

        if a[j] == 0:
            for i in range(j+1, n):

                if a[j] == 0 and a[i] != 0:
                    a[j], a[i] = a[i], a[j]
                    j += 1     
            break 
        
    return a

# https://www.codingninjas.com/studio/problems/linear-search_6922070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.

    for idx, i in enumerate(arr):
        if num == i:
            return idx

    return -1

# https://takeuforward.org/data-structure/union-of-two-sorted-arrays/
def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    
    out = []

    p1 = 0
    p2 = 0

    while p1 < len(a) and p2 < len(b):

        if a[p1] < b[p2]:
            out.append(a[p1])
            p1 += 1
        elif a[p1] > b[p2]:
            out.append(b[p2])
            p2 += 1
        
        elif a[p1] == b[p2]:

            out.append(a[p1])
            p1 += 1
            p2 += 1

        while p1 < len(a) and a[p1-1] == a[p1]:
            p1 += 1
            
        while p2 < len(b) and b[p2-1] == b[p2]:
            p2 += 1 

    # print(out)

    while p1 < len(a) and a[p1-1] != a[p1]:
        out.append(a[p1])
        p1 += 1
    
    while p2 < len(b) and b[p2-1] != b[p2]:
        out.append(b[p2])
        p2 += 1 
    
    # print(out)

    return out
        

# https://takeuforward.org/arrays/find-the-missing-number-in-an-array/ (need to see optimal approach 2 using xor.)
# https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: [int]) -> int:

        total_sum = sum(range(len(nums)+1))
        nums_sum = sum(nums)

        return total_sum - nums_sum


# https://www.codingninjas.com/studio/problems/find-the-single-element_6680465?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1from typing import *
# https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/
def getSingleElement(arr : [int]) -> int:
    # Write your code here.

    ans = arr[0]

    for i in arr[1:]:
        ans = ans ^ i

    return ans

# https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/
def getLongestSubarray(a: [int], k: int) -> int:
    # Write your code here
    
    n = len(a)
    length = 0
    
    for i in range(n):
        sum_i = 0
        for j in range(i, n):
            sum_i += a[j]

            if sum_i == k:
                length = max(length, j-i+1)

    return length

def longestSubarrayWithSumK(a: [int], k: int) -> int:

    left, right = 0, 0
    sum = a[0]
    length = 0
    n = len(a)

    while right < n:

        ###check left
        while(left <= right and sum > k):
            sum -= a[left]
            left += 1

        ###check if sum == k
        if sum == k:
            length = max(length, right-left+1)

        ###add the current element
        right += 1
        if right < n:
            sum += a[right]

    return length


# https://www.codingninjas.com/studio/problems/reading_6845742?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def twoSUM(n: int, book: [int], target: int) -> str:
    # Write your code here.
    
    ###brute force
    ## TC: O(N^2)
    ## SC: O(1)
    # for i in range(n):
    #     for j in range(i+1, n):

    #         if book[i] + book[j] == target:
    #             return 'YES'
    
    # return 'NO'

    ###better approach
    ## TC: O(N)
    ## SC: O(N)
    # mem = set(book)
    # for i in book:
    #     rem = target - i
    #     if rem in mem:
    #         return 'YES'
    
    # return 'NO'

    ##optimal approach
    ## TC: O(N)
    ## SC: O(1)
    low, high = 0, n-1

    book.sort()

    while low < high:

        ans = book[low] + book[high]

        if target == ans:
            return 'YES'
        elif ans > target:
            high -= 1
        else:
            low += 1

    return 'NO'


# https://www.codingninjas.com/studio/problems/sort-an-array-of-0s-1s-and-2s_892977?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def sortArray(arr, n):

	low, high = 0, n-1
	mid = low

	while mid <= high:

		if arr[mid] == 0:
			arr[mid], arr[low] = arr[low], arr[mid]
			low += 1
			mid += 1

		elif arr[mid] == 1:
			mid += 1

		else:
			arr[mid], arr[high] = arr[high], arr[mid]
			high -= 1

# https://www.codingninjas.com/studio/problems/majority-element_6783241?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
import math

def majorityElement(v: [int]) -> int:
    # Write your code here
    ## TC:  O(N*logN) + O(N). (O(N*logN)) takes logN to insert N elements.
    ## SC: O(Number of elements) O(N)

    # mem = {}

    # for i in v:
    #     mem[i] = mem.get(i, 0) + 1

    # n = math.floor(len(v) / 2)

    # for i in mem:
    #     if mem[i] > n:
    #         return i

    ##Moore's Voting Algorithem
    ### 5/2 == 2
    count = 0
    el = 0
    for i in v:
        if count == 0:
            count = 1
            el = i
        elif el == i:
            count += 1
        else:
            count -= 1

    ## if the question doesnt specify that there is an majority element then we need to
    ## check if count of el > floor(n / 2)
    ## here count cannot be used.
    count = 0
    for i in v:
        if i == el:
            count += 1

    return el if count > math.floor(len(v)/2) else -1
    # return el

# https://www.codingninjas.com/studio/problems/maximum-subarray-sum_630526?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def maxSubarraySum(arr, n):

    sum = 0
    ans = 0
    start = 0
    ansStart, ansEnd = -1, -1
    for idx, i in enumerate(arr):

        if sum == 0: start = idx

        sum += i

        # ans = max(ans, sum)
        if sum > ans:
            ans = sum

            ansStart = start
            ansEnd = idx

        if sum < 0:
            sum = 0


    for i in range(ansStart, ansEnd):
        print(arr[i], end = ' ')
    return ans

ans = maxSubarraySum(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4], n=9)
print('\n',ans)

# https://www.codingninjas.com/studio/problems/best-time-to-buy-and-sell-stock_6194560?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    ###when to buy: if the current is rate/value is less then I will buy
    ###when to sell:

    profit = float('-inf')
    buy = prices[0]

    for i in prices[1:]:

        if buy >= i:
            buy = i
        else:
            profit = max(profit, i - buy)

    return max(profit, 0)


# https://www.codingninjas.com/studio/problems/alternate-numbers_6783445?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.

    ## TC: O(2N) ~ O(N)
    ## SC: (N/2) + (N/2) = N
    # ans = []
    # pos = []
    # neg = []

    # for i in a:
    #     if i < 0:
    #         neg.append(i)
    #     else:
    #         pos.append(i)

    # neg_p = 0
    # pos_p = 0
    # for i in range(len(a)):
    #     if i % 2 == 0:
    #         ans.append(pos[pos_p])
    #         pos_p += 1
    #     else:
    #         ans.append(neg[neg_p])
    #         neg_p += 1

    # return ans

    ## TC: O(N)
    ## SC: O(1)

    ans = [0] * len(a)
    pos_p = 0
    neg_p = 1

    for idx, i in enumerate(a):

        if i > 0:
            if pos_p < len(a):
                ans[pos_p] = i
                pos_p += 2
        else:
            if neg_p < len(a):
                ans[neg_p] = i
                neg_p += 2

    return ans

from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    # Write your code here.

    n = len(arr)
    hashmap = {}
    sum_ = 0
    max_len = 0
    ### 0 1 2 3
    for i in range(n):

        sum_ += arr[i]
        if sum_ == 0:
            max_len = max(max_len, i+1)
        elif sum_ in hashmap:
            max_len = max(max_len, i - hashmap[sum_])
        else:
            hashmap[sum_] = i

    return max_len

# https://www.codingninjas.com/studio/problems/merge-all-overlapping-intervals_6783452?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from typing import *

def mergeOverlappingIntervals(arr : List[List[int]]) -> List[List[int]]:
    # Write your code here.

    ans = [arr[0]]

    for item in arr[1:]:

        ### L2 <= R1
        if item[0] <= ans[-1][1]:
            ans[-1] = [min(item[0], ans[-1][0]), max(item[1], ans[-1][1])]
        else:
            ans.append(item)

    return ans

##### PERFECT SOLUTION
from typing import List

def mergeOverlappingIntervals(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans


n = 195
numbers_list = [
    43, 187, 42, 194, 44, 150, 158, 17, 32, 131, 76, 74, 118, 163, 15, 129, 135, 38, 113, 81,
    89, 172, 148, 73, 151, 120, 166, 164, 100, 182, 4, 144, 56, 160, 34, 6, 52, 72, 84, 146,
    116, 54, 48, 95, 31, 46, 191, 22, 115, 168, 87, 26, 175, 90, 93, 161, 109, 128, 13, 71, 66,
    153, 176, 57, 70, 50, 62, 117, 16, 156, 11, 35, 75, 25, 97, 63, 105, 14, 28, 83, 33, 185,
    103, 21, 96, 152, 78, 133, 162, 106, 24, 68, 136, 195, 188, 91, 132, 102, 181, 7, 8, 124,
    60, 111, 55, 79, 2, 67, 99, 110, 122, 39, 77, 119, 127, 104, 37, 45, 121, 155, 85, 147, 165,
    1, 59, 12, 183, 137, 58, 123, 41, 180, 173, 126, 101, 157, 178, 18, 139, 69, 125, 36, 169,
    40, 171, 30, 138, 19, 82, 140, 3, 10, 88, 186, 190, 177, 5, 134, 179, 51, 184, 108, 92,
    66, 114, 53, 192, 86, 159, 142, 154, 112, 167, 20, 64, 149, 80, 49, 130, 145, 65, 61, 94,
    170, 107, 9, 23, 189, 174, 193, 27, 141, 143, 29, 47
]


def findMissingRepeatingNumbers(a):
    # Write your code here

    ##O (N)
    sum_a = sum([i for i in range(1, len(a)+1)])

    ##O (N)
    count = 1
    p = a[0]

    for i in a[1:]:
        if p == i:
            count += 1
        else:
            count -= 1

        if count == 0:
            count = 1
            p = i

    sum_a -= p

    for i in a:

        if i == p: continue

        sum_a -= i


    return [p, sum_a]
