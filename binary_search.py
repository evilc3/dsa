# https://www.codingninjas.com/studio/problems/binary-search_972?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
#### Base of binary search
def search(nums: [int], target: int):
    # Write your code here.

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# https://www.canva.com/design/DADRwAjhxF0/Z21tg8BQ4Dyy5wGJclxWbA/edit?category=tACZCk6N0I4&utm_source=onboarding
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    #### relation item >= x

    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

# https://www.codingninjas.com/studio/problems/implement-upper-bound_8165383?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here
    #### relation item >= x

    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

# https://www.codingninjas.com/studio/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def searchInsert(arr: [int], m: int) -> int:
    # Write your code here
    #### relation item >= x

    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if arr[mid] >= m:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def ceil(arr, x, n):

    low = 0
    high = n - 1
    ans = n

    while low <= high:

        mid = (low + high) //2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans 

def floor(arr, x, n):

    low = 0
    high = n - 1
    ans = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans 

def ceilingInSortedArray(n, x, arr):

    arr.sort()

    floor_idx = floor(arr, x, n)
    ceil_idx = ceil(arr, x, n)
    
    a, b = [-1, n]

    if floor_idx != -1:
        a = arr[floor_idx]

    if ceil_idx != n:
        b = arr[ceil_idx]

    return ''.join(map( lambda x: str(x),[a, b]))


# https://www.codingninjas.com/studio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def first_occur(arr: [int], n: int, x: int) -> int:
    # Write your code here
    #### relation item >= x

    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if arr[mid] == x:
            ans = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return ans

def last_occur(arr: [int], n: int, x: int) -> int:
    # Write your code here
    #### relation item >= x

    low = 0
    high = n - 1
    ans = n 

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if arr[mid] == x:
            ans = mid
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return ans 

def firstAndLastPosition(arr, n, k):

    ####first occurance is equal to lower_bound 
    ####last occurance is equal to upper_bound - 1


    a = first_occur(arr, n , k)

    if a == -1:
        return -1, -1

    b = last_occur(arr, n, k)

    return a, b


def first_occur(arr: [int], n: int, x: int) -> int:

    low = 0
    high = len(arr) - 1
    ans = 0

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if arr[mid] == x:
            ans = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return ans

def last_occur(arr: [int], n: int, x: int) -> int:

    low = 0
    high = n - 1
    ans = 0

    while low <= high:

        mid = (low + high) // 2
        # mid = low + (high - low) // 2

        if arr[mid] == x:
            ans = mid
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1

    return ans


def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here

    last_idx = last_occur(arr, n , x)
    first_idx = first_occur(arr, n, x)

    if last_idx == first_idx == 0:
        return 0

    return last_idx - first_idx + 1



def binary_search(arr, n, x):

    low = 0
    high = n - 1
    ans = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            high = mid - 1
        
        else:
            low = mid + 1


    return ans



def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here

    idx = binary_search(arr, n , x)

    if idx == -1: return 0

    # print(idx)

    ###searching in left side
    ans = 1

    left = idx - 1

    while left >= 0 and arr[left] == x:
        ans += 1
        left -= 1

    ### searching in right side
    right = idx + 1

    while right < n and arr[right] == x:
        ans += 1
        right += 1

    return ans


# https://www.codingninjas.com/studio/problems/search-in-rotated-sorted-array_1082554?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def search_rotated_array_1(arr, n, k):
	
	low = 0
	high = n - 1

	while low <= high:

		mid = (low + high) // 2

		if arr[mid] == k:
			return mid 
		
		###find the sorted part 
		
		if arr[low] <= arr[mid]:
			###fist part is sorted

			### now check if k in present in this range
			if arr[low] <= k <= arr[mid]:
				high = mid - 1
			else:
				low = mid  + 1
		else:
			### second part is sorted

			if arr[mid] <= k <= arr[high]:
				low = mid + 1
			else:
				high = mid - 1
			
	
	return -1

# https://www.codingninjas.com/studio/problems/search-in-a-rotated-sorted-array-ii_7449547?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def searchInARotatedSortedArrayII(A : List[int], key : int) -> bool:
    
    low = 0
    high = len(A) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if A[mid] == key:
            return True

        ### to handle duplicates 
        if A[mid] == A[low] == A[high]:
            low += 1   
            high -= 1
            continue

        ####find the sorted half
        if A[low] <= A[mid]: ### fisrt part is sorted

            if A[low] <= key <= A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:

            if A[mid] <= key <= A[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False

# https://www.codingninjas.com/studio/problems/rotated-array_1093219?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def findMin(arr: [int]):

    n = len(arr)
    low = 0
    high = n - 1
    mini = float('inf')

    while low <= high:

        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            mini = min(mini, arr[low])
            low = mid + 1
        else:
            mini = min(mini, arr[mid])
            high = mid - 1

    return mini

# https://www.codingninjas.com/studio/problems/rotation_7449070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def findMin(arr: [int]):

    n = len(arr)
    low = 0
    high = n - 1
    mini = float('inf')
    idx = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[low] <= arr[mid]:
            # mini = min(mini, arr[low])
            if mini > arr[low]:
                mini = arr[low]
                idx = low

            low = mid + 1
        else:
            # mini = min(mini, arr[mid])
            if mini > arr[mid]:
                mini = arr[mid]
                idx = mid

            high = mid - 1

    return idx

def findKRotation(arr : [int]) -> int:

    return findMin(arr)

# https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def singleNonDuplicate(arr):
  
  ### not considering the 0th and nth index 
  ### rule  arr[i] != arr[i-1] or arr[i] != arr[i+1] this is the single number.
  ### elimination rule:
    ### using odd, even pos
    ### before the single number (ans), we will follow the (even, odd) trend.
    ### after the single number (ans), we will follow the (odd, even) trend.  

  ### if it only has one element
  if len(arr) == 1: return arr[0]

  ### handling it 0th and nth case.    
  if arr[0] != arr[1]: return arr[0]

  n = len(arr)

  if arr[n-1] != arr[n-2]: return arr[n-1]

  low = 1
  high = n - 2

  while low <= high:

    mid = (low + high) // 2

    ##check if single number
    if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
        return arr[mid]
    ##if we are in left half we eliminate it
    ##left half follows the order even, odd
    if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 != 0 and arr[mid] == arr[mid-1]):
        ## in the left half
        low = mid + 1
    else:
        ### else I am in right half
        high = mid - 1

  return -1


# https://www.codingninjas.com/studio/problems/find-peak-element_1081482?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def findPeakElement(arr: [int]) -> int:
    ####similar to single number

    ###peak number condition arr[i] > arr[i + 1] and arr[i] > arr[i - 1]
    n = len(arr)

    ### handle edge cases
    ### case 1: only one element
    if n == 1: return 0

    ### case 2: 0th index is a peak element
    if arr[0] > arr[1]: return 0

    ### case 3: nth index is a peak element
    if arr[n-1] > arr[n-2]: return n-1

    low = 1
    high = n - 2

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid

        ###check if your at the descending or the ascending part.
        if arr[mid] > arr[mid-1]:
            ###in the descending part
            low = mid + 1
        else:
            ### in the ascending part
            high = mid - 1

    return -1

# https://www.codingninjas.com/studio/problems/square-root-integral_893351?leftPanelTab=1&utm_medium=website&utm_campaign=a_zcoursetuf
def floorSqrt(n):
   # write your code logic here .
   low = 1
   high = n
   ans = -1

   while low <= high:

      mid = (low + high) // 2

      if mid*mid <= n:
         ans = mid
         low = mid + 1
      else:
         high = mid - 1

   return ans

n= int(input())
print(floorSqrt(n))

# https://www.codingninjas.com/studio/problems/nth-root-of-m_1062679?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTab=0
###brute force approach for python
def NthRoot(n: int, m: int) -> int:
    ### range should go from 1 to n

    for i in range(1, m):

        val = i ** n

        if val == m:
            return i
        elif val > m:
            return -1

def NthRoot(n: int, m: int) -> int:
    ### range should go from 1 to n
    
    # for i in range(1, m):

    #     val = i ** n 
        
    #     if val == m:
    #         return i
    #     elif val > m:
    #         return -1


    low = 1
    high = m

    while low <= high:

        mid = (low + high) // 2

        val = mid ** n

        if val == m:
            return mid
        elif val > m:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# https://www.codingninjas.com/studio/problems/minimum-rate-to-eat-bananas_7449064?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
import math
def total_hours(a, m):

    total_time = 0

    for i in a:
        if i <= m:
            total_time += 1
        else:
            total_time += int(math.ceil(i/m))
    
    return total_time

# ###brute force apporach
# def minimumRateToEatBananas(v: [int], h: int) -> int:
    

#     for m in range(1, max(v)+1):

#         t = total_hours(v, m)

#         if t <= h:
#             return m


def minimumRateToEatBananas(v: [int], h: int) -> int:
    

    low = 1
    high = max(v)
    ans = high

    while low <= high:

        mid = (low + high) // 2

        if total_hours(v, mid) <= h:
            ans = mid 
            high = mid - 1
        else:
            low = mid + 1
    
    return ans




from typing import List

# def total_bouquets(arr, k, days, m):

#     total = 0
#     curr = 0

#     for i in arr:
        
#         if i <= days:
#             curr += 1
#         else:
#             curr = 0

#         if curr == k:
#             total += 1
#             curr = 0

#             if total == m:
#                 return True

#     return False


# https://www.codingninjas.com/studio/problems/rose-garden_2248080?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def total_bouquets(arr, k, days, m):

    total = 0
    curr = 0

    for i in arr:

        if i <= days:
            curr += 1
        else:
            curr = 0

        if curr == k:
            total += 1
            curr = 0
            if total == m:
                return total

    return total

def roseGarden(arr: List[int], k: int, m: int):

    # for days in range(1, max(arr) + 1):

    #     if total_bouquets(arr, k, days, m):
    #         return days

    low = 1
    high = max(arr)
    ans = -1

    while low <= high:

        mid = (low + high) // 2

        # print(mid)

        val = total_bouquets(arr, k, mid, m)

        if val >= m:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

# https://www.codingninjas.com/studio/problems/smallest-divisor-with-the-given-limit_1755882?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
from os import *
from sys import *
from collections import *
from math import *

def calculate_sum(arr, divisor):

    ans = 0
    for i in arr:
        ans += ceil(i/divisor)
    return int(ans)

def smallestDivisor(arr: [int], limit: int) -> int:
    
    
    # for i in range(1, max(arr) + 1):

    #     val = calculate_sum(arr, i)

    #     if val <= limit:
    #         return i

    # return -1

    low = 1
    high = max(arr)
    ans = -1

    while low <= high:

        mid = (low + high) // 2

        val = calculate_sum(arr, mid)

        if val <= limit:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


# https://www.codingninjas.com/studio/problems/capacity-to-ship-packages-within-d-days_1229379?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def calculate_time(weights, cap):

    load = 0
    days = 1

    for i in weights:
        if load + i >  cap:
            days += 1
            load = i
        else:
            ##can load/take the package on the same day.
            load += i

    return days

def leastWeightCapacity(weights, d):
    
    # for cap in range(max(weights), sum(weights) + 1):

    #     days = calculate_time(weights, cap)

    #     # print(days, cap)

    #     if days <= d:
    #         return cap
    
    # return -1

    low = max(weights)
    high = sum(weights)
    ans = -1

    while low <= high:

        #possiable capacity 
        mid = (low + high) // 2

        days = calculate_time(weights, mid)

        if days <= d:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
        
    return ans


# https://www.codingninjas.com/studio/problems/kth-missing-element_893215?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from typing import *

def missingK(vec: List[int], n: int, k: int) -> int:
    # Write your code here.
    
    ### TC: O(N)
    ### SC: O(N) becz of the set.

    # vec = set(vec)

    # for i in range(1, max(vec) + 1):

    #     if i not in vec:
    #         k -= 1

    #         if k == 0:
    #             return i 

    # return -1

    ###binary search in applied on the index

    low = 0
    high = n-1

    while low <= high:

        mid = (low + high) // 2

        missing = vec[mid] - mid - 1

        if missing < k:
            low = mid + 1
        else:
            high = mid - 1

    return k + high + 1


# https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def can_place(stalls, k, dist):

    last = stalls[0]
    count = 1

    for curr in stalls[1:]:

        if curr - last >= dist:
            count += 1
            last = curr

        if count >= k:
            return True

    return False 


def aggressiveCows(stalls, k):

    stalls.sort()

    min_range = 1
    max_range = max(stalls) - min(stalls)

    # for dist in range(min_range, max_range+1):

    #     ###check if its possiable to place k cows in stalls given dist 
    #     if not can_place(stalls, k, dist):
    #         return dist - 1
    
    # return max_range    

    low = min_range
    high = max_range 
    ans = -1

    while low <= high:

        mid = (low + high) // 2

        val = can_place(stalls, k, mid)

        ###if true then this is a possiable answer 
        if val:
            ans = max(mid, ans)
            low = mid + 1
        else:
            high = mid - 1
    
    return ans


# https://www.codingninjas.com/studio/problems/allocate-books_1090540?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)

    # for pages in range(low, high + 1):
    #     if countStudents(arr, pages) == m:
    #         return pages

    while low <= high:

        mid = (low + high) // 2

        val = countStudents(arr, mid)


        if val > m:
            low = mid + 1
        else:
            high = mid - 1

    return low

# https://www.codingninjas.com/studio/problems/largest-subarray-sum-minimized_7461751?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def split_array(a, k, limit):

    prev = 0
    splits = 1

    for i in a:

        if i + prev <= limit:
            prev += i
        else:
            ###split
            splits += 1
            prev = i

    return splits

def largestSubarraySumMinimized(a: [int], k: int) -> int:


    low = max(a)
    high = sum(a)

    # for i in range(low, high+1):

    #     if split_array(a, k, i) == k:
    #         return i

    while low <= high:

        mid = (low + high) // 2

        val = split_array(a, k, mid)

        if val > k:
            low = mid + 1
        else:
            high = mid - 1

    return low

# https://www.codingninjas.com/studio/problems/painter-s-partition-problem_1089557?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def painters_requied(boards, max_load):

    painters = 1
    load = 0

    for i in boards:

        if i + load <= max_load:
            load += i
        else:
            ###move to next painter
            painters += 1
            load = i

    return painters


def findLargestMinDistance(boards:list, k:int):
    
    low_limit = max(boards)
    max_limit = sum(boards)

    # for max_load in range(low_limit, max_limit):

    #     val = painters_requied(boards, max_load)

    #     if val <= k:
    #         return max_load
    
    # return max_limit ##if k == 1

    
    low = low_limit
    high = max_limit

    while low <= high:

        mid = (low + high) // 2

        val = painters_requied(boards, mid)

        if val > k:
            low = mid + 1
        else:
            high = mid - 1

    return low


def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    ### TC: O(N * log(M))
    ### SC: (1)
    # for col_arr in mat:

    #     if col_arr[0] <= target <= col_arr[-1]:
    #         ###do search
    #         val = binary_search(col_arr, target) 

    #         if val != -1:
    #             return True 
    
    # return False

    ###approach

    n = len(mat)
    m = len(mat[0])

    low = 0
    high = (m * n) - 1

    while low <= high:

        mid = (low + high) // 2

        ###need to get row index and col index 
        col = mid % m
        row = mid // m
        
        if mat[row][col] == target:
            return True 
        elif mat[row][col] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return False


# https://www.codingninjas.com/studio/problems/median-of-a-row-wise-sorted-matrix_1115473?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

def lower_then(arr, x):

    low = 0
    high = len(arr) -1
    ans = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
        
    
    return ans + 1


def median(matrix: [[int]], m: int, n: int) -> int:
    
    ###brute force 
    ### TC: O(NXM * log(N*M))
    ### SC: O(NXM)

    ### x is mxn
    # ls = [] #O(x)
    
    # ###O(x)
    # for i in matrix:
    #     ls.extend(i)
    
    # ls.sort() ##xlogx

    # return ls[m*n//2]
    
    ####binary search 
    # low = min([matrix[i][0] for i in range(n)])
    # high = max([matrix[i][m-1] for i in range(n)])

    n = len(matrix)
    m = len(matrix[0])

    low = 1
    high = 10 ** 9
    median_index = (n * m) // 2

    while low <= high:

        mid = (low + high) // 2

        ###count the number of elements <= mid
        ###get all elements <= mid 
        cnt = 0
        for i in range(n):
            cnt += lower_then(matrix[i], mid)

        if cnt <= median_index:
            low = mid + 1
        else:
            high = mid - 1

    return low

